import os
import datetime
from flask import Flask, request, send_file, jsonify
from scipy.io.wavfile import write, read
from tts import synthesize
from se import denoise
from vc import voice_conversion
from chat import chat_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={
    r"/tts*": {"origins": "https://210f839e.r9.cpolar.top"},
    r"/chat*": {"origins": "https://210f839e.r9.cpolar.top"}
})

limiter = Limiter(
    app=app,
    key_func=get_remote_address  # 使用请求的远程地址作为标识符
)

cache_dir = "/mnt/d/Coding/Projects/Lemon5/lemon5/app/backend/cache"
# cache_dir = "D:\Coding\Projects\Lemon5\lemon5\app\backend\cache"

@app.route("/")
def index():
    return "<p>Welcome to lemon5!</p>"

@app.route("/tts", methods=["POST", "GET"])
@limiter.limit("50 per minute") 
def tts():
    """Text-to-speech.
    """
    
    text = request.args.get("text")
    lang = request.args.get("lang", "ja")
    if text:
        audio = synthesize(text=text, lang=lang)
        file_name = "tts_{}.wav".format(lang)
        file_path = os.path.join(cache_dir, file_name)
        write(file_path, 22050, audio)
        try:
            return send_file(file_path, mimetype="audio/wav", as_attachment=True)
        finally:
            os.remove(file_path)
    else:
        return "Input text is invalid."

@app.route("/se", methods=["POST", "GET"])
@limiter.limit("50 per minute") 
def se():
    """Speech enhancement.
    """

    if "audio" not in request.files:
        return "No audio file uploaded."

    audio_file = request.files["audio"]
    file_name = audio_file.file_name
    file_path = os.path.join(cache_dir, file_name)
    audio_file.save(file_path)

    clean_audio = denoise(file_path)
    save_name = "se_{}".format(file_name)
    save_path = os.path.join(cache_dir, save_name)
    write(save_path, 16000, clean_audio)
    try:
        return send_file(save_path, mimetype="audio/wav", as_attachment=True)
    finally:
        os.remove(save_path)

@app.route("/vc", methods=["POST", "GET"])
@limiter.limit("50 per minute") 
def vc():
    """Voice conversion
    """

    if "src_audio" not in request.files:
        return "No src_audio file uploaded."

    if "tgt_audio" not in request.files:
        return "No tgt_audio file uploaded."
    
    src_audio = request.files["src_audio"]
    src_audio_path = os.path.join(cache_dir, src_audio.filename)
    src_audio.save(src_audio_path)
    
    tgt_audio = request.files["tgt_audio"]
    tgt_audio_path = os.path.join(cache_dir, tgt_audio.filename)
    tgt_audio.save(tgt_audio_path)

    out_audio = voice_conversion(src_audio_path, tgt_audio_path)
    out_filename = "{}-to-{}.wav".format(src_audio.filename.split('.')[0], tgt_audio.filename.split('.')[0])
    out_path = os.path.join(cache_dir, out_filename)
    write(out_path, 16000, out_audio)

    try:
        return send_file(out_path, mimetype="audio/wav", as_attachment=True)
    finally:
        os.remove(out_path)

@app.route("/chat", methods=['POST'])
def chat():
    json_post_list = request.json
    character = json_post_list.get('character', '派蒙')  # 从请求中获取角色名，默认为派蒙
    response, history = chat_response(json_post_list)
    
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    answer = {
        "response": response,
        "history": history,
        "status": 200,
        "time": time,
        "character": character  # 在响应中返回角色名
    }
    log = "[" + time + "] " + '", prompt:"' + json_post_list.get('prompt') + '", response:"' + repr(response) + '", character:"' + character + '"'
    print(log)
    
    return jsonify(answer)

@app.errorhandler(429)
def ratelimit_error(e):
    print("Ratelimit exceeded: ", str(e.description))
    return jsonify(error="ratelimit exceeded", message=str(e.description)), 429

if __name__ == "__main__":
    app.run(debug=True)
