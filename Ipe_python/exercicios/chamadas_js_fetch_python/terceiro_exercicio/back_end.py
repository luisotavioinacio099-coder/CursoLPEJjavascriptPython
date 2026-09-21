from flask import request, jsonify, Blueprint

juros_simples_bp = Blueprint("juros_simples", __name__)


@juros_simples_bp.post("/calcular_juros_simples")
def calcular_juros_simples():
    try:
        # Pegando os dados enviados pelo JavaScript.
        dados = request.get_json()

        # Declarando as Variáveis.
        capital = float(dados.get("capital"))
        taxa = float(dados.get("taxa"))
        tempo = float(dados.get("tempo"))

        # Calculando os Juros Simples.
        juros = capital * taxa * tempo

        # Retornando o resultado para o JavaScript.
        return jsonify({
            "status": "sucesso",
            "juros": round(juros, 2)
        }), 200
    except ValueError:
        return jsonify({
            "status": "erro",
            "mensagem": "Capital, taxa e tempo devem ser NUMÉRICOS!"
        }), 400
    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": f"Ocorreu um ERRO: {str(e)}"
        }), 500