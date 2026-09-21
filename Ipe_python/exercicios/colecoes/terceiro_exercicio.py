from flask import request, jsonify, Blueprint

colecoes_login_bp = Blueprint("colecoes_login", __name__)

# Dicionário global com os usuários válidos.
usuarios = {
    "admin": "12345",
    "joao": "senha123"
}

# Tupla com os status.
status_login = (
    "sucesso",
    "falha"
)

# Tupla com as mensagens.
mensagens_login = (
    "Login efetuado com sucesso",
    "Login não realizado"
)

@colecoes_login_bp.post("/fazer_login")
def fazer_login():
    try:
        # Pegar os dados enviados no formato JSON.
        dados = request.get_json()

        # Pegando usuário e senha.
        usuario = dados.get("usuario").strip()
        senha = dados.get("senha").strip()

        # Verificando se o usuário e a senha estão corretos.
        if usuario in usuarios and usuarios[usuario] == senha:
            resposta = {
                "status": status_login[0],
                "mensagem": mensagens_login[0]
            }
        else:
            resposta = {
                "status": status_login[1],
                "mensagem": mensagens_login[1]
            }
        return jsonify(resposta), 200
    except Exception as e:
        return jsonify({
            "Resultado": f"Ocorreu um ERRO: {str(e)}"
        }), 500