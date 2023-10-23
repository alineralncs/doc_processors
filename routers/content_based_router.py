import os

from docarray import Document, DocumentArray
from fastapi import APIRouter

from .content_based_service import ContentBasedRecomendation
from .processor_service import ProcessorService
from .content_based_service import ContentBasedRecomendation
from .processor_router import preprocess_documents
router = APIRouter()


@router.get("/available-documents")
def available_documents():
    result_preprocess = preprocess_documents()
    documents = []
    for result in result_preprocess["results"]:
        documents.append(result["title"])
        
    return {"documents": documents}
    
@router.post("/content-based-recommender")
def content_recommender(input_info: dict):
    try:
        documents = preprocess_documents()["results"]
        num_recommendations = input_info["num_recommendations"]
        content_recommendation = ContentBasedRecomendation(documents)
        recommendations = content_recommendation.recommend(input_info, num_recommendations)

        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao gerar recomendações")



    return {"results": results}
