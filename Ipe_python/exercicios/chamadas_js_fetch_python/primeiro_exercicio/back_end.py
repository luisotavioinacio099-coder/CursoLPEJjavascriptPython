from flask import request, jsonify, Blueprint

operadores_bp = Blueprint("operadores", __name__)

@operadores_bp.post("/calculo_media_ponderada")
def calcular_media_ponderada():
    try:
        dados = request.get_json()

        nota1 = float(dados.get("nota1"))
        nota2 = float(dados.get("nota2"))
        nota3 = float(dados.get("nota3"))

        peso1 = float(dados.get("peso1"))
        peso2 = float(dados.get("peso2"))
        peso3 = float(dados.get("peso3"))

        media = (
            (nota1 * peso1) +
            (nota2 * peso2) +
            (nota3 * peso3)
        ) / (peso1 + peso2 + peso3)

        return jsonify({
            "status": "sucesso",
            "media_ponderada": round(media, 2)
        }), 200
    except ValueError:
        return jsonify({
            "status": "erro",
            "mensagem": "As notas e os pesos devem ser numéricos!"
        }), 400
    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": f"Ocorreu um erro: {str(e)}"
        }), 500