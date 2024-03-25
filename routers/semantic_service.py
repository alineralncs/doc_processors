from docarray import Document, DocumentArray
import spacy
import pprint
from spacy import displacy
import imgkit
import os
import time
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import re



nlp = spacy.load("pt_core_news_lg")
class SemanticRelationRecommender:
    def __init__(self, text: str, title: str, classification:str, dates: str, resolution: str, pdf_path: str):
        self.text = text
        self.title = title
        self.resolution = resolution
        self.pdf_path = pdf_path
        self.dates = dates
        self.classification = classification

    
    def recommender(self):
        # chamar o modelo de recomendação semântica
        pass
    
    def text_preprocessing(self):
        # preprocessar o texto
        text = self.text

        doc = nlp(text)
        unwanted_words = {"art", "uft", "edu", "br"}

        unecessary_words = [
            "fundação",
            "universidade",
            "federal",
            "tocantins",
            "art",
            "°"
            "FUNDAÇÃO",
            "UNIVERSIDADE",
            "FEDERAL",
            "TOCANTINS",
            "Art",
            "secretaria",
            ".",
            "°",
            "º",
            "conselho",
            "universitario",
            "ensino",
            "pesquisa",
            "extensao",
            "reitor",
            "vice-reitor",
            "edu", 
            "br",
            "uft", 
            "https"
        ]
        import nltk

        # baixa as stopwords
        # nltk.download('stopwords')

        # para escolher as stopwords do português adicionamos a opçaõ de língua "portuguese"
        stopwords = nltk.corpus.stopwords.words('portuguese')
       # pattern = r"[Nn]\s?[º°]\s?\d+\s*/\s*\d+"
        pattern_art = r"\b[aA][rR][tT]\b"
        pattern_uft = r"\b[uU][fF][tT]\b"
        pattern_edu = r"\b[eE][dD][uU]\b"
        
        texto_sem_art = re.sub(pattern_art, "", text)
        texto_sem_uft = re.sub(pattern_uft, "", text)
        texto_sem_edu = re.sub(pattern_edu, "", text)

    
        # if re.search(pattern_art, text):

        #     print("Encontrou 'art' no texto.")

        # if re.search(pattern_uft, text):
        #     print("Encontrou 'uft' no texto.")

        # if re.search(pattern_edu, text):
        #     print("Encontrou 'edu' no texto.")
        #pattern = r"[Nn]\s*[º°]\s{2,}\d{0,2}\s*/\s*\d+"


      
        text_formated = spacy.tokens.Doc(doc.vocab,

         words=[
            token.text.lower()
            for token in doc
            if not token.is_punct
            and not token.is_space
            and not token.is_bracket
            and not token.text in unecessary_words
            and not token.text in stopwords
            and token.text.lower() not in unwanted_words

        ]
        )
        
        text_formatted = " ".join([token.text for token in text_formated if not token.is_space and not token.is_bracket  and not token.is_punct and not token.text in unecessary_words and not token.text in stopwords  and token.text.lower() not in unwanted_words
])
        
        return text_formatted

    def cut_text(self):
        text = self.text_preprocessing()
        palavras = text.split()[:70]
        primeiras_30_linhas = ' '.join(palavras)
        #print(primeiras_30_linhas)
        return primeiras_30_linhas

    def text_(self):
        doc = nlp(self.cut_text())
        verbos_interesse = ["regulamenta", "dispõe", "cria", "estabelece", 
                    "institui", "aprova", "altera", "anula", 
                    "convoca", "instituir"]
        for token in doc:
            if token.pos_ == "VERB" and token.text.lower() in verbos_interesse:
                
                indice_verbo = token.i
                indice_final_sentenca = token.sent[-1].i
                limite_palavras_apos_verbo = 20

                indices_palavras_apos_verbo = [i + 1 for i in range(indice_verbo, indice_final_sentenca) if i + 1 <= indice_final_sentenca][:limite_palavras_apos_verbo]
              
                tokens_entre_verbo_e_palavras = [doc[i] for i in indices_palavras_apos_verbo]
                tokens_entre_verbo_e_palavras.insert(0, doc[indice_verbo])
                texto_entre_verbo_e_palavras = ' '.join(token.text for token in tokens_entre_verbo_e_palavras)
                #pprint.pprint(texto_entre_verbo_e_palavras)
                return texto_entre_verbo_e_palavras

    def syntatic_analysis(self):
        # análise sintática
        #doc = nlp(self.text_())
        texto = "dispoe sobre normas funcionamento assembleia constituinte interna uft"
        doc = nlp(texto)
        print("syntatic analysis")
        print("-" * 50)

        html = displacy.render(doc, style="dep", options={'distance': 200, "color": "#40398F"})
        pasta_destino = "static"

        timestamp = str(time.time()).replace(".", "_")
        nome_arquivo_html = f"arvore_dependencia_{timestamp}.html"
        nome_arquivo_imagem = f"arvore_dependencia_{timestamp}.png"
        caminho_imagem = os.path.join(pasta_destino, nome_arquivo_imagem)
        caminho_arquivo_html = os.path.join(pasta_destino, nome_arquivo_html)

        with open(caminho_arquivo_html, "w", encoding="utf-8") as file:
            file.write(html)

                # Gere a imagem a partir do arquivo HTML
        imgkit.from_file(caminho_arquivo_html, os.path.join(pasta_destino, nome_arquivo_imagem))

        #print(f"A imagem foi salva em: {caminho_imagem}")

        pass
    
    def semantic_analysis(self):
        # análise semântica
        pass

    def simple_relation_extraction(self):
        text = self.cut_text()
        resolution = self.resolution if self.resolution else "none"

        verbos_interesse = ["regulamenta", "dispõe", "cria", "estabelece", 
                    "institui", "aprova", "altera", "anula", 
                    "convoca", "instituir"]
        doc = nlp(self.text_())
        #breakpoint()
        for token in doc:
            if token.pos_ == "VERB" and token.text.lower() in verbos_interesse:
                verb = token.text
              
                objeto_direto = [child.text for child in token.children if child.dep_ == "obj"]
                objeto_direto = ' '.join(objeto_direto)

        
        return resolution, verb, objeto_direto
    def word_cloud(self):
        # chamar a função de nuvem de palavras
        wordcloud = WordCloud(width=800, height=800, 
                    background_color ='white', 
                    min_font_size = 10).generate(self.text_preprocessing())
        plt.figure(figsize = (8, 8), facecolor = None)
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

    def complex_relation_extraction(self):
        # extrair relações complexas
        lista = ""
        text = self.cut_text()
        resolution = self.resolution
        doc = nlp(self.text_())
        verbos_interesse = ["regulamenta", "dispõe", "cria", "estabelece", 
                    "institui", "aprova", "altera", "anula", 
                    "convoca", "instituir"]
        for token in doc:
            if token.pos_ == "VERB" and token.text.lower() in verbos_interesse:
                verb = token.text
                # objeto_direto = [child.text for child in token.children if child.dep_ == "obj"]
                # objeto_direto = ' '.join(objeto_direto)
            for child in token.children:
                if child.dep_ == "obj":
                    print(child.text, child.dep_)
                    lista += child.text + " "
                if child.dep_ == "obl":
                    lista += child.text + " "
                if child.dep_ == "nmod":
                    lista += child.text + " "
                if child.dep_ == "amod":
                    lista += child.text + " "
        #print(resolution, verb, lista)
        return resolution, verb, lista

    def semantic_relations_(self):
        # chamar a função de extração de relações semânticas
        # self.syntatic_analysis()
        semantic = {
            "simple_relation": self.simple_relation_extraction(),
            "complex_relation": self.complex_relation_extraction()
        }
        # self.word_cloud()
        return semantic
