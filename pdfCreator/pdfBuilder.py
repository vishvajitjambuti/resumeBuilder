import os
import shutil
import subprocess
from typing import Optional


class PDFBuilder:
    def __init__(self, pdf_name: str, tex_dir: Optional[str] = None,  open_pdf: bool = False):
        self.pdf_name = pdf_name
        self.tex_dir = tex_dir or os.getcwd()
        self.open_pdf = open_pdf
    
    def render_to_pdf(self) -> str:
        """Render a .tex file to PDF using pdflatex via a temporary .bat file.

        Args:
            pdf_name: base name (without extension) of the tex file, e.g. 'resume'
            tex_dir: directory containing the .tex file (defaults to current working dir)
            open_pdf: if True, attempt to open the generated PDF (Windows only)

        Returns:
            Path to the generated PDF file.

        Raises:
            FileNotFoundError: if the .tex file does not exist.
            RuntimeError: if pdflatex is not available or the build fails.
        """
        work_dir = self.tex_dir or os.getcwd()
        tex_file = os.path.join(work_dir, f"{self.pdf_name}.tex")
        pdf_file = os.path.join(work_dir, f"{self.pdf_name}.pdf")

        if not os.path.exists(tex_file):
            raise FileNotFoundError(f"TeX file not found: {tex_file}")

        pdflatex_path = shutil.which('pdflatex')
        if pdflatex_path is None:
            raise RuntimeError('pdflatex not found in PATH. Please install a TeX distribution.')

        # Create a temporary batch file to run pdflatex twice
        bat_path = os.path.join(work_dir, 'generate_report.bat')
        run_command = f'@"{pdflatex_path}" -synctex=1 -interaction=nonstopmode "{os.path.basename(tex_file)}"'

        with open(bat_path, 'w', encoding='utf-8') as bat_file:
            bat_file.write('@ECHO OFF\n')
            bat_file.write(run_command + '\n')
            bat_file.write(run_command + '\n')

        # Execute the batch file
        try:
            subprocess.check_call([bat_path], cwd=work_dir)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f'pdflatex failed with exit code {e.returncode}')
        finally:
            try:
                os.remove(bat_path)
            except OSError:
                pass

        # Clean up auxiliary files commonly produced by LaTeX
        aux_exts = ['.aux', '.log', '.out', '.synctex.gz', '.toc']
        for ext in aux_exts:
            p = os.path.join(work_dir, f"{self.pdf_name}{ext}")
            try:
                if os.path.exists(p):
                    os.remove(p)
            except OSError:
                pass

        if not os.path.exists(pdf_file):
            raise RuntimeError('PDF was not generated.')

        if self.open_pdf and os.name == 'nt':
            try:
                os.startfile(pdf_file)
            except OSError:
                pass

        return pdf_file

    def render_to_pdf2(self) -> str:
        """
        Render a .tex file to PDF using XeLaTeX (required for fontspec).

        Returns:
            Path to the generated PDF file.

        Raises:
            FileNotFoundError: if the .tex file does not exist.
            RuntimeError: if xelatex fails.
        """
        work_dir = self.tex_dir or os.getcwd()
        tex_file = os.path.join(work_dir, f"{self.pdf_name}.tex")
        pdf_file = os.path.join(work_dir, f"{self.pdf_name}.pdf")

        if not os.path.exists(tex_file):
            raise FileNotFoundError(f"TeX file not found: {tex_file}")

        # Prefer xelatex (fontspec requires it)
        latex_engine = shutil.which("xelatex") or shutil.which("lualatex")
        if latex_engine is None:
            raise RuntimeError("xelatex or lualatex not found in PATH.")

        cmd = [
            latex_engine,
            "-synctex=1",
            "-interaction=nonstopmode",
            os.path.basename(tex_file)
        ]

        try:
            # Run twice for references
            subprocess.check_call(cmd, cwd=work_dir)
            subprocess.check_call(cmd, cwd=work_dir)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"LaTeX failed with exit code {e.returncode}")

        # Clean auxiliary files
        aux_exts = ['.aux', '.log', '.out', '.synctex.gz', '.toc']
        for ext in aux_exts:
            p = os.path.join(work_dir, f"{self.pdf_name}{ext}")
            if os.path.exists(p):
                try:
                    os.remove(p)
                except OSError:
                    pass

        if not os.path.exists(pdf_file):
            raise RuntimeError("PDF was not generated.")

        if self.open_pdf and os.name == "nt":
            try:
                os.startfile(pdf_file)
            except OSError:
                pass

        return pdf_file
