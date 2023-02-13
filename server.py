from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "I wish I were an Oscar Meyer wiener"

guess_left =10

def guessCounter():
    if 'visited' in session:
        session['visited'] += 1
        guess_left-=1
    else:
        session['visited'] = 0
    return

# def randomNumber():
#     randomNum= random.randint(0,100)
#     return randomNum
randomNum= random.randint(0,100)

@app.route('/')
def index():
    # randomNumber()
    
    print(randomNum)
    # print(randomNumber())
    print(session['visited'])
    return render_template("index.html")

@app.route('/check', methods = ['POST'])
def count():
    guess=request.form['guess']
    if (guess == randomNum) and (guess_left>0): 
        print(f"{{input}} was the number! Congrats!")
    elif (guess > randomNum) and (guess_left>0):
        print(f"Too high!!!")
    elif (guess < randomNum) and (guess_left>0):
        print(f"Too low!")
    elif guess_left <= 0:
        print(f"You have run out of guesses nd lost!")
    print("Person has been here!")
    guessCounter()
    return redirect('/')


@app.route('/replay')
def restart():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
