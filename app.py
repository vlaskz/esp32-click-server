from flask import Flask, request


app = Flask(__name__)



@app.route('/')
def index():
    return 'Welcome to @vlaskzBot server. Proudly hosted in Heroku.'


if __name__ == '__main__':
    app.run(threaded=True)