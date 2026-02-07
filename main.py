from fastapi import FastAPI
from routes import users


app = FastAPI(
    title="Users API",
    version="1.0.0"
)

app.include_router(users.router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}