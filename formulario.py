from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de produtos (inicialmente vazia)
produtos = []


# Rota para a página inicial (listagem de produtos)
@app.route('/')
def index():
    # Ordena os produtos pelo valor, do menor para o maior
    produtos_ordenados = sorted(produtos, key=lambda x: x['valor'])
    return render_template('index.html', produtos=produtos_ordenados)


# Rota para o formulário de cadastro de produto
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        # Obtém os dados do formulário
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor = float(request.form['valor'])
        disponivel = True if request.form['disponivel'] == 'sim' else False

        # Adiciona o produto à lista de produtos
        produtos.append({'nome': nome, 'descricao': descricao, 'valor': valor, 'disponivel': disponivel})

        # Redireciona para a página inicial (listagem de produtos)
        return redirect(url_for('index'))

    # Se o método for GET, exibe o formulário de cadastro
    return render_template('cadastrar.html')


if __name__ == '__main__':
    app.run(debug=True)
