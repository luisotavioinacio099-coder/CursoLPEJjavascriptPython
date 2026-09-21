# comunica com o Docker onde esta a imagem do Projeto Flask em Python
FROM python:3.12-slim

# Instrodução onde esta as pastas dentro do Container do Docker,onde estara o Projeto em Pyyhon !
WORKDIR /app

# Chama todas as bibliotecas necessárias para roder o Projeto Em pythonno ambiente Docker!
RUN pip install --no-cache-dir "Flask>=3,<4"

# Copiar os arqueivos da ásta local para dentro das pasta do Container levatado no Docker!
COPY  . .

# Porta para comunicar e rodar o Projeto hospedado no Container.
EXPOSE 5000