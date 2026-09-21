from flask import request, jsonify, Blueprint

colecoes_ganhos_bp = Blueprint("colecoes_ganhos", __name__)

# Tupla para classificação dos ganhos.
classificacao_ganhos = (
    "Aumento Ruim",
    "Aumento Bom",
    "Aumento Excelente"
)

@colecoes_ganhos_bp.post("/analisar_ganhos")
def analisar_ganhos():
    try:
        # Pegar as informações no formato JSON.
        dados = request.get_json()

        # Pegando o nome do cliente.
        nome_cliente = dados.get("nome_cliente").strip()

        # Pegando a lista de ganhos dos últimos 3 meses.
        ganhos_mensais = dados.get("ganhos_ultimos_3_meses")

        # Validando o nome do cliente.
        if nome_cliente == "":
            return jsonify({
                "Resultado": "É necessário informar o NOME DO CLIENTE!"
            }), 400

        # Validando se os ganhos estão em uma lista.
        if not isinstance(ganhos_mensais, list):
            return jsonify({
                "Resultado": "Os GANHOS devem estar em uma LISTA!"
            }), 400

        # Validando se a lista possui valores.
        if not ganhos_mensais:
            return jsonify({
                "Resultado": "A lista de GANHOS não pode estar vazia!"
            }), 400

        # Variável para armazenar a soma dos ganhos.
        soma_ganhos = 0

        # Percorrendo a lista de ganhos.
        for ganho in ganhos_mensais:
            soma_ganhos += ganho

        # Calculando a média dos ganhos.
        media_ganhos = soma_ganhos / len(ganhos_mensais)

        # Classificando os ganhos através de condições.
        if media_ganhos < 1000:
            classificacao = classificacao_ganhos[0]
        elif media_ganhos <= 5000:
            classificacao = classificacao_ganhos[1]
        else:
            classificacao = classificacao_ganhos[2]

        # Retorno final em formato de DICIONARIO.
        resposta = {
            "nome_cliente": nome_cliente,
            "media_ganhos": media_ganhos,
            "classificacao": classificacao
        }

        return jsonify(resposta), 200
    except Exception as e:
        return jsonify({
            "Resultado": f"Ocorreu um ERRO: {str(e)}"
        }), 500