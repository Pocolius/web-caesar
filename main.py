from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method="post">
            <label for="rot">
            Rotate By:
            <input id="rot" name="rot" type="text" value="0" />
            </label>
            <textarea name="text"></textarea>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypted():
    rot = int(request.form['rot'])
    text = str(request.form['text'])
    encryption = encrypt(text, rot)
    return '<h1>' + encryption + '</h1>'


app.run()