from flask import Flask, render_template
from data import data

app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html', data=data)

@app.route('/paslaugos')
def paslaugos():
    return render_template('paslaugos.html')

@app.route('/albumas')
def albumas():
    return render_template('albumas.html')

@app.route('/apie')
def apie():
    return render_template('apie.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)

