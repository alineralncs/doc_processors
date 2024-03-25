from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from nltk.tokenize import word_tokenize

import string
from gensim.models import Word2Vec
from gensim.similarities import WmdSimilarity
import numpy as np

data = [
    {
        "simple_relation": ["none", "regulamenta", "processo escolha mandato"],
        "complex_relation": [None, "regulamenta", "processo escolha mandato listas tríplices "]
    },
    {
        "simple_relation": ["02/2004", "dispõe", "normas egrégio"],
        "complex_relation": ["02/2004", "dispõe", "normas egrégio funcionamento assembléia constituinte interna universitário sessão abril art. assembléia "]
    },
    {
        "simple_relation": ["003/2004", "cria", "regimento"],
        "complex_relation": ["003/2004", "cria", "regimento interno universitário interno universitário "]
    },
    {
        "simple_relation": ["09/2005", "aprova", "criação"],
        "complex_relation": ["09/2005", "aprova", "criação regimento interno "]
    },
    {
        "simple_relation": ["36/2021", "dispõe", "calendário"],
        "complex_relation": ["36/2021", "dispõe", "calendário acadêmico "]
    },
    {
        "simple_relation": ["51/2021", "dispõe", "calendário ano"],
        "complex_relation": ["51/2021", "dispõe", "calendário ano acadêmico letivo universitário "]
    },
        {
        "simple_relation": ["51/2021", "regular", "calendário ano"],
        "complex_relation": ["51/2021", "regular", "calendário ano acadêmico letivo universitário "]
    }
]

# Combine relações simples e complexas em uma lista de textos
corpus = [relation[2] for item in data for relation in item.values() if relation[0] is not None]

# Inicialize o vetorizador TF-IDF
vectorizer = TfidfVectorizer()

# Ajuste e transforme os dados
tfidf_matrix = vectorizer.fit_transform(corpus)

def recommend(query):
    # Transforme a consulta em um vetor TF-IDF
    query_vector = vectorizer.transform([query])

    # Calcule as similaridades de cosseno entre a consulta e cada entrada
    similarities = cosine_similarity(query_vector, tfidf_matrix)

    # Encontre o índice da entrada com a maior similaridade
    best_index = np.argmax(similarities)

    # Retorne a entrada correspondente
    return data[best_index]

# Exemplo de uso:
query = "regulamento processo escolha mandato"
recommendation = recommend(query)
print("Consulta:", query)
print("Recomendação:", recommendation)


corpus = []
for item in data:
    print(item)
    corpus.append(item["simple_relation"])
    corpus.append(item["complex_relation"])

# Treinamento do modelo Word2Vec
model = Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=1, workers=4)

# Exemplo de uso do modelo
print("Vetor da palavra 'regulamenta':")
print(model.wv['regulamento processo escolha'])

# Encontrar palavras semanticamente similares a uma palavra específica
similar_words = model.wv.most_similar('regulamento processo escolha')
print("Palavras semanticamente similares a 'regulamento processo escolha':")
for word, similarity in similar_words:
    print(word, similarity)