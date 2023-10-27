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
    uvicorn.run("main:app", host="127.0.0.1", port=8088, reload=True)



    # user_ip = request.client.host
    # logging.info(f"User {user_ip} is requesting to preprocess documents")
    # response = requests.get(f"https://ipinfo.io/{user_ip}/json")
    # location_data = response.json()
    # breakpoint()