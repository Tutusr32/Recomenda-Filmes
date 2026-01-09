🎬 Movie Matcher: Motor de Recomendação com Pandas
Este projeto representa um marco importante na minha trajetória como desenvolvedor. Foi o meu primeiro projeto de grande escala, onde saí da sintaxe básica do Python para aplicar lógica de análise de dados real em um problema do cotidiano: "O que assistir agora?".

🚀 O Desafio
O objetivo era criar um sistema que recomendasse filmes não apenas por gênero, mas pelo comportamento de consumo dos usuários.

🧠 Lógica e Inteligência
A solução foi construída utilizando Filtragem Colaborativa baseada em itens.

Processamento: Criei uma matriz de pivô onde cada linha é um usuário e cada coluna um filme.

Correlação: Utilizei o método .corr() do Pandas para calcular a correlação de Pearson entre as avaliações de um filme escolhido e todos os outros da base.

Resultado: O sistema retorna uma lista ordenada dos filmes que possuem o maior "match" de notas com o título consultado.

🛠️ Tecnologias Utilizadas
Python 3

Pandas: Manipulação e análise da matriz de dados.

Numpy: Operações matemáticas para suporte à correlação.

📈 Lições de Evolução (O que este projeto me ensinou)
Como este repositório serve de registro para o meu crescimento técnico, listei pontos que identifiquei após a conclusão:

Limpeza de Dados: Aprendi a importância de lidar com valores nulos (NaN) que surgem quando um usuário não avaliou um filme.

Filtro de Relevância: Percebi que correlações perfeitas (1.0) podem ocorrer em filmes com pouquíssimas avaliações. Em projetos futuros, a aplicação de um filtro de count() antes da correlação é essencial.

Experiência do Usuário (UX): O sistema hoje é funcional via terminal. O próximo passo de evolução seria tratar erros de digitação e buscas parciais.

Como rodar
Certifique-se de ter o Python e o Pandas instalados.

Clone o repositório.

Execute o arquivo principal e digite o nome de um filme presente no dataset quando solicitado.
