from flask import Flask
app = Flask(__name__, static_folder='./templates/images')
import flasker.main

from flasker import db
db.create_table()

if __name__ == '__main__':
    app.run(debug=True, host='192.168.2.27', port=5000)