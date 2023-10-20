from flask import Flask, render_template, request
import db

app = Flask(__name__)

# Tampilan awal
@app.route('/', methods=['GET'])
def awal():
    return render_template('register.html')

# Register
@app.route('/register', methods=['POST'])
def register():
    username = request.form['nama']
    email = request.form['email']
    password = request.form['password']

    db.inputUser(username,email,password)

    return render_template('berhasil.html')

if __name__ == '__main__':
    app.run(debug=True)