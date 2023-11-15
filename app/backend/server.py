import os
from datetime import datetime
import pkg_resources
import requests
import json
from flask import Flask, request, send_file, jsonify
from flask_socketio import SocketIO
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from gradio_client import Client
import uuid
import platform

# Identify the current operating system
current_os = platform.system()

if current_os == 'Windows':
    path_delimiter = '\\'
else:
    path_delimiter = '/'

chat_history = [
]

CACHE_DIR = pkg_resources.resource_filename(__name__, "cache")

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backend.db'
db = SQLAlchemy(app)

CORS(app)

API_KEY = "tvGX7YwZGsaT3Vez8IMDSl8i",
SECRET_KEY = "HO6dIOw4duyPQQULQ71ug3y6xnPF4OVM"

limiter = Limiter(
    app=app,
    key_func=get_remote_address  # 使用请求的远程地址作为标识符
)


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token")
               )


# index page
@app.route("/api/")
def index():
    return "<p>Welcome to lemon5!</p>"


# text-to-speech
@app.route("/api/tts", methods=["GET"])
def tts():
    # Extract data from the incoming request
    data = request.args  # Get JSON data sent in the POST request
    text = data.get('text')
    format = data.get('format')
    speaker = data.get('speaker')
    sdp = data.get('sdp')
    noise = data.get('noise')
    noisew = data.get('noisew')
    length = data.get('length')
    try:
        if speaker == '丁真':
            cache_dir = 'cache'
            if not os.path.exists(cache_dir):
                os.makedirs(cache_dir)
            client = Client("https://modelscope.cn/api/v1/studio/MiDd1Eye/DZ-Bert-VITS2/gradio/",
                            output_dir=cache_dir)
            result = client.predict(
                text,  # str in 'Text' Textbox component
                "Speaker",  # str (Option from: ['Speaker']) in 'Speaker' Dropdown component
                float(sdp),  # int | float (numeric value between 0.1 and 1) in 'SDP/DP混合比' Slider component
                float(noise),  # int | float (numeric value between 0.1 and 1) in '感情调节' Slider component
                float(noisew),  # int | float (numeric value between 0.1 and 1) in '音素长度' Slider component
                float(length),  # int | float (numeric value between 0.1 and 2) in '生成长度' Slider component
                fn_index=0
            )
            print("result:")
            print(result[1])
            dirname, filename = result[1].split(path_delimiter)[-2], result[1].split(path_delimiter)[-1]
            newfilename = dirname + '.wav'
            # move file one level up
            os.rename(os.path.join('cache', dirname, filename), os.path.join('cache', newfilename))
            # remove folder
            os.rmdir(os.path.join('cache', dirname))
            socketio.emit('notification', {'message': f'{speaker}语音合成完成',
                                           'time': str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
            return jsonify({'filename': newfilename})
        else:
            # Define the API endpoint and parameters as per API documentation
            api_url = 'http://genshinvoice.top/api'
            params = {'speaker': speaker+"_ZH",
                      'text': text,
                      'format': format,
                      'language': 'ZH',
                      'sdp': sdp,
                      'noise': noise,
                      'noisew': noisew,
                      'length': length
                      }


            # Make a request to the TTS API
            response = requests.get(api_url, params=params)
            if response.headers.get('Content-Type') == 'audio/wav':
                # Generate a unique filename
                filename = f"{uuid.uuid4()}.wav"
                cache_dir = 'cache'
                if not os.path.exists(cache_dir):
                    os.makedirs(cache_dir)

                file_path = os.path.join(cache_dir, filename)

                # Save the audio file
                with open(file_path, 'wb') as audio_file:
                    audio_file.write(response.content)

                socketio.emit('notification', {'message': f'{speaker}语音合成完成',
                                               'time': str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
                # Return the filename to the frontend
                return jsonify({'filename': filename})
            else:
                socketio.emit('notification', {'message': f'{speaker}语音合成完成',
                                               'time': str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
                return jsonify({'error': 'Invalid content type received'}), 400
    except Exception as e:
        print(e)
        # pass to front end with current time
        socketio.emit('notification', {'message': f'{speaker}语音合成失败',
                                       'time': str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
        return jsonify({'error': 'Invalid content type received'}), 400



# # voice conversion
# @app.route("/api/vc", methods=["POST", "GET"])
# @limiter.limit("50 per minute")
# def vc():
#     if "src_audio" not in request.files:
#         return "No src_audio file uploaded."
#
#     if "tgt_audio" not in request.files:
#         return "No tgt_audio file uploaded."
#
#     src_audio = request.files["src_audio"]
#     src_audio_path = os.path.join(CACHE_DIR, src_audio.filename)
#     src_audio.save(src_audio_path)
#
#     tgt_audio = request.files["tgt_audio"]
#     tgt_audio_path = os.path.join(CACHE_DIR, tgt_audio.filename)
#     tgt_audio.save(tgt_audio_path)
#
#     out_audio = convert_voice(src_audio_path, tgt_audio_path)
#     out_filename = "{}-to-{}.wav".format(src_audio.filename.split('.')[0], tgt_audio.filename.split('.')[0])
#     out_path = os.path.join(CACHE_DIR, out_filename)
#     write(out_path, 16000, out_audio)
#
#     try:
#         return send_file(out_path, mimetype="audio/wav", as_attachment=True)
#     finally:
#         os.remove(out_path)

@app.route("/api/chat", methods=["POST"])
@cross_origin()
def chat():
    data = request.json  # Get JSON data sent in the POST request
    prompt = data.get("prompt")
    character = data.get("character")
    newConv = data.get("newConv")

    with open(f"sysprompts/{character}.txt", "r", encoding='utf-8') as f:
        sysprompt = f.read()

    if newConv:
        chat_history.clear()

    chat_history.append({"role": "user", "content": prompt})
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()
    payload = json.dumps({"messages": chat_history, "system": sysprompt})
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload).json()
    print(response)
    chat_history.append({"role": "assistant", "content": response['result']})


    # tts
    audio_url = tts_for_chat(response['result'],character)
    # Construct the response object
    bot_message = {
        "character": character,  # Replace with actual sender if available
        "response": response['result'],
        "mode": "audio",  # Replace with actual mode if available
        "audioURL": audio_url,
    }

    return jsonify(bot_message)

@app.route('/api/audio/<path:filename>', methods=['GET', 'POST'])
@cross_origin()
def serve_audio(filename):
    # Replace 'path_to_file.wav' with the actual file path
    path_to_wav_file = 'cache/' + filename
    return send_file(
        path_to_wav_file,
        mimetype='audio/wav',
        as_attachment=True,
    )


def tts_for_chat(text,charactor):
    cache_dir = 'cache'
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    if charactor == '丁真':
        client = Client("https://modelscope.cn/api/v1/studio/MiDd1Eye/DZ-Bert-VITS2/gradio/",
                        output_dir=cache_dir)
        result = client.predict(
            text,  # str in 'Text' Textbox component
            "Speaker",  # str (Option from: ['Speaker']) in 'Speaker' Dropdown component
            0.2,  # int | float (numeric value between 0.1 and 1) in 'SDP/DP混合比' Slider component
            1,  # int | float (numeric value between 0.1 and 1) in '感情调节' Slider component
            0.3,  # int | float (numeric value between 0.1 and 1) in '音素长度' Slider component
            1,  # int | float (numeric value between 0.1 and 2) in '生成长度' Slider component
            fn_index=0
        )
        print("result:")
        print(result[1])
        dirname, filename = result[1].split(path_delimiter)[-2], result[1].split(path_delimiter)[-1]
        newfilename = dirname + '.wav'
        # move file one level up
        os.rename(os.path.join('cache', dirname, filename), os.path.join('cache', newfilename))
        # remove folder
        os.rmdir(os.path.join('cache', dirname))
        return newfilename
    else:
        # Define the API endpoint and parameters as per API documentation
        api_url = 'http://genshinvoice.top/api'
        params = {'speaker': charactor+"_ZH",
                  'text': text,
                  'format': 'wav',
                  'language': 'ZH',
                  'sdp': 0.2,
                  'noise': 1,
                  'noisew': 0.3,
                  'length': 1
                  }

        # Make a request to the TTS API
        response = requests.get(api_url, params=params)
        if response.headers.get('Content-Type') == 'audio/wav':
            # Generate a unique filename
            filename = f"{uuid.uuid4()}.wav"
            cache_dir = 'cache'
            if not os.path.exists(cache_dir):
                os.makedirs(cache_dir)

            file_path = os.path.join(cache_dir, filename)

            # Save the audio file
            with open(file_path, 'wb') as audio_file:
                audio_file.write(response.content)

            # Return the filename to the frontend
            return filename
        else:
            socketio.emit('notification', {'message': f'{charactor}语音合成失败',
                                           'time': str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
            return jsonify({'error': 'Invalid content type received'}), 400



@app.errorhandler(429)
def ratelimit_error(e):
    print("Ratelimit exceeded: ", str(e.description))
    return jsonify(error="ratelimit exceeded", message=str(e.description)), 429

# ----- DataBase -----
# Database model for Attribute
class Voice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    avatar = db.Column(db.String(200), nullable=False)
    audio = db.Column(db.String(200), nullable=False)

    # Relationship with attributes
    attributes = db.relationship('Attribute', backref='voice', lazy=True)


class Attribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    element = db.Column(db.String(5), nullable=False)
    style = db.Column(db.String(5), nullable=False)

    # Foreign Key to Voice
    voice_id = db.Column(db.Integer, db.ForeignKey('voice.id'), nullable=False)


@app.route('/api/voices', methods=['GET'])
def get_filtered_voices():
    # Fetch query parameters
    name_query = request.args.get('name')
    element_query = request.args.get('element')
    style_query = request.args.get('style')

    # Base query
    query = Voice.query

    # Apply filters based on query parameters
    if name_query:
        query = query.filter(Voice.name.contains(name_query))

    if any([element_query, style_query]):
        query = query.join(Attribute).filter(
            and_(
                or_(Attribute.element == element_query, element_query is None),
                or_(Attribute.style == style_query, style_query is None),
            )
        )

    voices = query.all()
    return jsonify([{'id': voice.id, 'name': voice.name, 'avatar': voice.avatar, 'audio': voice.audio,
                     'attributes': [{'element': attribute.element, 'style': attribute.style}
                                    for attribute in voice.attributes]}
                    for voice in voices])


# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


# User Registration Endpoint
@app.route('/api/signup', methods=['POST'])
def register():
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']  # In a real app, you should hash passwords
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'message': '邮箱已被注册'}), 400

    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201


# User Login Endpoint
@app.route('/api/signin', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email, password=password).first()
    if user:
        socketio.emit('notification', {'message': f'{user.name}登录成功',
                                       'time': str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
        return jsonify({'user': user.name}), 200
    else:
        return jsonify({'message': '用户名或密码错误'}), 401

@app.route('/api/signout', methods=['POST'])
def logout():
    # clear cache
    for filename in os.listdir('cache'):
        os.remove(os.path.join('cache', filename))
    # clear chat history
    chat_history.clear()
    return jsonify({'message': 'User logout successfully'}), 200

# Database model for Notification
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)
