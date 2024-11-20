import os
import uuid
from datetime import datetime

from fastapi import FastAPI, UploadFile, Depends
from fastapi.responses import FileResponse

from sqlalchemy.orm import Session
from database import get_db, init_db
from models import File

app = FastAPI()
init_db()


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.post("/upload")
async def upload(file: UploadFile, db: Session = Depends(get_db)):
    id = str(uuid.uuid4())
    file_path = os.path.join(
        "uploads", f"{id}{os.path.splitext(file.filename)[1]}")

    file_content = await file.read()

    if not os.path.exists("uploads"):
        os.makedirs(os.path.dirname("uploads"))

    with open(file_path, "wb") as output_file:
        output_file.write(file_content)

    file_record = File(
        id=id,
        file_name=file.filename,
        file_size=file.size,
        file_path=file_path,
        created_at=datetime.now(),
        created_by="admin"
    )

    db.add(file_record)
    db.commit()
    db.refresh(file_record)

    return {"id": id}


@app.get("/download/{id}")
async def download(id: str, db: Session = Depends(get_db)):
    file_record = db.query(File).filter(File.id == id).first()
    return FileResponse(file_record.file_path)


@app.get("/all")
async def list_files(db: Session = Depends(get_db)):
    files = db.query(File).all()
    return files
