# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)

camisetas = [{'tipo': 'pequena', 'preco': 10.00},
{'tipo': 'media', 'preco': 12.00},
{'tipo': 'grande', 'preco': 15.00}]

# http://127.0.0.1:5000/produtos
@app.route('/produtos', methods=['GET'])
def retornar_todos_os_produtos():
    resp = camisetas

    if 'X-nome-produto' in request.headers:
        tipo = request.headers['X-nome-produto']
        for produto in camisetas:
            if produto['tipo'] == tipo:
                resp = produto
    return jsonify(resp)
# http://127.0.0.1:5000/produtos/quantidades
@app.route('/produtos/quantidades', methods=['GET'])
def retornar_total_dos_produtos():

    if 'X-qtdp' in request.headers:
        qtdp = int(request.headers['X-qtdp'])
    if 'X-qtdm' in request.headers:
        qtdm = int(request.headers['X-qtdm'])
    if 'X-qtdg' in request.headers:
        qtdg = int(request.headers['X-qtdg'])
    total = qtdp * 10 + qtdm * 12 + qtdg * 15
    return jsonify({"Total": total})

if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)
