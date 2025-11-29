from fastapi import FastAPI

app = FastAPI(title="Intern-Ally Backend")


@app.get("/health")
def health_check():
    return {"status": "ok"}
