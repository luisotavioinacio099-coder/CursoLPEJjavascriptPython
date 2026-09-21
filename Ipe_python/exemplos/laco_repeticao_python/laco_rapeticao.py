from flask import request, jsonify, Blueprint

laco_tepeticao_bp = Blueprint("laco_repeticao", __name__)

# f"{total:.2f}" - Tratamento para casas Decimais.

# Laço de Repetição FOR.
@laco_tepeticao_bp.post("/somar_for")
def somar_com_for():
    try:
        dados = request.get_json()
        precos_itens = dados.get("precos_itens")

        total = 0

        for valor in precos_itens:
            # total = total + valor
            total += valor

        return jsonify({"Total dos Valores com FOR: ": f"{total:.2f}"})

    except Exception as e:
        return jsonify({"Resultado: ": f"Ocorreu um ERRO: {str(e)}"}), 500

# laço de Repetição WHILE
@laco_tepeticao_bp.post("/somar_while")
def somar_com_while():
    try:
        dados = request.get_json()
        dados_itens = dados.get("dados_itens")

        i = 0
        total = 0

        while i < len(dados_itens):
            total += dados_itens[i]
            i += 1

            return jsonify({"Total dos Valores com While: ": f"{total:.2f}"})

    except Exception as e:
        return jsonify({"Resultado: ": f"Ocorreu um ERRO: {str(e)}"}), 500