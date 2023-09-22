import os

from flask import Flask, request, send_file
from scipy.io.wavfile import write, read

from tts import synthesize
from se import denoise

app = Flask(__name__)

cache_dir = "app/backend/cache"

@app.route("/")
def index():
    return "<p>Welcome to lemon5!</p>"

@app.route("/tts", methods=["POST", "GET"])
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

if __name__ == "__main__":
    app.run()