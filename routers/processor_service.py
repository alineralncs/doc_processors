import re

import PyPDF2
import spacy
from docarray import DocumentArray
from tinydb import TinyDB, Query

nlp = spacy.load("pt_core_news_sm")


class ProcessorService:
    def __init__(self, doc_array: DocumentArray, pdf_path):
        self.doc_array = doc_array  # path to the pdf file
        self.text = ""
        self.db = TinyDB('db.json')
        self.pdf_path = pdf_path

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
        if "consepe" in text.lower() or "conselho ensino" in text.lower():
            return "Consepe"
        return "Não classificado"

    def extract_publication_date(self, text) -> str:
        # extrair a data de publicação do documento
        if not self.text:
            self.extract_text()
        datas = []
        date_pattern = r"palmas\s\d+\s[a-zA-Z]+\s\d{4}"
        date_pattern_new_documents = r"\d+ (\d{1,2}) ([a-zA-Z]+) (\d{4})"

        documents = text.split("\n")
        for document in documents:
            match = re.search(date_pattern_new_documents, document) or re.search(date_pattern, document)
            print(match)

            if match:
                # verificar demais grupos
                day = match.group().split(" ")[1]
                # print(day)
                month = match.group().split(" ")[2]
                # print(month)
                year = match.group().split(" ")[3]
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

        prof_pattern = r"prof\s+([a-z]+\s+[a-z]+)\s+presidente"

        reitor_pattern = r"[A-Z][A-ZÁ-ÚÉÊÓÔÍ][A-ZÁ-ÚÉÊÓÔÍa-zá-úéêóôí]+\sreitor"

        professor_match = re.search(prof_pattern, text)
        if professor_match:
            nome = professor_match.group().split(" ")[1]
            sobrenome = professor_match.group().split(" ")[2]

            return f"{nome} {sobrenome}"

        reitor_match = re.search(reitor_pattern, text)
        if reitor_match:
            return reitor_match.group()
        return "Assinatura não encontrada"

    def extract_images(self) -> str:
        # extrair as imagens do documento
        pass

    def remove_unecessary_data(self) -> str:
        # remover dados desnecessarios do documento
        pass

    def extract_resolutions(self, text) -> str:
        # extrair as resoluções do documento
        # pattern = r"N[º°]\s?\d+\s*/\s*\d+"
        pattern = r"[Nn]\s?[º°]\s?\d+\s*/\s*\d+"
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            resolution_number = match.group()
            return resolution_number
        else:
            return None

    def combination(self):

        # Verificando se o documento já existe.
        query = Query()

        if self.db.search(query.pdf_path == self.pdf_path):
            print("Documento já inserido")
            return

        if not self.text:
            self.extract_text()

        texto_formatado = self.preprocess_text()
        dates = self.extract_publication_date(texto_formatado)
        classification = self.classification(texto_formatado)
        signature = self.extract_signatures(texto_formatado)
        resolution = self.extract_resolutions(texto_formatado)

        for i, document in enumerate(self.doc_array):
            pdf_path = document.tags.get("path")

            if pdf_path:
                date = dates[i] if i < len(dates) else None
                infos_return = {
                    "pdf_path": pdf_path,
                    "texto": texto_formatado,
                    "dates": date,
                    "classification": classification,
                    "signature": signature,
                    "resolution": resolution,
                }
            
                self.db.insert(infos_return)

        return {'data': 'Todos os documentos foram inseridos'}

    def see_empty_values(self, pdf_info):
        for valor in pdf_info.items():
            if valor[1] is None:
                print(f"O documento {pdf_info['pdf_path']} não tem um dos valores preenchidos")
                self.db_none.insert(pdf_info)


