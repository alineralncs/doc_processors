import re

import PyPDF2
import spacy
from dateutil import parser
from docarray import DocumentArray
from tinydb import TinyDB, Query

nlp = spacy.load("pt_core_news_sm")


class ProcessorService:
    def __init__(self, doc_array: DocumentArray, pdf_path):
        self.doc_array = doc_array  # path to the pdf file
        self.text = ""
        self.db = TinyDB('db.json')
        self.pdf_path = pdf_path
        self.query = Query()

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
<<<<<<< HEAD
<<<<<<< HEAD
        date_pattern = r"palmas\s\d+\s[a-zA-Z]+\s\d{4}"
        date_pattern_new_documents = r"\d+ (\d{1,2}) ([a-zA-Z]+) (\d{4})"

        documents = text.split("\n")
=======
        date_pattern = r"\d{1,2} de [a-zA-Z]+ de \d{4}"
        documents = self.text.split("\n")
>>>>>>> parent of 957d357 (remocao de stopwords e outros, padronizacao data, add resolucao)
        for document in documents:
            match = re.search(date_pattern_new_documents, document) or re.search(date_pattern, document)
            print(match)

=======
        date_pattern = r"\d{1,2} de [a-zA-Z]+ de \d{4}"
        documents = self.text.split("\n")
        for document in documents:
            match = re.search(date_pattern, document)
>>>>>>> parent of 957d357 (remocao de stopwords e outros, padronizacao data, add resolucao)
            if match:
                datas.append(match.group())

        return datas

    def extract_signatures(self, text) -> str:
        # extrair as assinaturas do documento
        prof_pattern = r"Prof\.\s[A-Z][a-z]+\s[A-Z][a-z]+"
        reitor_pattern = r"[A-Z][A-ZÁ-ÚÉÊÓÔÍ][A-ZÁ-ÚÉÊÓÔÍa-zá-úéêóôí]+\sReitor"

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
        # remover dados desnecessarios do documento
        pass

    def extract_resolutions(self) -> str:
        # extrair as resoluções do documento
<<<<<<< HEAD
<<<<<<< HEAD
        # pattern = r"N[º°]\s?\d+\s*/\s*\d+"
        pattern = r"[Nn]\s?[º°]\s?\d+\s*/\s*\d+"
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            resolution_number = match.group()
            return resolution_number
        else:
            return None
=======
=======
>>>>>>> parent of 957d357 (remocao de stopwords e outros, padronizacao data, add resolucao)
        pass
>>>>>>> parent of 957d357 (remocao de stopwords e outros, padronizacao data, add resolucao)

    def combination(self):
        if self.db.search(self.query.pdf_path == self.pdf_path):
            print("Documento já inserido")
            return

        if not self.text:
            self.extract_text()
<<<<<<< HEAD
<<<<<<< HEAD

        texto_formatado = self.preprocess_text()
        dates = self.extract_publication_date(texto_formatado)
        classification = self.classification(texto_formatado)
        signature = self.extract_signatures(texto_formatado)
        resolution = self.extract_resolutions(texto_formatado)
=======
        dates = self.extract_publication_date()
        classification = self.classification(self.text)
        signature = self.extract_signatures(self.text)
>>>>>>> parent of 957d357 (remocao de stopwords e outros, padronizacao data, add resolucao)
=======
        dates = self.extract_publication_date()
        classification = self.classification(self.text)
        signature = self.extract_signatures(self.text)
>>>>>>> parent of 957d357 (remocao de stopwords e outros, padronizacao data, add resolucao)

        for i, document in enumerate(self.doc_array):
            pdf_path = document.tags.get("path")

            if pdf_path:
                date = dates[i] if i < len(dates) else None
                infos_return = {
                    "pdf_path": pdf_path,
                    "dates": date,
                    "classification": classification,
                    "signature": signature,
                }
            
                self.db.insert(infos_return)

        return {'data': 'Todos os documentos foram inseridos'}
