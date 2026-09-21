from flask import request, jsonify, Blueprint

conversor_temperatura_bp = Blueprint("conversor_temperatura", __name__)

@conversor_temperatura_bp.post("/converter_temperatura")
def converter_temperatura():
    try:
        # Pegando os dados enviados pelo JavaScript.
        dados = request.get_json()

        # Pegando a temperatura em Celsius.
        celsius = float(dados.get("celsius"))

        # Fazendo a conversão.
        fahrenheit = (celsius * 9 / 5) + 32

        # Retornando o resultado.
        return jsonify({
            "status": "sucesso",
            "celsius": celsius,
            "fahrenheit": round(fahrenheit, 2)
        }), 200
    except ValueError:
        return jsonify({
            "status": "erro",
            "mensagem": "A temperatura deve ser um valor numérico!"
        }), 400
    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": f"Ocorreu um erro: {str(e)}"
        }), 500