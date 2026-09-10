from flask import redirect, render_template, request, session, url_for
import models
from . import auth_bp


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    erro = None

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        senha = request.form.get('senha', '')

        for usuario in models.usuarios:
            if usuario['nome'] == nome and usuario['senha'] == senha:
                session['usuario'] = usuario['nome']
                return redirect(url_for('catalog.index'))

        erro = 'Usuário ou senha incorretos. Tente novamente.'

    return render_template('auth/login.html', erro=erro)


@auth_bp.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('catalog.index'))
