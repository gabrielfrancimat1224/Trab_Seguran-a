import sqlite3
from flask import Flask, render_template, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


def RegisterApp(login, senha):
    banco = sqlite3.connect('unifor.db')
    cursor = banco.cursor()
    #Tipo de criptografia usada sha256
    safePass = generate_password_hash(senha, 'sha256') 
    cursor.execute(f"INSERT INTO users(username, password) VALUES ('{login}', '{safePass}')")
    banco.commit()
    banco.close()
    print(f'User: {login} | Password: {senha}')


def loginApp(login, senha):
    banco = sqlite3.connect('unifor.db')
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{login}'")
    result = cursor.fetchall()
    if result != []: 
        print('User Existe!')
        PassHash = result[0][1]

        if check_password_hash(str(PassHash), str(senha)) == True:
            print('Senha Correta!')
            return 0
        else:
            print('Senha Incorreta!')
            return 1
    else:
        print('User Não Existe!')
        return 1 


@app.route('/')
def welcome():
    return redirect('/register')


@app.route('/register', methods=['GET', 'POST'])
def register():
    global username

    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            RegisterApp(username, password)
            return redirect('/login')
        except Exception as e:
            print(e)
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    global username

    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            if loginApp(username, password) == 0:
                return 'Logado com sucesso!'
            else:
                return render_template('login.html')
        except Exception as e:
            print(e)
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)