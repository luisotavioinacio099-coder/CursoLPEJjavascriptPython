from flask import request, jsonify, Blueprint

laco_repeticao_bp = Blueprint("laco_repeticao", __name__)

# Laco de Repetição WHILE.
@laco_repeticao_bp.post("/calcular_media_anual")
def calcular_media_anual():
    try:
        dados = request.get_json()

        salarios_anuais = dados.get("salarios_anuais")

        soma_salarios = 0
        i = 0

        while i < len(salarios_anuais):
            soma_salarios += salarios_anuais[i]
            i += 1

        media = soma_salarios / 12

        return jsonify({
            "status": "sucesso",
            "media_salarial_anual": f"{media:.2f}"
        })
    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": f"Ocorreu um ERRO: {str(e)}"
        }), 500