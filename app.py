from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buildpagesvart')
def buildpagesvart():
    return render_template('buildpagesvart.html')

@app.route('/buildpagevit')
def buildpagevit():
    return render_template('buildpagevit.html')

@app.route('/buildpagebla')
def buildpagebla():
    return render_template('buildpagebla.html')

if  __name__ == '__main__':
    app.run(debug=True)