from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buildpage')
def buildpage():
    return render_template('buildpage.html')

if  __name__ == '__main__':
    app.run(debug=True)