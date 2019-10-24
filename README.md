# Foca aqui - aplicação
Repositório da aplicação web do projeto Foca Aqui. Consiste em duas aplicações: uma backend feita com Django que provê a api consultada pela aplicação frontend React

## Dados
As seguintes bases de dados são utilizadas na aplicação
- Votação por municipio e zona eleitoral das eleições de 2018 - fonte [Repositório de Dados Eleitorais do TSE](http://www.tse.jus.br/eleicoes/estatisticas/repositorio-de-dados-eleitorais-1/repositorio-de-dados-eleitoraishttp:// "Repositório de Dados Eleitorais do TSE")
- Evolução mensal das estatísticas por circunscrição de Delegacia  - fonte [ISP](http://www.ispdados.rj.gov.br/estatistica.html "ISP")
- Relação de Zonas Eleitorais e bairros

Estes dados podem ser baixados [aqui](https://drive.google.com/file/d/12F1P_zV82GkXKgs62gUtl-2WFqfOgjMr/view?usp=sharing "aqui").

#### Instalação backend
Com as dependências do Django e o MySQL instaladas, você vai precisar criar um banco de dados para a aplicação. Em seguida criar um arquivo local_settings.py cópia do settings.py configurando a variável DATABASE de acordo com o banco mysql criado. Por fim, rodar os comandos  `python manage.py makemigrations && python manage.py migrate` para criar as tabelas no banco.

Em seguida, baixe os arquivos CSV que irão alimentar o banco ([aqui](https://drive.google.com/file/d/12F1P_zV82GkXKgs62gUtl-2WFqfOgjMr/view?usp=sharing "aqui")) e descompacte-os na pasta data/csv/

Com isso, inicie o shell interativo do django com `python manage.py shell`e execute as funções do arquivo data/populate.py para carregar os dados dos CSVs no banco de dados

    from data.populate import *
    populate_ocorrenciasmesdata()
    populate_votacao_municipio_zona()
    populate_zonas()`

Com a instação pronta, executar `python3 manage.py runserver` para iniciar a aplicação, que será requisitada pelo frontend em localhost:8000

#### Instalação frontend
Com o NPM instalado, executar `npm install`que instalará as dependências e `npm run dev` para executar. A aplicação ficará acessível em localhost:8080