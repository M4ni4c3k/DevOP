from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
	return '<p>Hello, %s!'% World!
@app.route('/')

def hello_world():
	return 'Hello World'

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True)
