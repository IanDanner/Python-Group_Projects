from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'win' not in session:
        session['win'] = 0
        session['loss'] = 0
        session['ties'] = 0 
    if 'action' in session:
        move = random.randint(0,2)
        print "random " + str(move)
        print "session " + str(session['action'])
        print "type "+str(type(session['action']))
        if move == 0:
            hand = "rock"
        elif move == 1:
            hand = "paper"
        elif move == 2:
            hand = "scissors"
        if session['action'] == move:
            session['ties'] += 1
        elif session['action'] == 0:
            if move == 1:
                session['loss'] += 1
            elif move == 2:
                session['win'] += 1
        elif session['action'] == 1:
            if move == 0:
                session['win'] += 1
            elif move == 2:
                session['loss'] += 1
        elif session['action'] == 2:
            if move == 0:
                session['loss'] += 1
            elif move == 1:
                session['win'] += 1
        elif session['action'] == 3:
            session['win'] = 0
            session['loss'] = 0
            session['ties'] = 0 
    print session['win'], session['loss'], session['ties']
    return render_template("rock-paper-scissors.html", move = hand)

@app.route('/action', methods=['POST'])
def action():
    session['action'] = int(request.form['val'])
    print request.form['val']
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['action'] = 3
    return redirect('/')

app.run(debug=True)