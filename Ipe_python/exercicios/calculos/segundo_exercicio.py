# Importando as bibliotecas necessarias
from flask import request, jsonify, Blueprint

# Criando uma Blueprint (E auxilia na localização).
exercicio_2_bp = Blueprint("exercicio_2", __name__)

# Conteúdo desse exercicio:
# CALCULAR SALÁRIO FINAL. ==================
@exercicio_2_bp.post("/calculo-area-retangulo")
def calculo_area_retangulo():

    # Pegar os valores no formato JSON
    dados = request.get_json()

    salario = dados.get("largura")
    desconto = dados.get("altura")

    resultado = largura - altura

    return jsonify({"AREA DO RETANGULO = ": resultado})