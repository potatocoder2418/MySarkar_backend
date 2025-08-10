from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth
from app.core.config import settings

app = FastAPI()

# Add CORS middleware with explicit configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://hackodisha.vercel.app", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
    expose_headers=["*"],
    max_age=600  # Cache preflight request for 10 minutes
)

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Auth API is running"}
