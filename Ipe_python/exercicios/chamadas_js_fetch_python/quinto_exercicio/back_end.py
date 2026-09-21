from flask import request, jsonify, Blueprint


dividir_conta_bp = Blueprint(
    "dividir_conta",
    __name__
)


@dividir_conta_bp.post("/dividir_conta")
def dividir_conta():

    try:

        # Pegando os dados enviados pelo JavaScript.
        dados = request.get_json()

        # Declarando as Variáveis.
        valor_total = float(
            dados.get("valor_total")
        )

        numero_de_pessoas = int(
            dados.get("numero_de_pessoas")
        )


        # Verificando se o número de pessoas é válido.
        if numero_de_pessoas <= 0:

            return jsonify({
                "status": "erro",
                "mensagem": "O número de pessoas deve ser maior que ZERO!"
            }), 400


        # Calculando o valor para cada pessoa.
        valor_por_pessoa = (
            valor_total / numero_de_pessoas
        )


        # Retornando o resultado para o JavaScript.
        return jsonify({
            "status": "sucesso",
            "valor_por_pessoa": valor_por_pessoa
        }), 200


    except ValueError:

        return jsonify({
            "status": "erro",
            "mensagem": "O valor da conta e o número de pessoas devem ser NUMÉRICOS!"
        }), 400


    except Exception as e:

        return jsonify({
            "status": "erro",
            "mensagem": f"Ocorreu um ERRO: {str(e)}"
        }), 500