# source venv/bin/activate
# python3 -m pip freeze > requirements.txt

from flask import Flask, request, render_template
from json2html import *
from decoder import decode

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        qr = request.form['qr']
        json = decode(qr)
        table = json2html.convert(json=json, table_attributes='class="table table-striped"')
        return render_template('json.html', table=table)
    else:
        return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
