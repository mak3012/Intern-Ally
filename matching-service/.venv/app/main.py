from fastapi import FastAPI

app = FastAPI(title="Intern-Ally Matching Service")


@app.get("/health")
def health_check():
    return {"status": "ok"}
