from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def lifeline():
    return render_template('lifeline.html' )

@app.route("/gas")
    name = 'Gas'
def gas():
    return render_template('category.html')

@app.route("/denki")
    name = 'Denki'
def denki():
    return render_template('category.html')

@app.route("/suidou")
    name = 'Suidou'
def suidou():
    return render_template('category.html')



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=6000)