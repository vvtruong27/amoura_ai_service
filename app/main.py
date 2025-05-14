# app/main.py
from fastapi import FastAPI
from app.core.config import settings
# from app.services.matching_service import MatchingService # Example of loading model at startup

app = FastAPI(
    title=settings.PROJECT_NAME,
)

# @app.on_event("startup")
# async def startup_event():
#     # Load heavy AI models here
#     # Example: MatchingService.load_model()
#     print("AI Models loaded (if any).")

@app.get("/")
async def root():
    return {"message": "Welcome to Amoura AI Service"}
