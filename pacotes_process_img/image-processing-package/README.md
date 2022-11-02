# Projeto de aprendizado de criação de pacotes de processamento de imagens em Python
## Autora do Projeto: Karina Kato

#### Tutorial de instalação inspirado no README do projeto https://github.com/HenriqueMAP/image-processing-package

#### Aula: Descomplicando a criação de pacotes de processamento de imagens em Python - Digital Innovation One
#### Bootcamp: Geração Tech Unimed-BH - Ciência de Dados
[(clique aqui para ver o meu perfil na plataforma)](https://web.dio.me/users/isabella_mfbr)

#### Tecnologia: Python

#### Data: 02/11/2022
-----------------------------------------
### Descrição
O pacote "image_processing-test" é usado para:

- Módulo "Processing":
  - Correspondência de histograma;
  - Similaridade estrutural;
  - Redimensionar imagem;

- Módulo "Utils":
  - Ler imagem;
  - Salvar imagem;
  - Plotar imagem;
  - Resultado do gráfico;
  - Plotar histograma;
---------------------------------------------
## Passo a passo da configuração para hospedar um pacote em Python no ambiente de testes Test Pypi

- [x] Instalação das últimas versões de "setuptools" e "wheel"

```
py -m pip install --user --upgrade setuptools wheel
```
- [x] Tenha certeza que o diretório no terminal seja o mesmo do arquivo "setup.py"

```
C:\User\Isabella\image-processing-package> py setup.py sdist bdist_wheel
```

- [x] Após completar a instalação, verifique se as pastas abaixo foram adicionadas ao projeto:
  - [x] build;
  - [x] dist;
  - [x] image_processing_test.egg-info.

- [x] Basta subir os arquivos, usando o Twine, para o Test Pypi:

```
py -m twine upload --repository testpypi dist/*
```

- [x] Após rodar o comando acima no terminal, será pedido para inserir o usuário e senha. Feito isso, o projeto estará hospedado no Test Pypi.hospedá-lo no Pypi diretamente.

### Nesse projeto, meu objetivo não é usar o projeto de Karina Kato para postar em meu perfil do Pypi pessoal, pois a autoria do projeto é dela. 
### Ainda não tenho projetos que possam ser utilizados como pacote, portanto apenas estou utilizando seu projeto como exemplo para o aprendizado da criação de pacotes.

### No entanto, tenha em mente que o Test Pypi, como o próprio nome diz, é apenas um ambiente de testes. Para que o projeto esteja disponível como um pacote para ser usado publicamente, é necessário hospedá-lo no site oficial do Pypi.
----------------------------------------------------
## Instalação local, após hospedagem no Test Pypi

- [x] Instalação de dependências
```
pip install -r requirements.txt
```

- [x] Instalção do Pacote

Use o gerenciador de pacotes ```pip install -i https://test.pypi.org/simple/ image-processing-test ```para instalar image_processing-test

```bash
pip install image-processing-test
```
-------------------------------------------------
## Como usar em qualquer projeto

```python
from image-processing-test.processing import combination
combination.find_difference(image1, image2)
```
<img width="auto" src="">

## Autor (quem hospedou o projeto no Test Pypi)
Isabella Firmino

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
