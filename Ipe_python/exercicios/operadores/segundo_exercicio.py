from flask import request, jsonify, Blueprint

operadores_calculos_bp = Blueprint("operadores_calculadora", __name__)

# Função responsável pela conversão de Celsius para Fahrenheit!
def converter_temperatura(celsius):
    resultado = (celsius * 9 / 5) + 32
    return resultado

# Endpoint - Converter Temperatura!
@operadores_calculos_bp.post("/converter_temperatura")
def converter():
    try:
        # Pegar os dados no formato JSON.
        dados = request.get_json()

        # Declarando a Variável.
        celsius = float(dados.get("celsius"))

        # Chamando a função para realizar a conversão.
        resultado = converter_temperatura(celsius)

        return jsonify({
            "Fahrenheit": resultado
        })
    except ValueError:
        return jsonify({
            "Resultado": "Revise as Informações - Deverá ser NUMÉRICO!"
        }), 400
    except Exception as e:
        return jsonify({
            "Resultado": f"Ocorreu um erro GERAL: {str(e)}"
        }), 500