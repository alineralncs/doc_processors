from fastapi import FastAPI

from routers import processor_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "DocProcessor API running!"}


app.include_router(processor_router.router)
