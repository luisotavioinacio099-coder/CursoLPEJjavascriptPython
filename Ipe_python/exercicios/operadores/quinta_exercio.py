from flask import request, jsonify, Blueprint

operadores_calculos_bp = Blueprint("operadores_calculadora", __name__)

# Função responsável por dividir o valor da conta entre as pessoas!
def dividir_conta(valor_total, numero_de_pessoas):
    resultado = valor_total / numero_de_pessoas
    return resultado

# Endpoint - Dividir Conta!
@operadores_calculos_bp.post("/dividir_conta")
def dividir():
    try:
        # Pegar os dados no formato JSON.
        dados = request.get_json()

        # Declarando as Variáveis.
        valor_total = float(dados.get("valor_total"))
        numero_de_pessoas = int(dados.get("numero_de_pessoas"))

        # Verificando se o número de pessoas é maior que zero.
        if numero_de_pessoas <= 0:
            return jsonify({
                "Resultado": "O número de pessoas deverá ser maior que zero!"
            }), 400

        # Chamando a função para realizar o cálculo.
        resultado = dividir_conta(
            valor_total,
            numero_de_pessoas
        )
        return jsonify({
            "Valor por Pessoa": resultado
        })
    except ValueError:
        return jsonify({
            "Resultado": "Revise as Informações - Deverão ser NUMÉRICOS!"
        }), 400
    except Exception as e:
        return jsonify({
            "Resultado": f"Ocorreu um erro GERAL: {str(e)}"
        }), 500