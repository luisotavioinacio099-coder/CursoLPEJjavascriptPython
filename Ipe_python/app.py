from flask import Flask, jsonify, request
from flask_cors import CORS

# Importando as Blueprints
from exemplos.calculadora.calculadora import calculadora_bp
from exemplos.calculadora.calculadora_simples import calculos_basicos_bp
from exemplos.laco_repeticao.laco_repeticao import laco_repeticao_bp
from exemplos.colecos.carrinho_compras import carrinho_compra_bp
from exemplos.manipulacao_arquivos.manipulacao_arquivo import arquivo_bp as arquivo_exemplo_bp

# Exercícios
from exerciocios.calculos.primeiro_exercicio import exercicio_1_bp
from exerciocios.calculos.primeiro_exercicio import exercicio_2_bp
from exerciocios.calculos.primeiro_exercicio import exercicio_3_bp
from exerciocios.calculos.primeiro_exercicio import exercicio_4_bp
from exerciocios.calculos.primeiro_exercicio import exercicio_5_bp
from exerciocios.calculos.primeiro_exercicio import operadores_calculo_bp_1
from exerciocios.calculos.segundo_exercicio import operadores_calculo_bp_2
from exerciocios.calculos.terceiro_exercicio import operadores_calculo_bp_3
from exerciocios.calculos.quarto_exercicio import operadores_calculo_bp_4
from exerciocios.calculos.quinto_exercicio import operadores_calculo_bp_5

from exerciocios.laco_repeticao.primeiro_exercicio import laco_calculo_bp_1
from exerciocios.laco_repeticao.primeiro_exercicio import laco_calculo_bp_2

from exerciocios.chamadas_js_fetch_python.primeiro_exercicio.back_end import operadores_bp
from exerciocios.chamadas_js_fetch_python.segundo_exercicio.back_end import conversor_temperatura_bp
from exerciocios.chamadas_js_fetch_python.terceiro_exercicio.back_end import juros_simples_bp
from exerciocios.chamadas_js_fetch_python.quarto_exercicio.back_end import estoque_bp
from exerciocios.chamadas_js_fetch_python.quinto_exercicio.back_end import dividir_conta_bp

from exerciocios.colecoes.primeiro_exercicio import colecoes_bp
from exerciocios.colecoes.primeiro_exercicio import colecoes_ganho_bp
from exerciocios.colecoes.primeiro_exercicio import colecoes_login_bp

from exerciocios.manipilacao_de_arquivo_exercicio import arquivo_bp as arquivo_exercicio_bp

from exerciocios.chamando_api_externa.arquivo_api import api_bp


# Criando aplicação Flask
app = Flask(__name__)

# Ativando CORS
CORS(app)


# Registrando Blueprints
app.register_blueprint(calculadora_bp)
app.register_blueprint(calculos_basicos_bp)
app.register_blueprint(laco_repeticao_bp)
app.register_blueprint(carrinho_compra_bp)
app.register_blueprint(arquivo_exemplo_bp)

# Exercícios
app.register_blueprint(exercicio_1_bp)
app.register_blueprint(exercicio_2_bp)
app.register_blueprint(exercicio_3_bp)
app.register_blueprint(exercicio_4_bp)
app.register_blueprint(exercicio_5_bp)

app.register_blueprint(operadores_calculo_bp_1)
app.register_blueprint(operadores_calculo_bp_2)
app.register_blueprint(operadores_calculo_bp_3)
app.register_blueprint(operadores_calculo_bp_4)
app.register_blueprint(operadores_calculo_bp_5)

app.register_blueprint(laco_calculo_bp_1)
app.register_blueprint(laco_calculo_bp_2)

app.register_blueprint(operadores_bp)
app.register_blueprint(conversor_temperatura_bp)
app.register_blueprint(juros_simples_bp)
app.register_blueprint(estoque_bp)
app.register_blueprint(dividir_conta_bp)

app.register_blueprint(colecoes_bp)
app.register_blueprint(colecoes_ganho_bp)
app.register_blueprint(colecoes_login_bp)

app.register_blueprint(arquivo_exercicio_bp)
app.register_blueprint(api_bp)


@app.get("/chamar-conteudoo")
def iniciarMsg():
    return "seja Bem vindo(a), sua primeira aplicação em Python com framework Flask!"