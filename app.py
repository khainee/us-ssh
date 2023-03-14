from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'GreyMatters'

@app.route('/gdrive-auth')
def hello_world():
    return 'GreyMatter'


if __name__ == "__main__":
    app.run()
