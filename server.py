from flask import *
from facedetect import excute

app = Flask(__name__)

@app.route('/swap', methods=['post'])
def swap_page():
    img = request.files.get('file')
    sex = request.form.get('sex')
    major = request.form.get('major')

    f = excute(img, sex, major)

    resp = make_response(f.getvalue())
    resp.headers["Content-Type"] = "image/jpeg"
    return resp

@app.route('/notice')
def notice():
    return render_template('notice.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
