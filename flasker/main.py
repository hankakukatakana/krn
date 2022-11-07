from flasker import app
from flask import render_template, request, redirect, url_for
from datetime import datetime
import sqlite3

dbname = 'lifeline.db'

@app.route("/")
def home():
    today = datetime.today()
    mm = today.month
    con = sqlite3.connect(dbname)
    db_lifeline = con.execute('SELECT * FROM lifeline').fetchall()
    con.close()

    lifelines = []
    for row in db_lifeline:
        lifelines.append({'mm':row[0], 'category':row[1], 'prise':row[2]})

    return render_template('home.html', lifelines=lifelines, mm=mm)

@app.route('/gas')
def gas():
    name = 'Gas'
    con = sqlite3.connect(dbname)
    db_element = con.execute("SELECT * FROM lifeline WHERE category = 'ガス'").fetchall()
    con.close()

    elements = []
    for row in db_element:
        elements.append({'mm':row[0], 'category':row[1], 'prise':row[2]})
    
    return render_template('category.html', name=name)

@app.route('/denki')
def denki():
    name = 'Denki'
    return render_template('category.html', name=name)

@app.route('/suidou')
def suidou():
    name = 'Suidou'
    return render_template('category.html', name=name)

@app.route('/form')
def form():
    name = 'form'
    return render_template('form.html', name=name)

@app.route('/register', methods=['POST'])
def register():
    mm = request.form['mm']
    category = request.form['category']
    price = request.form['price']

    con = sqlite3.connect(dbname)
    con.execute('INSERT INTO lifeline VALUES(?, ?, ?)',
                [mm, category, price])
    con.commit()
    con.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)