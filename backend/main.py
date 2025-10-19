from fastapi import FastAPI
import uvicorn
from api.routes import router as api_router

app = FastAPI(title="SERVER")

app.include_router(api_router, prefix="/api", tags=["api"])

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
