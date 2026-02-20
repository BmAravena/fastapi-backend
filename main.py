from fastapi import FastAPI
from routes import users


app = FastAPI(
    title="Users API",
    version="1.0.0"
)

app.include_router(users.router)


@app.get("/", tags=["first"])
def main_message():
    return {"Hello": "Welcome to the abys 999"}

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}