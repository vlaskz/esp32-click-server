from flask import Flask, request
import json
import time
from datetime import datetime


app = Flask(__name__,
    static_url_path='',
    static_folder='web/static',
    template_folder='web/template')


def apnd_to_json(name, message):
    with open('web/static/messages.json', 'r+') as file:
        data = json.load(file)
        text = name + ' diz: ' + message
        data.update({datetime.now().strftime('%d/%m/%Y %H:%M:%S'): text})
        file.seek(0)
        json.dump(data, file)
        print(data)

@app.route('/', methods=['GET', 'POST'])
def clicked():
    if request.method == 'POST':
        name = request.values.get('name')
        message = request.values.get('message')
        apnd_to_json(name, message)
        time.sleep(1)
        return app.send_static_file('index.html')
    else:
        return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(threaded=True)
