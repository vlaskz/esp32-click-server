from flask import Flask, request


app = Flask(__name__,
    static_url_path='',
    static_folder='web/static',
    template_folder='web/template')
    

@app.route('/', methods=['GET', 'POST'])
def clicked():
if request.method == 'POST':
        name = request.values.get('name')
        message = request.values.get('message')
        print('name:', name, ' message:', message)
if method =='GET':
else:
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(threaded=True)
