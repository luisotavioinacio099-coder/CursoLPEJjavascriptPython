from flask import request, jsonify, Blueprint


estoque_bp = Blueprint(
    "estoque",
    __name__
)


@estoque_bp.post("/calculo_estoque")
def calculo_estoque():

    try:

        # Pegando os dados enviados pelo JavaScript.
        dados = request.get_json()

        # Declarando as Variáveis.
        quantidade_minima = float(
            dados.get("quantidade_minima")
        )

        quantidade_maxima = float(
            dados.get("quantidade_maxima")
        )


        # Calculando a quantidade média.
        quantidade_media = (
            quantidade_minima + quantidade_maxima
        ) / 2


        # Retornando o resultado para o JavaScript.
        return jsonify({
            "status": "sucesso",
            "quantidade_media": quantidade_media
        }), 200


    except ValueError:

        return jsonify({
            "status": "erro",
            "mensagem": "As quantidades devem ser NUMÉRICAS!"
        }), 400


    except Exception as e:

        return jsonify({
            "status": "erro",
            "mensagem": f"Ocorreu um ERRO: {str(e)}"
        }), 500