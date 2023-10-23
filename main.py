from fastapi import FastAPI
import logging

from routers import processor_router, content_based_router

logging.basicConfig(
    filename='app.log',      
    level=logging.DEBUG,    
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  
)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "DocProcessor API running!"}


app.include_router(processor_router.router)
app.include_router(content_based_router.router)
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8089, reload=True)