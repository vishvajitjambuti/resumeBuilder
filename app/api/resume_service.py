import os
from typing import Optional

from services.JsonCreator import JsonCreator
from pdfCreator.texBuilder import TexBuilder
from pdfCreator.pdfBuilder import PDFBuilder
from pdfCreator.texBuilderEnglish import TexBuilderEnglish
from pdfCreator.texCoverLetter import CoverLetterTexBuilder


class ResumeService:
    def __init__(self):
        self.default_base_json_dir = r"C:\Users\vishv\Working_Dir\resumeBuilder\data"
        self.default_output_dir = r"C:\Users\vishv\Working_Dir\resumeBuilder\out_dir\NI"
        self.default_pdf_name = "Vishvajit_jambuti"

    def create_json(self, job_description: str, filename: str = "Vishvajit_jambuti_lebenslauf", base_json_dir: Optional[str] = None) -> dict:
        creator = JsonCreator(
            job_discription=job_description,
            base_json_dir=base_json_dir or self.default_base_json_dir,
        )
        creator.create_jason(filename=filename, job_description=job_description)
        return {"filename": filename, "base_json_dir": base_json_dir or self.default_base_json_dir}

    def create_json_without_agent(self, job_description: str, filename: str = "Vishvajit_jambuti_lebenslauf", base_json_dir: Optional[str] = None) -> dict:
        creator = JsonCreator(
            job_discription=job_description,
            base_json_dir=base_json_dir or self.default_base_json_dir,
        )
        creator.create_english_jason_witoutAgent(filename=filename, job_description=job_description)
        return {"filename": filename, "base_json_dir": base_json_dir or self.default_base_json_dir}

    def create_english_json(self, job_description: str, filename: str = "Vishvajit_jambuti_lebenslauf", base_json_dir: Optional[str] = None) -> dict:
        creator = JsonCreator(
            job_discription=job_description,
            base_json_dir=base_json_dir or self.default_base_json_dir,
        )
        creator.create_english_jason(filename=filename, job_description=job_description)
        return {"filename": filename, "base_json_dir": base_json_dir or self.default_base_json_dir}

    def translate_json(self, job_description: str, filename: str = "Vishvajit_jambuti_lebenslauf", base_json_dir: Optional[str] = None) -> dict:
        creator = JsonCreator(
            job_discription=job_description,
            base_json_dir=base_json_dir or self.default_base_json_dir,
        )
        creator.update_json_with_translated_result(filename=filename)
        return {"filename": filename, "base_json_dir": base_json_dir or self.default_base_json_dir}

    def create_pdf(self, job_description: Optional[str] = None, output_dir: Optional[str] = None, image_path: Optional[str] = None, pdf_name: Optional[str] = None, job_json_path: Optional[str] = None) -> dict:
        tex = TexBuilder(
            tex_dir=output_dir or self.default_output_dir,
            job_dis_path=job_json_path or os.path.join(self.default_base_json_dir, "Vishvajit_jambuti_lebenslauf.json"),
            img_path=image_path or None,
            pdf_name=pdf_name or self.default_pdf_name,
        )
        tex_file_path, file = tex.create_tex_file()
        pdf_builder = PDFBuilder(tex_dir=output_dir or self.default_output_dir, pdf_name=file)
        pdf_builder.render_to_pdf()
        return {"tex_file": tex_file_path, "pdf_name": file}

    def create_english_pdf(self, job_description: Optional[str] = None, output_dir: Optional[str] = None, image_path: Optional[str] = None, pdf_name: Optional[str] = None, job_json_path: Optional[str] = None) -> dict:
        tex = TexBuilderEnglish(
            tex_dir=output_dir or self.default_output_dir,
            job_dis_path=job_json_path or os.path.join(self.default_base_json_dir, "Vishvajit_jambuti_lebenslauf.json"),
            img_path=image_path or None,
            pdf_name=pdf_name or self.default_pdf_name,
        )
        tex_file_path, file = tex.create_tex_file()
        pdf_builder = PDFBuilder(tex_dir=output_dir or self.default_output_dir, pdf_name=file)
        pdf_builder.render_to_pdf()
        return {"tex_file": tex_file_path, "pdf_name": file}

    def create_cover_letter_pdf(self, job_description: Optional[str] = None, output_dir: Optional[str] = None, pdf_name: Optional[str] = None, job_json_path: Optional[str] = None) -> dict:
        tex = CoverLetterTexBuilder(
            tex_dir=output_dir or self.default_output_dir,
            job_dis_path=job_json_path or os.path.join(self.default_base_json_dir, "Vishvajit_jambuti_lebenslauf.json"),
            pdf_name=pdf_name or self.default_pdf_name,
        )
        tex_file_path, file = tex.create_tex_file()
        pdf_builder = PDFBuilder(tex_dir=output_dir or self.default_output_dir, pdf_name=file)
        pdf_builder.render_to_pdf()
        return {"tex_file": tex_file_path, "pdf_name": file}
