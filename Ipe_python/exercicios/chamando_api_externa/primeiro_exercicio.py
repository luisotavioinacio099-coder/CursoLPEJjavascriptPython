# Importando as bibliotecas necessárias.
from flask import request, jsonify, Blueprint
import requests

# Criando a Blueprint.
api_bp = Blueprint("api", __name__)

# Endpoint - BUSCAR CEP ==========================================================
@api_bp.get("/buscar_cep")
def buscar_cep():
    try:
        # Pegando o CEP enviado na requisição.
        dados = request.get_json()

        cep = dados.get("cep").strip()

        # Verificando se o CEP foi informado.
        if cep == "":
            return jsonify({
                "status": "erro",
                "mensagem": "Informe o CEP!"
            }), 400

        # Removendo caracteres que não sejam números.
        cep = cep.replace("-", "").replace(".", "").replace(" ", "")

        # Verificando se o CEP possui 8 números.
        if not cep.isdigit() or len(cep) != 8:
            return jsonify({
                "status": "erro",
                "mensagem": "CEP inválido! Informe um CEP com 8 números."
            }), 400

        # URL da API externa ViaCEP.
        API_URL = f"https://viacep.com.br/ws/{cep}/json/"

        # Fazendo a requisição para a API externa.
        resposta = requests.get(API_URL)

        # Verificando se a API respondeu corretamente.
        if resposta.status_code != 200:
            return jsonify({
                "status": "erro",
                "mensagem": "Erro ao consultar a API de CEP!"
            }), 500

        # Transformando a resposta da API em JSON.
        dados_cep = resposta.json()

        # Verificando se o CEP foi encontrado.
        if dados_cep.get("erro"):
            return jsonify({
                "status": "erro",
                "mensagem": f"Não foi encontrado nenhum endereço com o CEP {cep} informado"
            }), 404

        # Retornando os dados encontrados.
        return jsonify({
            "status": "sucesso",
            "cep": dados_cep.get("cep"),
            "logradouro": dados_cep.get("logradouro"),
            "bairro": dados_cep.get("bairro"),
            "cidade": dados_cep.get("localidade"),
            "estado": dados_cep.get("uf")
        }), 200

    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": f"Ocorreu um erro geral: {str(e)}"
        }), 500