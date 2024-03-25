import os

from docarray import Document, DocumentArray
from fastapi import APIRouter
from tqdm import tqdm

from .content_based_service import ContentBasedRecomendation
from .processor_service import ProcessorService
from .content_based_service import ContentBasedRecomendation
from .processor_router import preprocess_documents
from .semantic_service import SemanticRelationRecommender
from gensim import corpora, models

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import gensim
import nltk

router = APIRouter()


@router.get("/semantic-relations")
def semantic_relations():
    results = []
    result_preprocess = preprocess_documents()
    #print(result_preprocess)
    for item in result_preprocess["results"]:

        text = item["texto"]
        title = item["title"]
        classification = item["classification"]
        resolution = item["resolution"]
        pdf_path = item["pdf_path"]
        dates = item["dates"]
        semantic_service = SemanticRelationRecommender(text=text, title=title, classification=classification, resolution=resolution, pdf_path=pdf_path, dates=dates)
        results.append(semantic_service.semantic_relations_())
    return results


# @router.post("/semantic-recommender")
# def semantic_recommender():
#     entrada = request.json
#     semantic = semantic_relations()



#     return 
# def calculate_similarity(doc_en, doc_pt):
#     doc_en = nlp(doc_en)
#     doc_pt = nlp(doc_pt)
#     return doc_en.similarity(doc_pt)
    