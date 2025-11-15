from fastapi import FastAPI
app = FastAPI(title="Gartenhandbuch")

@app.get("/")
def read_root():
    return {"message": "Du hast dein Gartenhandbuch geöffnet! "}
