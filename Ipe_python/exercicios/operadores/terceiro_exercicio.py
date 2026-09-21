from flask import request, jsonify, Blueprint

operadores_calculos_bp = Blueprint("operadores_calculadora", __name__)

# Função responsável pelo cálculo dos Juros Simples!
def calcular_juros_simples(capital, taxa, tempo):
    juros = capital * taxa * tempo
    return juros

# Endpoint - Calcular Juros Simples!
@operadores_calculos_bp.post("/calcular_juros_simples")
def calcular():
    try:
        # Pegar os dados no formato JSON.
        dados = request.get_json()

        # Declarando as Variáveis.
        capital = float(dados.get("capital"))
        taxa = float(dados.get("taxa"))
        tempo = float(dados.get("tempo"))

        # Chamando a função para realizar o cálculo.
        resultado = calcular_juros_simples(
            capital,
            taxa,
            tempo
        )
        return jsonify({
            "Juros Simples": resultado
        })
    except ValueError:
        return jsonify({
            "Resultado": "Revise as Informações - Deverão ser NUMÉRICOS!"
        }), 400
    except Exception as e:
        return jsonify({
            "Resultado": f"Ocorreu um erro GERAL: {str(e)}"
        }), 500