import os
from typing import Optional
import json
from pdfCreator.template.Template2 import template

class TexBuilder:
    def __init__(self,  tex_dir: str, job_dis_path: str, img_path : str = None,  pdf_name = "Vishvajit_jambuti" ):
        self.pdf_name = pdf_name
        self.tex_dir = tex_dir
        self.job_dis_path = job_dis_path
        self.img_path = img_path
        self.image_path = os.path.normpath(r"C:\Users\vishv\Working_Dir\resumeBuilder\vish.png").replace('\\', '/')

    def create_tex_file(self) -> str:
        """Create a .tex file named `{pdf_name}.tex` inside `tex_dir` using the template.

        Returns:
            Full path to the created .tex file.
        """
        with open(self.job_dis_path, 'r', encoding='utf-8') as f:
            job_details = json.load(f)
        #filename should be name of json file 
        parsed_job_details =  job_details.get("result_german", {})
        parsed_job_details_english =  job_details.get("result_english", {})
        filename = os.path.splitext(os.path.basename(self.job_dis_path))[0] + '.tex'
        file = os.path.splitext(os.path.basename(self.job_dis_path))[0]

        if not self.tex_dir:
            raise ValueError('tex_dir is required and must be a directory path')
        work_dir = self.tex_dir
        os.makedirs(work_dir, exist_ok=True)
        tex_path = os.path.join(work_dir, filename)

        job1 = parsed_job_details.get("Job_1_suggested_german", [])
        job2 = parsed_job_details.get("Job_2_suggested_german", [])
        profile_details = parsed_job_details.get("about_me_german", "")
        keywords = parsed_job_details_english.get("keywords", [])

        job1_str = self.job_details_to_latex(job1)
        job2_str = self.job_details_to_latex(job2)
        keywords_str = self.keywords_to_latex(keywords)

        if template is None:
        # look for a template.tex in workspace or same directory
            fallback_paths = [os.path.join(os.getcwd(), 'template.tex'), os.path.join(os.path.dirname(__file__), 'template.tex')]
            loaded = False
            for p in fallback_paths:
                if os.path.exists(p):
                    with open(p, 'r', encoding='utf-8') as tf:
                        tpl = tf.read()
                    loaded = True
                    break
            if not loaded:
                    raise FileNotFoundError('No template found: cannot import template_1 and no template.tex present')
        else:
            tpl = template

        # Build content from template and replace placeholders
        content = tpl.replace('__IMAGE_PATH__', self.image_path)
        content = content.replace('__PROFILE_DETAILS__', profile_details)
        # content = content.replace('__NAME__', name)
        content = content.replace('__JOB_1_DETAILS__', job1_str)
        content = content.replace('__JOB_2_DETAILS__', job2_str)
        content = content.replace('__KEYWORDS__', keywords_str)
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(content)

        
        print('.tex file created at:', tex_path)
        return tex_path, file 


    def job_details_to_latex(self, items):
        latex = "\\begin{itemize}\n"
        for item in items:
            latex += f"    \\item {item}\n"
        latex += "\\end{itemize}\n"
        return latex

    def keywords_to_latex(self, keywords):
        #  \textcolor{cvblue!90} {Python, C++, TypeScript,  Matlab, Git FastAPI, React, Vector CANoe, Capl}
        latex = "\\textcolor{cvblue!90} {"
        latex += ", ".join(keywords)
        latex += "}"
        return latex