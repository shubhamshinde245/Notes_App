from flask import Flask

# Create the application instance
app = Flask(__name__)

# decorator is used to tell Flask what URL should trigger our function
@app.route('/')
def hello_world():
    return 'Hi Adiyat!'

# Create a URL route in our application for "/name"
@app.route("/name")
def name():
    return "Name: John Doe"

if __name__ == '__main__':
    app.run(debug=True)