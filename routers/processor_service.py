import re

import PyPDF2
import spacy
from dateutil import parser
from docarray import DocumentArray

import logging

nlp = spacy.load("pt_core_news_sm")


class ProcessorService:
    def __init__(self, doc_array: DocumentArray):
            self.doc_array = doc_array  # path to the pdf file
            self.text = ""

    def extract_text(self) -> str:
        for document in self.doc_array:
            pdf_path = document.tags.get("path")
            if pdf_path:
                read_pdf = PyPDF2.PdfReader(pdf_path)
                number_of_pages = len(read_pdf.pages)
                for page_num in range(number_of_pages):
                    page = read_pdf.pages[page_num]
                    content = page.extract_text()
                    doc = nlp(content)
                    self.text += doc.text + "\n"

        return self.text

    def preprocess_text(self) -> str:
        # pre processar o texto do documento
        # retirar caracteres especiais
        # retirar pontuacoes
        # retirar stopwords
        from nltk.corpus import stopwords

        stopwords = stopwords.words("portuguese")
        stopwords_personalizadas = [
            "universidade federal tocantins",
            "fundação universidade federal tocantins",
            "uft",
            "universidad federal tocantins",
        ]
        text = ""
        doc = nlp(self.text)
        text_formatted = spacy.tokens.Doc(
            doc.vocab,
            words=[
                token.text.lower()
                for token in doc
                if not token.is_space
                and not token.is_punct
                and not (
                    token.text.lower() in stopwords and token.text.lower() != "conselho"
                )
                and token.text.lower() not in stopwords_personalizadas
            ],
        )
        text_formatted = " ".join([token.text for token in text_formatted])
        return text_formatted

    def classification(self, text) -> str:
        # classificar o documento dividir entre consiuni e consepe
        if "consuni" in text.lower() or "conselho universitário" in text.lower():
            return "Consuni"
        if "consepe" in text.lower() or "conselho de ensino" in text.lower():
            return "Consepe"
        return "Não classificado"

    def extract_publication_date(self) -> str:
        # extrair a data de publicação do documento
        if not self.text:
            self.extract_text()
        datas = []
        #date_pattern = r"\d{1,2} de [a-zA-Z]+ de \d{4}"
       # date_pattern = r"palmas\s\d+\s[a-zA-Z]+\s\d{4}"

        date_pattern = r"\d{1,2} de [a-zA-Z]+ de \d{4}"
        documents = self.text.split("\n")
        for document in documents:
            
            match = re.search(date_pattern, document.lower())
            if match:
                # verificar demais grupos

                day = match.group().split(" ")[0]
                # print(day)
                month = match.group().split(" ")[2]
                # print(month)
                year = match.group().split(" ")[4]
                # print(year)
                month_dict = {
                    "janeiro": "01",
                    "fevereiro": "02",
                    "março": "03",
                    "abril": "04",
                    "maio": "05",
                    "junho": "06",
                    "julho": "07",
                    "agosto": "08",
                    "setembro": "09",
                    "outubro": "10",
                    "novembro": "11",
                    "dezembro": "12",
                }
                month = month_dict[month.lower()]
                date = f"{day}/{month}/{year}"

                datas.append(date)

        return datas

    def extract_signatures(self, text) -> str:
        # extrair as assinaturas do documento

        # prof_pattern = r"prof\s+([a-z]+\s+[a-z]+)\s+presidente"

        # reitor_pattern = r"[A-Z][A-ZÁ-ÚÉÊÓÔÍ][A-ZÁ-ÚÉÊÓÔÍa-zá-úéêóôí]+\sreitor"
        prof_pattern = r"Prof\.\s[A-Z][a-z]+\s[A-Z][a-z]+"
        reitor_pattern = r"[A-Z][A-ZÁ-ÚÉÊÓÔÍ][A-ZÁ-ÚÉÊÓÔÍa-zá-úéêóôí]+\sReitor"

        # prof_pattern = r"PROF\s+([a-z]+\s+[a-z]+)\s+PRESIDENTE"

        # reitor_pattern = r"[A-Z][A-ZÁ-ÚÉÊÓÔÍ][A-ZÁ-ÚÉÊÓÔÍa-zá-úéêóôí]+\sREITOR"

        professor_match = re.search(prof_pattern, text)
        if professor_match:
            return professor_match.group()

        # Verifique se o texto contém a assinatura de um reitor
        reitor_match = re.search(reitor_pattern, text)
        if reitor_match:
            return reitor_match.group()
        return "Assinatura não encontrada"

    def extract_images(self) -> str:
        # extrair as imagens do documento
        pass

    def remove_unecessary_data(self) -> str:
        # remover dados desnecessários do documento
        if not self.text:
            self.extract_text()
        texto = self.preprocess_text()
        unecessary = [
            "universidade federal tocantins",
            "fundação universidade federal tocantins",
            "uft",
            "universidad federal tocantins",
        ]
        for word in unecessary:
            texto = texto.replace(word, "")
            #print(texto)
        return texto

    def old_new_classification(self) -> str:
        # classificar o documento como antigo ou novo
        resolution = self.extract_resolutions(self.text)
        if resolution: 
            parts = resolution.split("/")
            if len(parts) == 2:
                year_part = parts[1]
            try:
                year = int(year_part)
            except ValueError:
                return "Não foi possível determinar a data"
            if 2004 <= year <= 2015:
                return "Antigo"
            elif year >= 2015:
                return "Novo"
            else:
                return "Documento de data desconhecida"
        else:
            return "None"


    def get_pdf_path(self) -> str:
        # extrair o caminho do documento
        for i, document in enumerate(self.doc_array):
            pdf_path = document.tags.get("path")
            return pdf_path

    def extract_title(self) -> str:
        # extrair o título do documento
        pdf_path = self.get_pdf_path()
        pattern = r'(?:.*\\){3}(.*)'
        match = re.search(pattern, pdf_path)
        if match:
            title = match.group(1)
            return title
        else:
            return None
        
    def extract_resolutions(self, text) -> str:
        # extrair as resoluções do documento 
        # pattern = r"N[º°]\s?\d+\s*/\s*\d+"
        pattern = r"[Nn]\s?[º°]\s?\d+\s*/\s*\d+"
        #pattern = r"[Nn]\s*[º°]\s{2,}\d{0,2}\s*/\s*\d+"


        match = re.search(pattern, text.lower(), re.IGNORECASE)

        if match:
            resolution_number = match.group()
            return resolution_number
        else:
            pattern = r"N[º°]\s\d{3}/\d{4}"
            match = re.search(pattern, text.lower(), re.IGNORECASE)
            return match.group() if match else None

        pass

    def remove_resolution_str(self, text) -> str:
        # remover a string de resolução do texto
        if not self.text:
            self.extract_text()
        texto_formatado = self.preprocess_text()
        
        resolution = self.extract_resolutions(text)
       
        pattern = r'\d+/+\d+'
        if resolution:
            match = re.search(pattern, resolution) 
        
            if match:
                resolution_number = match.group()
                return resolution_number
            else:
                return None   
    def extract_location(self, text) -> str:
        self.text = text
        doc = nlp(self.text)
        locations = []
        for ent in doc.ents:
            if ent.label_ == "LOC":
                locations.append(ent.text)
        return locations

    def combination(self):

        dic_null = []

        for i, document in enumerate(self.doc_array):
            pdf_path = document.tags.get("path")

            if pdf_path:
                if not self.text:
                    self.extract_text()
                texto = self.extract_text()

                dates = self.extract_publication_date()
                classification = self.classification(texto)
                signature = self.extract_signatures(texto)
                texto_formatado_ = self.remove_unecessary_data()
                resolution = self.remove_resolution_str(texto) if self.remove_resolution_str(texto) else None
                title =  self.extract_title(),
                old_new = self.old_new_classification()
                
                date = dates[i] if i < len(dates) else None
                infos_return = {
                    "title": title,
                    "pdf_path": pdf_path,
                    #"texto": texto_formatado,
                    "documentStatus": old_new,
                    "dates": date,
                    "classification": classification,
                    "signature": signature,
                    "resolution": resolution,
                    # "location_of_document": self.extract_location(texto), 
                }
                if any(value is None for value in infos_return.values()):
                    dic_null.append(infos_return)
    
            if dic_null:
                    logging.info("-----------------")
                    logging.info(f"Valores nulos no documento {title}:")
                    for i, item in enumerate(dic_null, start=1):
                        for key, value in item.items():
                            if value is None:
                                logging.info(f"{i}. Atributo: {key}")
                    
    

        return infos_return