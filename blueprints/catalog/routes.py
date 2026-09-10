from flask import render_template, request
import models
from . import catalog_bp


@catalog_bp.route('/')
def index():
    termo = request.args.get('q', '').strip()

    if termo:
        livros = models.buscar_livros(termo)
    else:
        livros = models.buscar_livros()

    return render_template('catalog/index.html', livros=livros, termo=termo)


@catalog_bp.route('/livro/<int:livro_id>')
def ver_livro(livro_id):
    livro = models.buscar_livro(livro_id)

    if livro is None:
        return 'Livro não encontrado', 404

    resenhas = models.resenhas_do_livro(livro_id)
    return render_template('catalog/livro.html', livro=livro, resenhas=resenhas)
