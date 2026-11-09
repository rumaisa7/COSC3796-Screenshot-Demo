
from flask import Flask, request, render_template_string
from pathlib import Path

app = Flask(__name__)

UPLOAD_DIR = Path(__file__).parent / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

HTML = """
<h1>COSC 3796 - Screenshot Demo</h1>
<p>Local practice server</p>

<form action="/upload" method="post"
      enctype="multipart/form-data">
    <input type="file" name="image"
           accept="image/png">
    <button type="submit">Upload Test Image</button>
</form>

<h2>Latest Test Image</h2>
<h2>Latest Test Image</h2>
<img id="latest" src="/latest" width="600">

<script>
setInterval(() => {
    document.getElementById("latest").src =
        "/latest?t=" + Date.now();
}, 30000);
</script>
"""

@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/upload", methods=["POST"])
def upload():
    image = request.files.get("image")

    if not image or not image.filename.lower().endswith(".png"):
        return "Please upload a PNG test image.", 400

    image.save(UPLOAD_DIR / "test.png")
    return "Test image received successfully!"


@app.route("/latest")
def latest():
    from flask import send_file

    path = UPLOAD_DIR / "test.png"

    if not path.exists():
        return "No image uploaded yet.", 404

    return send_file(path, mimetype="image/png")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
