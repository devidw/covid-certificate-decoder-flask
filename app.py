from flask import Flask, request, render_template
from decoder.decoder import decode

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        qr = request.form['qr']
        json = decode(qr)
        return render_template('json.html', cert=json)
    else:
        return render_template('form.html')


if __name__ == '__main__':
    app.run()
