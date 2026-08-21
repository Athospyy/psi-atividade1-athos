from flask import Flask, render_template
import models

app = Flask(__name__)
app.secret_key = 'qualquercoisa123'  # Tarefa 1: chave secreta

# Tarefa 2 - Só a listagem de livros por enquanto
@app.route('/')
def index():
    livros = models.buscar_livros()  # pega todos do models.py
    return render_template('index.html', livros=livros)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/livro/<int:livro_id>')
def detalhe_livro(livro_id):
    livro = models.buscar_livro(livro_id)  # usa a função do models
    
    if livro is None:
        return "Livro não encontrado", 404
    
    return f"Livro: {livro['titulo']} - Autor: {livro['autor']}"