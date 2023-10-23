
class ContentBasedRecomendation:
    def __init__(self, documents):
        self.documents = documents

    def recommend(self, input_info, num_recommendations=5):
        recomended_documents = []
        input_text = input_info["text"]
        input_date = input_info["date"]

        for document in self.documents:
            text = document["text"]
            date = document["date"]
            common_words = len(set(input_text.split()) & set(text.split()))
            
            # Você também pode considerar a data como um fator de classificação.
            # Quanto mais recente, maior a pontuação.
            date_difference = abs(input_date - date).days

            # Aqui, estamos usando uma métrica de pontuação simples. 
            # Você pode personalizar a lógica de pontuação conforme necessário.
            score = common_words - date_difference  
            recommended_docs.append((doc, score))

        recommended_docs.sort(key=lambda x: x[1], reverse=True)

        # Retornando os documentos mais recomendados
        return recommended_docs[:num_recommendations]