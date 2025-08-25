# %%

import pandas as pd

filmes = pd.read_csv("./ml-latest-small/movies.csv")

rating = pd.read_csv("./ml-latest-small/ratings.csv")

filmes.head(60)

# %%

# Relaciona filmes com ratings

df = pd.merge(rating, filmes, on="movieId")
df = df.drop(columns=['timestamp'])

# Tabela Pivot

pivot = df.pivot_table(
    index='userId', 
    columns='movieId',
    values='rating')

# %%

# Cria o dicionário para transformar Id em Nome

idd = filmes.set_index('movieId')['title'].to_dict()

# %%

def recomendar(titulo, filmes, pivot, n=5):
    # Filtra pelo filme escolhido

    filtro = filmes[filmes['title'] == titulo]

    if filtro.empty:
        print("Filme não encontrado.")
        return
    
    # seleciona o filme escolhido
    movie_id = filtro.iloc[0]['movieId']

    # correlação
    corr = pivot.corr()

    #similares com o filme escolhido, sem N/As e do maior para o menor
    similar = corr[movie_id].dropna().sort_values(ascending=False)

    #Remove o próprio filme dos similares
    similar = similar.drop(movie_id)  

    #notas médias por notas de cada usuário
    notas_medias = df.groupby('movieId')['rating'].mean()
    
    #IDs similares
    top_ids = similar.head(n).index

    #Construção da tabela com Filme, Nota e semelhança
    #Os for são usados para adicionar as informações para cada parte do dicionário
    final = pd.DataFrame({

        "filme": [idd[i] for i in top_ids],
        "Nota": [notas_medias[i] for i in top_ids],
        "% Semelhança": [similar[i] for i in top_ids]
    })

    return final

# %%

titulo2 = input("nome do filme: ")
tabela = recomendar(titulo2, filmes, pivot, n=5)
print(tabela.head(10))
