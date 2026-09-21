# Importando as bibliotecas necessarias
from flask import request, jsonify, Blueprint

# Criando uma Blueprint (E auxilia na localização).
exercicio_4_bp = Blueprint("exercicio_4", __name__)

# Conteúdo desse exercicio:
# CALCULAR SALÁRIO FINAL. ==================
@exercicio_4_bp.post("/calculo-troco")
def calculo_troco():

    # Pegar os valores no formato JSON
    dados = request.get_json()

    valor_compra = dados.get("valor_compra")
    valor_pago = dados.get("valor_pago")
    

    resultado = valor_pago - valor_compra

    return jsonify({"TROCO = ": resultado})