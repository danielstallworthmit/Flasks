from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Worlds!!!"

@app.route('/name')
def welcome():
    return "Welcome to our application!"

if __name__ == "__main__":
    app.run(port=3000,debug=True)