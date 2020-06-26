from flask import Flask, request
import json


app = Flask(__name__,
    static_url_path='',
    static_folder='web/static',
    template_folder='web/template')


def apnd_to_json(name, message):
    print('initializing function')
    with open('web/static/messages.json', 'r+') as file:
        data = json.load(file)
        data.update({name: message})
        file.seek(0)
        json.dump(data, file)
        print(data)

@app.route('/', methods=['GET', 'POST'])
def clicked():
    if request.method == 'POST':
        name = request.values.get('name')
        message = request.values.get('message')
        apnd_to_json(name, message)
        return app.send_static_file('index.html')
    else:
        return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(threaded=True)
