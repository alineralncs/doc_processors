import json
import os

from docarray import Document, DocumentArray
from fastapi import APIRouter
from tinydb import TinyDB, Query

from .processor_service import ProcessorService

router = APIRouter()

@router.get("/db")
def get_all_documents():
    with open('db.json', 'r') as db:
        db = json.load(db)
        return db
    
@router.get("/db-none")
def get_all_documents_with_some_value_none():
    results = []
    db = TinyDB('db.json')
    entradas = db.all()

    for entrada in entradas:
        for chave, valor in entrada.items():
            if valor is None:
                results.append(entrada)
                print(f"Encontrou um valor None na entrada: {entrada}")
                break  
    db.close()
    return results
    
@router.get("/preprocess")
def preprocess_documents():
    root_directory = "documents_new"
    results = []
    # chamar funcao de pre processamento
    for year in range(2014, 2024):
        for folder_name in ["Consuni", "Consepe"]:
            folder_path = os.path.join(root_directory, folder_name, str(year))
<<<<<<< HEAD
=======
            print(folder_path)
>>>>>>> parent of 957d357 (remocao de stopwords e outros, padronizacao data, add resolucao)

            for root, dirs, files in os.walk(folder_path):
                for filename in files:
                    pdf_path = os.path.join(root, filename)
                    print(pdf_path)

                    doc_array = DocumentArray()
                    doc_array.append(Document(path=pdf_path))

                    processor_service = ProcessorService(doc_array, pdf_path)

                    results.append(processor_service.combination())
                    
    return {"results": results}
