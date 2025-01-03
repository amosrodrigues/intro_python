# Baixe a última versão do python
# docker pull python
# Baixe uma versão específica
# docker pull python:tag
# docker run -it --rm python:tag

# O comando `FROM` é usado para especificar a imagem base da qual a sua imagem irá derivar
# Neste caso vamos usar como base a imagem do Python3 mais recente
FROM python:3

# A partir da imagem do Python 3 vamos realizar uma série de passos para preparar o ambiente da nova imagem.

# O comando `WORKDIR` é usado para definir o diretório principal de execução e armazenamento no interior da imagem
WORKDIR /usr/src/app

# O comando `COPY` copia um diretório ou arquivo local para dentro da imagem durante o build
# Com isso ao executar um contêiner a partir dessa imagem os arquivos já estarão lá
# Neste caso copiamos o arquivo de requisitos para dentro do WORKDIR
COPY requirements.txt ./

# O comando `RUN` permite que executemos um comando durante o build da imagem
# Neste caso executamos a instalação das dependências, fazendo com que ao criar
# um contêiner a partir da nossa imagem, o mesmo já tenha todas as dependências instaladas
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos o resto dos arquivos do diretório atual para o WORKDIR da imagem
COPY . .

# O comando `CMD` define qual comando será executado quando criarmos um contêiner a partir da imagem
CMD [ "python", "./seu-arquivo.py" ]


# docker build -t my-python-app .
# docker run -it --rm --name my-running-app my-python-app

# docker run -it --rm --name nome-do-seu-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python seu-arquivo.py
# -v "$PWD":/usr/src/myapp - monta o diretório atual para dentro do contêiner
# -w /usr/src/myapp - muda o WORKDIR para executar o comando no diretório recém montado.