from fastapi import FastAPI

app = FastAPI()

from fastapi import UploadFile
import shutil

@app.post("/upload")

async def upload_pdf(
        file: UploadFile):

    path = f"uploads/{file.filename}"

    with open(path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "message":
        "PDF uploaded"
    }

    @app.post("/process")
async def process():

    text = read_pdf(
        "uploads/policy.pdf"
    )

    chunks = chunk_text(text)

    embeddings = (
        generate_embeddings(
            chunks
        )
    )

    store_chunks(
        chunks,
        embeddings
    )

    return {
        "message":
        "Document Indexed"
    }

from pydantic import BaseModel

class Question(BaseModel):

    question: str

@app.post("/ask")

async def ask(
        request: Question):

    docs = search_documents(
        request.question
    )

    context = "\n".join(docs)

    answer = generate_answer(
        request.question,
        context
    )

    return {
        "answer": answer
    }