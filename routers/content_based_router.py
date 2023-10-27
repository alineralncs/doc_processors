import os

from docarray import Document, DocumentArray
from fastapi import APIRouter

import numpy as np

from .content_based_service import ContentBasedRecomendation
from .processor_service import ProcessorService
from .content_based_service import ContentBasedRecomendation
from .processor_router import preprocess_documents
router = APIRouter()


document_features = [
    {
        "title": "Documento 1",
        "documentStatus": 1,
        "dates": 20220101,
        "classification": "A",
        "signature": "John Doe",
        "resolution": "High",
    }
]

feature_matrix = np.array([[doc["documentStatus"], doc["dates"]] for doc in document_features])

@router.get("/available-documents")
def available_documents():
    result_preprocess = preprocess_documents()
    documents = []
    for result in result_preprocess["results"]:
        documents.append(result["title"])
        
    return {"documents": documents}
    
@router.post("/content-based-recommender")
def content_recommender(document: int):



    return {"results": results}
