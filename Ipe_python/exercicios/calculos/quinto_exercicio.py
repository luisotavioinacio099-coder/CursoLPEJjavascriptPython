# Importando as bibliotecas necessarias
from flask import request, jsonify, Blueprint

# Criando uma Blueprint (E auxilia na localização).
exercicio_5_bp = Blueprint("exercicio_5", __name__)

# Conteúdo desse exercicio:
# CALCULAR SALÁRIO FINAL. ==================
@exercicio_4_bp.post("/calculo-combustivel")
def calculo_combustivel():

    # Pegar os valores no formato JSON
    dados = request.get_json()

    distancia = dados.get("distancia")
    litros = dados.get("litros")
    

    resultado = distancia / litros

    return jsonify({"CONSUMO MEDIO (KM/L) = ": resultado})