# Importando os recursos do Frawemework Flask (Bibliotecas necessarias)!
from flask import request, jsonify, Blueprint

# Criando um blueprint (Será utulizada para a requisição do arquivo app.py)!
calculadora_bp = Blueprint("segunda_calculadora", __name__)

#Conteúdo principal dessa Blueprint
# SOMAR =====================
@calculadora_bp.post("/segundo_calculo_soma")
def segundo_calculo_soma():
    # Pegar os valores no formato JSON!
    dados = request.get_json()

    numero_1 = dados.get("num1")
    numero_2 = dados.get("num2")

    resultado = numero_1 + numero_2

    return jsonify({"SOMA = ": resultado})