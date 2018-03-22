from flask import Flask

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
        <form method="POST">
        <label for="rot-id">Rotate By:</label>
        <input id="rot-id" name="rot" type="text" />
        <textarea name="text" />
        <input type="submit" />
        </form>
    </body>
</html>"""

@app.route("/"), methods=['POST']
def index():
    rot_by = request.form['rot']
    return rot_by

app.run()