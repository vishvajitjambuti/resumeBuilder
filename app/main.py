from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

from app.api.resume_service import ResumeService

app = FastAPI(title="Resume Builder API", version="1.0.0")
service = ResumeService()


class JsonRequest(BaseModel):
    job_description: str = Field(..., min_length=1)
    filename: str = Field(default="Vishvajit_jambuti_lebenslauf")
    base_json_dir: Optional[str] = None


class PdfRequest(BaseModel):
    job_description: Optional[str] = None
    output_dir: Optional[str] = None
    image_path: Optional[str] = None
    pdf_name: Optional[str] = None
    job_json_path: Optional[str] = None


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/json")
def create_json(request: JsonRequest) -> dict:
    try:
        output = service.create_json(
            job_description=request.job_description,
            filename=request.filename,
            base_json_dir=request.base_json_dir,
        )
        return {"status": "success", "output": output}
    except Exception as exc:  # pragma: no cover - simple API error handling
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/json/no-agent")
def create_json_without_agent(request: JsonRequest) -> dict:
    try:
        output = service.create_json_without_agent(
            job_description=request.job_description,
            filename=request.filename,
            base_json_dir=request.base_json_dir,
        )
        return {"status": "success", "output": output}
    except Exception as exc:  # pragma: no cover - simple API error handling
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/json/english")
def create_english_json(request: JsonRequest) -> dict:
    try:
        output = service.create_english_json(
            job_description=request.job_description,
            filename=request.filename,
            base_json_dir=request.base_json_dir,
        )
        return {"status": "success", "output": output}
    except Exception as exc:  # pragma: no cover - simple API error handling
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/json/translate")
def translate_json(request: JsonRequest) -> dict:
    try:
        output = service.translate_json(
            job_description=request.job_description,
            filename=request.filename,
            base_json_dir=request.base_json_dir,
        )
        return {"status": "success", "output": output}
    except Exception as exc:  # pragma: no cover - simple API error handling
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/pdf")
def create_pdf(request: PdfRequest) -> dict:
    try:
        output = service.create_pdf(
            job_description=request.job_description,
            output_dir=request.output_dir,
            image_path=request.image_path,
            pdf_name=request.pdf_name,
            job_json_path=request.job_json_path,
        )
        return {"status": "success", "output": output}
    except Exception as exc:  # pragma: no cover - simple API error handling
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/pdf/english")
def create_english_pdf(request: PdfRequest) -> dict:
    try:
        output = service.create_english_pdf(
            job_description=request.job_description,
            output_dir=request.output_dir,
            image_path=request.image_path,
            pdf_name=request.pdf_name,
            job_json_path=request.job_json_path,
        )
        return {"status": "success", "output": output}
    except Exception as exc:  # pragma: no cover - simple API error handling
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/pdf/cover-letter")
def create_cover_letter_pdf(request: PdfRequest) -> dict:
    try:
        output = service.create_cover_letter_pdf(
            job_description=request.job_description,
            output_dir=request.output_dir,
            pdf_name=request.pdf_name,
            job_json_path=request.job_json_path,
        )
        return {"status": "success", "output": output}
    except Exception as exc:  # pragma: no cover - simple API error handling
        raise HTTPException(status_code=500, detail=str(exc)) from exc
