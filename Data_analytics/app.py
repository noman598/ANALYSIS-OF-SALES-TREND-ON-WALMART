
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/tableau_dashboard')
def tableau_dashboard():
    return render_template('index.html')

@app.route('/tableau_story')
def tableau_story():
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)