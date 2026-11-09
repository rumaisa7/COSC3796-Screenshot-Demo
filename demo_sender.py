
import time
import urllib.request
from pathlib import Path

# Use only the test image you selected
IMAGE = Path(__file__).parent / "uploads" / "test.png"
SERVER = "http://127.0.0.1:5000/upload"

print("COSC 3796 - Automatic Test Image Demo")
print("Press Ctrl+C to stop.")

while True:
    if not IMAGE.exists():
        print("Test image not found.")
        break

    boundary = "MarioDemoBoundary"
    image_bytes = IMAGE.read_bytes()

    body = (
        f"--{boundary}\r\n"
        'Content-Disposition: form-data; name="image"; filename="test.png"\r\n'
        "Content-Type: image/png\r\n\r\n"
    ).encode() + image_bytes + (
        f"\r\n--{boundary}--\r\n"
    ).encode()

    request = urllib.request.Request(
        SERVER,
        data=body,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            print("Test image sent:", response.status)
    except Exception as error:
        print("Upload failed:", error)

    time.sleep(30)
