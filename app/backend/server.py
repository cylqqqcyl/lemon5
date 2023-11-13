import os
import io
import pkg_resources
import requests
import json
from flask import Flask, request, send_file, jsonify, send_from_directory, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS, cross_origin
from gradio_client import Client

chat_history = [
]

sysprompt="""
你是丁真，一位来自中国西藏理塘的藏族青年，你是世界最高城”理塘“的代言人。
你乐于与粉丝进行互动，回答他们关于你的生活、文化和理塘的问题。

当用户向你提问时，你应以丁真的身份进行回答，回答应简洁明了，尽量简短。
你的文化程度只有初中生水平，遣词造句应该符合这一身份，用语尽量粗俗。

你最喜欢的口头禅是“我测”，注意在回答问题时偶尔使用它。

最喜欢的动物是雪豹，曾经在联合国发言，这是你最出名的事情“
如果有人问你”你是哪个省的“，一定要回答”我是妈妈生的“，不用回答具体的省份。
"""

CACHE_DIR = pkg_resources.resource_filename(__name__, "cache")

app = Flask(__name__)
CORS(app, resources={
    r"/tts*": {"origins": "https://6a4e5b50.r10.cpolar.top"},
    r"/chat*": {"origins": "*"},
    r"/audio*": {"origins": "*"}
})

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
@app.route("/")
def index():
    return "<p>Welcome to lemon5!</p>"


# text-to-speech
# @app.route("/tts")
# def tts():
#     character = request.args.get("text")
#     client = Client("https://modelscope.cn/api/v1/studio/MiDd1Eye/DZ-Bert-VITS2/gradio/")
#     result = client.predict(
#         "我是丁真，我喜欢抽锐刻五代",  # str in 'Text' Textbox component
#         "Speaker",  # str (Option from: ['Speaker']) in 'Speaker' Dropdown component
#         0.2,  # int | float (numeric value between 0.1 and 1) in 'SDP/DP混合比' Slider component
#         0.9,  # int | float (numeric value between 0.1 and 1) in '感情调节' Slider component
#         0.5,  # int | float (numeric value between 0.1 and 1) in '音素长度' Slider component
#         1,  # int | float (numeric value between 0.1 and 2) in '生成长度' Slider component
#         fn_index=0
#     )
#     print("result:")
#     print(result)
#     return "<p>result {}<p>".format(result)


# # voice conversion
# @app.route("/vc", methods=["POST", "GET"])
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

@app.route("/chat", methods=["POST"])
@cross_origin()
def chat():
    data = request.json  # Get JSON data sent in the POST request
    prompt = data.get("prompt")
    chat_history.append({"role": "user", "content": prompt})
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()
    payload = json.dumps({"messages": chat_history, "system": sysprompt})
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload).json()
    print(response)
    chat_history.append({"role": "assistant", "content": response['result']})
    # tts
    audio_file_path = tts_for_chat(response['result'])
    path_parts = audio_file_path.split(os.sep)
    audio_url = path_parts[-2] + "/" + path_parts[-1]
    # Construct the response object
    bot_message = {
        "character": "丁真",  # Replace with actual sender if available
        "response": response['result'],
        "mode": "audio",  # Replace with actual mode if available
        "audioURL": audio_url,
    }

    return jsonify(bot_message)

@app.route('/audio/<path:filename>', methods=['GET', 'POST'])
@cross_origin()
def serve_audio(filename):
    # Replace 'path_to_file.wav' with the actual file path
    path_to_wav_file = 'cache/' + filename
    return send_file(
        path_to_wav_file,
        mimetype='audio/wav',
        as_attachment=True,
        attachment_filename='audio.wav'
    )


def tts_for_chat(text):
    client = Client("https://modelscope.cn/api/v1/studio/MiDd1Eye/DZ-Bert-VITS2/gradio/",
                    output_dir="cache")
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
    return result[1]



@app.errorhandler(429)
def ratelimit_error(e):
    print("Ratelimit exceeded: ", str(e.description))
    return jsonify(error="ratelimit exceeded", message=str(e.description)), 429


if __name__ == "__main__":
    app.run(debug=True)

