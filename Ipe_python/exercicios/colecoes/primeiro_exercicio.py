from flask import request, jsonify, Blueprint

colecoes_bp = Blueprint("colecoes", __name__)

# Objeto de Dados - Dicionário!
estoque = {
    "mouse": 5,
    "teclado": 34,
    "monitor": 21
}

# Endpoint - Verificar Estoque!
@colecoes_bp.post("/verificar_estoque")
def verificar_estoque():
    try:
        # Pegar as informações no formato JSON.
        dados = request.get_json()

        # Pegando o nome do produto e a quantidade desejada.
        produto = dados.get("produto").strip()
        quantidade = dados.get("quantidade")

        # Verificando se o nome do produto foi informado.
        if produto == "":
            return jsonify({
                "Resultado": "É necessário informar o PRODUTO!"
            }), 400
        # Verificando se a quantidade é válida.
        if not isinstance(quantidade, int) or quantidade <= 0:
            return jsonify({
                "Resultado": "A QUANTIDADE deve ser um número inteiro maior que zero!"
            }), 400
        # Verificando se o produto existe no estoque.
        if produto not in estoque:
            return jsonify({
                "produto": produto,
                "tem_estoque": False,
                "quantidade_atual": 0
            }), 200

        # Pegando a quantidade atual do produto.
        quantidade_atual = estoque[produto]

        # Verificando se existe quantidade suficiente.
        tem_estoque = quantidade <= quantidade_atual

        # Montando a resposta.
        resposta = {
            "produto": produto,
            "tem_estoque": tem_estoque,
            "quantidade_atual": quantidade_atual
        }
        return jsonify(resposta), 200
    except Exception as e:
        return jsonify({
            "Resultado": f"Ocorreu um ERRO: {str(e)}"
        }), 500