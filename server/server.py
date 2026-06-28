from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    img_data = request.data
    filename = f"images/pothole_{int(time.time())}.jpg"
    with open(filename, "wb") as f:
        f.write(img_data)
    print(f"Saved {filename}")
    return "Image received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
