from flask import request, jsonify, Blueprint

operadores_calculos_bp = Blueprint("operadores_calculadora", __name__)

# Função responsável pelo cálculo do ponto de reposição do estoque!
def calcular_estoque(quantidade_minima, quantidade_maxima):
    resultado = (quantidade_minima + quantidade_maxima) / 2
    return resultado

# Endpoint - Calcular Estoque!
@operadores_calculos_bp.post("/calculo_estoque")
def calcular():
    try:
        # Pegar os dados no formato JSON.
        dados = request.get_json()

        # Declarando as Variáveis.
        quantidade_minima = float(dados.get("quantidade_minima"))
        quantidade_maxima = float(dados.get("quantidade_maxima"))

        # Chamando a função para realizar o cálculo.
        resultado = calcular_estoque(
            quantidade_minima,
            quantidade_maxima
        )
        return jsonify({
            "Quantidade Média": resultado
        })
    except ValueError:
        return jsonify({
            "Resultado": "Revise as Informações - Deverão ser NUMÉRICOS!"
        }), 400
    except Exception as e:
        return jsonify({
            "Resultado": f"Ocorreu um erro GERAL: {str(e)}"
        }), 500