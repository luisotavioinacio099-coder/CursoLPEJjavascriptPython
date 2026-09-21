from flask import request, jsonify, Blueprint

laco_repeticao_bp = Blueprint("laco_repeticao", __name__)

# Laco de Repetição FOR.
@laco_repeticao_bp.post("/calculo_semestre")
def calcular_semestre():
    try:
        dados = request.get_json()

        ganhos_semestre = dados.get("ganhos_semestre")

        total = 0

        for valor in ganhos_semestre:
            total += valor

        return jsonify({
            "status": "sucesso",
            "total_ganho_semestral": f"{total:.2f}"
        })
    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": f"Ocorreu um ERRO: {str(e)}"
        }), 500