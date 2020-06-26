from flask import Flask, request


app = Flask(__name__,
    static_url_path='',
    static_folder='web/static',
    template_folder='web/template')


def append(name, message):
    data_to_append = {name: message}
    with open('messages.json', 'r+') as file:
        data = json.load(file)
        data.update(data_to_append)
        file.seek(0)
        json.dump(data, file)

@app.route('/', methods=['GET', 'POST'])
def clicked():
    if request.method == 'POST':
        name = request.values.get('name')
        message = request.values.get('message')
        append(name, message)
        return app.send_static_file('index.html')
    else:
        return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(threaded=True)
