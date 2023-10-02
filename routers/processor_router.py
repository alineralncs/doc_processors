import os

from docarray import Document, DocumentArray
from fastapi import APIRouter

from .processor_service import ProcessorService

router = APIRouter()


@router.get("/preprocess")
def preprocess_documents():
    root_directory = "documents_new"
    results = []
    # chamar funcao de pre processamento
    for year in range(2014, 2024):
        for folder_name in ["Consuni", "Consepe"]:
            folder_path = os.path.join(root_directory, folder_name, str(year))

            for root, dirs, files in os.walk(folder_path):
                for filename in files:
                    pdf_path = os.path.join(root, filename)
                    print(pdf_path)

                    doc_array = DocumentArray()
                    doc_array.append(Document(path=pdf_path))

                    processor_service = ProcessorService(doc_array)

                    results.append(processor_service.combination())
    for x in results:
        print(x)
        print('\n\n\n')

    return {"results": results}
