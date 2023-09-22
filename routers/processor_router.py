from fastapi import APIRouter

router = APIRouter()

@router.get("pre-process")
def pre_process():
    # chamar funcao de pre processamento
    return {"message": "pre-process"}



