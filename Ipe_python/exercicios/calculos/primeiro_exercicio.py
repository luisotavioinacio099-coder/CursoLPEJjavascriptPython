# Importando as bibliotecas necessarias
from flask import request, jsonify, Blueprint

# Criando uma Blueprint (E auxilia na localização).
exercicio_1_bp = Blueprint("exercicio_1", __name__)

# Conteúdo desse exercicio:
# CALCULAR SALÁRIO FINAL. ==================
@exercicio_1_bp.post("/calculo-salario")
def calculo_salario():

    # Pegar os valores no formato JSON
    dados = request.get_json()

    salario = dados.get(salario)
    desconto = dados.get("desconto")

    resultado = salario - desconto

    return jsonify({"SALÁRIO FINAL = ": resultado})