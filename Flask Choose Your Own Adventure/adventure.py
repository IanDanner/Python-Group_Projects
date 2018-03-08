from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def startSpace():
    return render_template('startSpace.html')

@app.route('/left')

def enterShip():
    return render_template('enterShip.html')

@app.route('/death')

def death():
    return render_template('death.html')

@app.route('/left/right')

def enterBridge():
    return render_template('enterBridge.html')

@app.route('/escape')

def escape():
    return render_template('escape.html')


app.run(debug=True)