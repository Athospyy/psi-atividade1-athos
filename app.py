from flask import Flask, render_template, request, redirect, url_for, session
import models


app = Flask(__name__)
app.secret_key = 'qualquercoisa123'
@app.route('/')
def index():
    if 'q' in request.args and request.args['q'].strip() != '':
        termo = request.args['q'].strip()
        lista_livros = models.buscar_livros(termo)
    else:
        termo = None
        lista_livros = models.buscar_livros()

    return render_template('index.html', livros=lista_livros, termo=termo)


@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        nome_usuario = request.form.get('nome', '').strip()
        senha_usuario = request.form.get('senha', '')

        indice_encontrado = -1
        for i in range(len(models.usuarios)):
            u = models.usuarios[i]
            if u.get('nome') == nome_usuario and u.get('senha') == senha_usuario:
                indice_encontrado = i
                break

        if indice_encontrado >= 0:
            session['usuario'] = models.usuarios[indice_encontrado].get('nome')
            return redirect(url_for('index'))

        erro = 'Usuário ou senha incorretos. Tente novamente.'

    return render_template('login.html', erro=erro)


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))


@app.route('/livro/<int:livro_id>')
def detalhe_livro(livro_id):
    livro = models.buscar_livro(livro_id)

    if livro is None:
        return "Livro não encontrado", 404

    resenhas = models.resenhas_do_livro(livro_id)
    return render_template('livro.html', livro=livro, resenhas=resenhas)


if __name__ == '__main__':
    app.run(debug=True)