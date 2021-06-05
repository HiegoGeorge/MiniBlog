from flask import Flask
from flask import request
from flask import render_template

import sqlite3
from sqlite3 import Error

app = Flask(__name__)

# 1. Cadastrar Posts
@app.route('/novopost', methods=['GET','POST'])

def cadastrar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        mensagem = 'Erro - nao cadastrado'
        if titulo and descricao:
            registro = (titulo, descricao)
            try:
                conn = sqlite3.connect('database/db-blog.db')

                sql = ''' INSERT INTO posts (titulo, descricao)
                              VALUES(?,?) '''

                cur = conn.cursor()

                cur.execute(sql, [descricao])

                conn.commit()

                mensagem = 'Cadastrado com sucesso'

            except Error as e:
                print(e)
            finally:
                conn.close()
    return render_template('cadastrar.html')

# Listar topicos
@app.route('/posts/listar', methods=['GET'])
def listar():
    try:
        conn = sqlite3.connect('database/db-blog.db')
        sql = '''SELECT * FROM posts'''
        cur = conn.cursor()
        cur.execute(sql)
        registros = cur.fetchall()
        return render_template('listar.html', regs=registros)
    except Error as e:
        print(e)
    finally:
        conn.close()


# Rota de Erro
@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404

#######################################################
# Execucao da Aplicacao
if __name__ == '__main__':
    app.run()