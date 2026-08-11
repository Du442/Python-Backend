from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Heallo world!'

app.run(debug=True)