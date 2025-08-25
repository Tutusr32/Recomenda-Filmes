🎬 Sistema de Recomendação de Filmes

Este é o meu primeiro projeto em Python, onde desenvolvi um sistema simples de recomendação de filmes usando análise de correlação entre notas de usuários.
O objetivo foi aprender na prática como manipular dados com pandas e aplicar conceitos básicos de recomendação.

⚡ Importante: neste projeto utilizei a IA como auxílio para estruturar algumas partes, mas entendo 100% do código e consigo recriá-lo por conta própria.

📂 Dados Utilizados

Os dados usados fazem parte do MovieLens Dataset (ml-latest-small):

movies.csv
 → contém informações dos filmes (ID, título e gênero).

ratings.csv
 → contém as avaliações feitas por usuários (nota de 0.5 a 5.0).

🚀 Como Rodar o Projeto
1️⃣ Clone o repositório:
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2️⃣ Instale as dependências:

É necessário ter Python 3.x instalado. Depois, instale as bibliotecas necessárias:

pip install pandas

3️⃣ Baixe o dataset do MovieLens:

Baixe a versão ml-latest-small neste link:
👉 https://grouplens.org/datasets/movielens/

Extraia os arquivos e coloque a pasta ml-latest-small dentro do diretório do projeto.

4️⃣ Execute o código:
python recomendador.py

5️⃣ Informe o nome de um filme:

Digite o título de um filme presente no dataset (exemplo: Toy Story (1995)) e o programa retornará recomendações de filmes similares com nota média e porcentagem de semelhança.

🛠️ Tecnologias Utilizadas

Python 3.x

Pandas

📊 Exemplo de Saída
nome do filme: Toy Story (1995)

             filme       Nota  % Semelhança
0   Toy Story 2 (1999)  3.56       0.72
1       Bug's Life (1998)  3.45       0.65
2  Monsters, Inc. (2001)  3.78       0.63
...

📌 Observações

Este é um projeto inicial de estudo, focado em entender manipulação de dados e sistemas de recomendação.

A IA foi usada apenas como auxílio no processo de aprendizado, mas todo o código foi estudado e é de total compreensão minha.
