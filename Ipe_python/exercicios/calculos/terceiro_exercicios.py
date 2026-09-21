# Importando as bibliotecas necessarias
from flask import request, jsonify, Blueprint

# Criando uma Blueprint (E auxilia na localização).
exercicio_3_bp = Blueprint("exercicio_3", __name__)

# Conteúdo desse exercicio:
# CALCULAR SALÁRIO FINAL. ==================
@exercicio_3_bp.post("/calculo-medida")
def calculo_medida():

    # Pegar os valores no formato JSON
    dados = request.get_json()

    nota_1 = dados.get("nota1")
    nota_2 = dados.get("nota2")
    nota_3 = dados.get("nota3")

    resultado = (nota_1 + nota_2 + nota_3) / 3

    return jsonify({"MEDIA = ": resultado})