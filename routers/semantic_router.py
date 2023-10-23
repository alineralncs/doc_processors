import os

from docarray import Document, DocumentArray
from fastapi import APIRouter

from .content_based_service import ContentBasedRecomendation
from .processor_service import ProcessorService
from .content_based_service import ContentBasedRecomendation
from .processor_router import preprocess_documents
router = APIRouter()


@router.post("/semantic-recommender")
def semantic_recommender():
    result_preprocess = preprocess_documents()

        
    return