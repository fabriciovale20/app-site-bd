from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__) # Inicialização da Aplicação WEB
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='passwordsql',
    database='app_bd_teste'
)

cursor = conexao.cursor()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        msg = request.form.get('msg')
        print(msg)

        # Adicionando as variáveis a Classe Aluno
        comando = f'''INSERT INTO mensagens (mensagem) VALUES ("{msg}");'''
        cursor.execute(comando)
        conexao.commit()

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)