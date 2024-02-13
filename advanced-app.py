from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

@app.route('/profile')
def profile():
    random_number = random.randint(1, 1000)
    return render_template('advanced-profile.html', view=random_number)

@app.route('/')
def index():
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)