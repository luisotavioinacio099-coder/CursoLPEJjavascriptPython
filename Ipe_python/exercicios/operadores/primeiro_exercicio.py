from flask import request, jsonify, Blueprint

operadores_calculos_bp = Blueprint("operadores_calculos", __name__)

# Função responsável pelo cálculo da Média Ponderada!
def calcular_media_ponderada(nota1, nota2, nota3, peso1, peso2, peso3):
    resultado = (
        (nota1 * peso1) +
        (nota2 * peso2) +
        (nota3 * peso3)
    ) / (peso1 + peso2 + peso3)
    return resultado

# Endpoint - Calcular Média Ponderada!
@operadores_calculos_bp.post("/calculo_media_ponderada")
def media_ponderada():
    try:
        # Pegar os dados no formato JSON.
        dados = request.get_json()
        # Declarando as Variáveis.
        nota1 = float(dados.get("nota1"))
        nota2 = float(dados.get("nota2"))
        nota3 = float(dados.get("nota3"))
        peso1 = float(dados.get("peso1"))
        peso2 = float(dados.get("peso2"))
        peso3 = float(dados.get("peso3"))
        
        # Verificando se a soma dos pesos é diferente de zero.
        if peso1 + peso2 + peso3 == 0:
            return jsonify({
                "Resultado": "A soma dos PESOS não poderá ser zero!"
            }), 400
            
        # Chamando a função para realizar o cálculo.
        resultado = calcular_media_ponderada(
            nota1,
            nota2,
            nota3,
            peso1,
            peso2,
            peso3
        )
        return jsonify({
            "Média Ponderada": resultado
        })
        
    except ValueError:
        return jsonify({
            "Resultado": "Revise as Informações - Deverão ser NUMÉRICOS!"
        }), 400
    except Exception as e:
        return jsonify({
            "Resultado": f"Ocorreu um erro GERAL: {str(e)}"
        }), 500

        

    