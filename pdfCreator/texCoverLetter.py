import os
from typing import Optional
import json
from pdfCreator.template.coverLetterTemplate import template

class CoverLetterTexBuilder:
    def __init__(self, tex_dir: str, job_dis_path: str, pdf_name="Vishvajit_jambuti_cover_letter"):
        self.pdf_name = pdf_name
        self.tex_dir = tex_dir
        self.job_dis_path = job_dis_path
       
        
    def create_tex_file(self) -> str:
        """Create a .tex file named `{pdf_name}.tex` inside `tex_dir` using the template.

        Returns:
            Full path to the created .tex file.
        """
        with open(self.job_dis_path, 'r', encoding='utf-8') as f:
            job_details = json.load(f)
        #filename should be name of json file 
        parsed_job_details =  job_details.get("result_german", {})
        file_name = os.path.splitext(os.path.basename(self.job_dis_path))[0].replace("_lebenslauf", "")
        filename = file_name + '_CoverLetter.tex'
        file = os.path.splitext(filename)[0]
        print('file_name:', filename)
        print('file', file)
        
        if not self.tex_dir:
            raise ValueError('tex_dir is required and must be a directory path')
        work_dir = self.tex_dir
        
         
        tex_path = os.path.join(work_dir, filename)
        
        first_parapraph = parsed_job_details.get("cover_letter_first_german", "")
        last_paragraph = parsed_job_details.get("cover_letter_last_german", "")
        
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

        content = tpl.replace('___FIRST_PARAGRAPH__', first_parapraph)
        content = content.replace('__LAST_PARAGRAPH__', last_paragraph)
        
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(content)

        
        print('.tex file created at:', tex_path)
        return tex_path, file 