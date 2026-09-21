from flask import request, jsonify, Blueprint

condicionais_calculos_bp = Blueprint("condicionais_calculadora", __name__)

@condicionais_calculos_bp.post("/resposta-calculadora")
def calcular():

    try:
        dados = request.get_json()

        # Declarando as Variáveis.
        numero_1 = float(dados.get("n1"))
        numero_2 = float(dados.get("n2"))
        operador = dados.get("op")

        # Condições Lógicas em Python!
        if operador == "+":
            res = numero_1 + numero_2

        elif operador == "-":
            res = numero_1 - numero_2

        elif operador == "x" or operador == "X":
            res = numero_1 * numero_2

        elif operador == "/":
            if numero_2 == 0:
                return jsonify({
                    "Resultado": "O SEGUNDO VALOR NÃO PODERÁ SER ZERO 0!"
                }), 400

            res = numero_1 / numero_2

        else:
            res = "Operador INEXISTENTE!"

        return jsonify({"Resultado": res})

    except ValueError:
        return jsonify({
            "Resultado": "Revise as informações - deverão ser NUMÉRICOS!"
        }), 400

    except Exception as e:
        return jsonify({
            "Resultado": f"Ocorreu um erro GERAL: {str(e)}"
        }), 500