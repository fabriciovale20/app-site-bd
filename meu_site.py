from flask import Flask, render_template, request
import mysql.connector
import config_key as key

app = Flask(__name__) # Inicialização da Aplicação WEB

conexao = mysql.connector.connect(
    host = key.MYSQLHOST,
    port = key.MYSQLPORT,
    user = key.MYSQLUSER,
    password = key.MYSQLPASSWORD,
    db = key.MYSQLDATABASE,
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

    comando = f'SELECT * FROM mensagens'
    cursor.execute(comando)
    lista_mensagens = cursor.fetchall()
    print(lista_mensagens)

    return render_template('home.html', lista_mensagens=lista_mensagens)

if __name__ == '__main__':
    app.run(debug=True)