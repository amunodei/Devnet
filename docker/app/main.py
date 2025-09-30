from fastapi import FastAPI

app = FastAPI(title="NetAuto API")

@app.get("/")
async def root():
    return {"message": "Welcome to NetAuto"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}