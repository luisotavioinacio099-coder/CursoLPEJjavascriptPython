from flask import Blueprint, request, jsonify
import requests

api_bp = Blueprint("api", __name__)

API_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

@api_bp.get("/cotacao-dalor")
def cotacao_dolar():
    try:
        requests = requests.get(API_URL)

        if requests.status_code != 200:
            return jsonify({"status": f"Erro ao chamar a API. STATUS: {requests.status_code}"})

        dados_cotacao = requests.json()

        valor = f"{float(dados_cotacao['USDBRL']['bid']):.2f}"
        moeda = dados_cotacao['USDBRL']['name']

        return jsonify({
            "status": "sucesso",
            "moeda": moeda,
            "valor_real": valor
        })

    except Exception as e:
        return jsonify({"status": "erro", "mensagem": f"Erro geral: {str(e)}"})