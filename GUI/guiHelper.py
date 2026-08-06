from services.JsonCreator import JsonCreator
from pdfCreator.texBuilder import TexBuilder
from pdfCreator.pdfBuilder import PDFBuilder
from pdfCreator.texBuilderEnglish import TexBuilderEnglish
from pdfCreator.texCoverLetter import CoverLetterTexBuilder
from pdfCreator.texBuilderV2 import TexBuilder as TexBuilderV2
from pdfCreator.template.englishResumeTemplateV2 import template as english_templateV2
from pdfCreator.template.germanResumeTemplateV2 import template as german_templateV2
from pdfCreator.template.Template2 import template as german_templateV1
import sys
import io
from contextlib import redirect_stdout
import json
import os
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
)

DEFAULTS = {
    "file_name": "Vishvajit_jambuti_lebenslauf",
    "job_dis_path": r"C:\Users\vishv\Working_Dir\resumeBuilder\data\Vishvajit_jambuti_lebenslauf.json",
    "out_dir": r"C:\Users\vishv\Working_Dir\resumeBuilder\out_dir\NI",
    "img_path":  r"C:\Users\vishv\Working_Dir\resumeBuilder\out_dir\NI",
    "pdf_name": "Vishvajit_jambuti",
    "BASE_JSON_DIR": r"C:\Users\vishv\Working_Dir\resumeBuilder\data"
}

class Tee:
    def __init__(self, *streams):
        self.streams = streams
    def write(self, data):
        for stream in self.streams:
            stream.write(data)
            stream.flush()
    def flush(self):
        for stream in self.streams:
            stream.flush()

class guiHelper:
    def __init__(self):
        self.job1_update_state = False
        self.job2_update_state = False

    def select_json(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select JSON File",
            "",
            "JSON Files (*.json)"
        )

        if path:
            self.job_dis_path.setText(path)

    def select_output_dir(self):
        path = QFileDialog.getExistingDirectory(
            self,
            "Select Output Directory"
        )

        if path:
            self.out_dir.setText(path)

    def select_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Images (*.png *.jpg *.jpeg)"
        )

        if path:
            self.img_path.setText(path)

    # ====================================================
    # Helper
    # ====================================================

    def log(self, text):
        self.console_text += text + "\n"
        if self.current_view == "console":
            self.viewer.setPlainText(self.console_text)


    # ====================================================
    # JSON Function
    # ====================================================


    
    def run_json(self):
        custom_text_JD = self.custom_input_job_description.toPlainText().strip()

        # Store for later use
        self.user_prompt_JD = custom_text_JD

        self.log(f"User Input:\n{self.user_prompt_JD}\n")


        self.json_button.setText("Processing...")
        self.json_button.setEnabled(False)

        QApplication.processEvents()

        output_buffer = io.StringIO()
        tee = Tee(sys.stdout, output_buffer) 
        

        try:

            with redirect_stdout(tee):

                jason_creator = JsonCreator(job_discription=self.user_prompt_JD,base_json_dir=DEFAULTS["BASE_JSON_DIR"] )

                jason_creator.create_jason(
                    filename=self.file_name.text().strip(),
                    job_description=self.user_prompt_JD
                )

            self.console_text += output_buffer.getvalue()
            self.show_console()

            self.log("✅ JSON Creation Complete")

            QMessageBox.information(
                self,
                "Success",
                "JSON file created successfully."
            )

        except Exception as e:

            self.log(f"❌ ERROR: {str(e)}")

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

        finally:

            self.json_button.setText("Create JSON")
            self.json_button.setEnabled(True)
    
    def run_json_no_agent(self):
        custom_text_JD = self.custom_input_job_description.toPlainText().strip()

        # Store for later use
        self.user_prompt_JD = custom_text_JD

        self.log(f"User Input:\n{self.user_prompt_JD}\n")


        self.creat_json_withoutAgent.setText("Processing...")
        self.creat_json_withoutAgent.setEnabled(False)

        QApplication.processEvents()

        output_buffer = io.StringIO()
        tee = Tee(sys.stdout, output_buffer) 
        

        try:

            with redirect_stdout(tee):

                jason_creator = JsonCreator(job_discription=self.user_prompt_JD, base_json_dir=DEFAULTS["BASE_JSON_DIR"])

                jason_creator.create_english_jason_witoutAgent(
                    filename=self.file_name.text().strip(),
                    job_description=self.user_prompt_JD
                )

            self.console_text += output_buffer.getvalue()
            self.show_console()

            self.log("✅ JSON Creation Complete")

            QMessageBox.information(
                self,
                "Success",
                "JSON file created successfully."
            )

        except Exception as e:

            self.log(f"❌ ERROR: {str(e)}")

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

        finally:

            self.creat_json_withoutAgent.setText("No Agent Json ")
            self.creat_json_withoutAgent.setEnabled(True)
            
    def run_json_english(self):
        custom_text_JD = self.custom_input_job_description.toPlainText().strip()

        # Store for later use
        self.user_prompt_JD = custom_text_JD

        self.log(f"User Input:\n{self.user_prompt_JD}\n")


        self.english_json_button.setText("Processing...")
        self.english_json_button.setEnabled(False)

        QApplication.processEvents()

        output_buffer = io.StringIO()
        tee = Tee(sys.stdout, output_buffer) 

        try:

            with redirect_stdout(tee):

                jason_creator = JsonCreator(base_json_dir=DEFAULTS["BASE_JSON_DIR"], job_discription=self.user_prompt_JD)

                jason_creator.create_english_jason(
                    filename=self.file_name.text().strip(),
                    job_description=self.user_prompt_JD
                )

            self.console_text += output_buffer.getvalue()
            self.show_console()

            self.log("✅ JSON Creation Complete")

            QMessageBox.information(
                self,
                "Success",
                "JSON file created successfully."
            )

        except Exception as e:

            self.log(f"❌ ERROR: {str(e)}")

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

        finally:

            self.english_json_button.setText("Create JSON")
            self.english_json_button.setEnabled(True)
    
    def run_json_translate(self):
        custom_text_JD = self.custom_input_job_description.toPlainText().strip()

        # Store for later use
        self.user_prompt_JD = custom_text_JD

        self.log(f"User Input:\n{self.user_prompt_JD}\n")


        self.translate_json_button.setText("Processing...")
        self.translate_json_button.setEnabled(False)

        QApplication.processEvents()

        output_buffer = io.StringIO()
        tee = Tee(sys.stdout, output_buffer) 

        try:

            with redirect_stdout(tee):

                jason_creator = JsonCreator(base_json_dir=DEFAULTS["BASE_JSON_DIR"], job_discription=self.user_prompt_JD)

                jason_creator.update_json_with_translated_result(
                    filename=self.file_name.text().strip()
                )

            self.console_text += output_buffer.getvalue()
            self.show_console()

            self.log("✅ JSON Creation Complete")

            QMessageBox.information(
                self,
                "Success",
                "JSON file created successfully."
            )

        except Exception as e:

            self.log(f"❌ ERROR: {str(e)}")

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

        finally:

            self.translate_json_button.setText("Translate JSON to German")
            self.translate_json_button.setEnabled(True)




    # ====================================================
    # PDF Function
    # ====================================================

    
    def run_pdf(self):

        self.pdf_button.setText("Processing...")
        self.pdf_button.setEnabled(False)

        QApplication.processEvents()

        output_buffer = io.StringIO()
        tee = Tee(sys.stdout, output_buffer)

        try:

            with redirect_stdout(tee):

                tex = TexBuilder(
                    tex_dir=self.out_dir.text().strip(),
                    job_dis_path=self.job_dis_path.text().strip(),
                    img_path=self.img_path.text().strip() or None,
                    pdf_name=self.pdf_name.text().strip(),
                )

                tex_file_path, file = tex.create_tex_file()

                print(f"TEX FILE: {tex_file_path}")

                pdf_builder = PDFBuilder(
                    tex_dir=self.out_dir.text().strip(),
                    pdf_name=file,
                )

                pdf_builder.render_to_pdf()

            self.console_text += output_buffer.getvalue()
            self.show_console()

            self.log("✅ PDF Creation Complete")

            QMessageBox.information(
                self,
                "Success",
                "PDF created successfully."
            )

        except Exception as e:

            self.log(f"❌ ERROR: {str(e)}")

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

        finally:

            self.pdf_button.setText("Create PDF")
            self.pdf_button.setEnabled(True)
    
    def run_pdf_EnglishCV(self):

        self.pdf_EnglishCV_button.setText("Processing...")
        self.pdf_EnglishCV_button.setEnabled(False)

        QApplication.processEvents()

        output_buffer = io.StringIO()
        tee = Tee(sys.stdout, output_buffer)

        try:

            with redirect_stdout(tee):

                tex = TexBuilderEnglish(
                    tex_dir=self.out_dir.text().strip(),
                    job_dis_path=self.job_dis_path.text().strip(),
                    img_path=self.img_path.text().strip() or None,
                    pdf_name=self.pdf_name.text().strip(),
                )

                tex_file_path, file = tex.create_tex_file()

                print(f"TEX FILE: {tex_file_path}")

                pdf_builder = PDFBuilder(
                    tex_dir=self.out_dir.text().strip(),
                    pdf_name=file,
                )

                pdf_builder.render_to_pdf()

            self.console_text += output_buffer.getvalue()
            self.show_console()

            self.log("✅ PDF Creation Complete")

            QMessageBox.information(
                self,
                "Success",
                "PDF created successfully."
            )

        except Exception as e:

            self.log(f"❌ ERROR: {str(e)}")

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

        finally:

            self.pdf_EnglishCV_button.setText("Create English CV PDF")
            self.pdf_EnglishCV_button.setEnabled(True)

    
    # ====================================================
    # Cover letter Function
    # ====================================================   
    
    def run_pdf_cover_letter(self):

        self.pdf_CoverLetter_button.setText("Processing...")
        self.pdf_CoverLetter_button.setEnabled(False)

        QApplication.processEvents()

        output_buffer = io.StringIO()
        tee = Tee(sys.stdout, output_buffer)
        try:

            with redirect_stdout(tee):

                tex = CoverLetterTexBuilder(
                    tex_dir=self.out_dir.text().strip(),
                    job_dis_path=self.job_dis_path.text().strip(),
                    pdf_name=self.pdf_name.text().strip(),
                )

                tex_file_path, file = tex.create_tex_file()

                print(f"TEX FILE: {tex_file_path}")

                pdf_builder = PDFBuilder(
                    tex_dir=self.out_dir.text().strip(),
                    pdf_name=file,
                )

                pdf_builder.render_to_pdf()

            self.console_text += output_buffer.getvalue()
            self.show_console()

            self.log("✅ PDF Creation Complete cover letter")

            QMessageBox.information(
                self,
                "Success",
                "PDF created successfully."
            )

        except Exception as e:

            self.log(f"❌ ERROR: {str(e)}")

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

        finally:

            self.pdf_CoverLetter_button.setText("Create Cover Letter PDF")
            self.pdf_CoverLetter_button.setEnabled(True)
    

    def show_console(self):
        self.current_view = "console"
        self.viewer.setPlainText(self.console_text)
        # hide json controls when showing console
        self.edit_json_btn.hide()
        self.save_json_btn.hide()
        
        self.viewer.setReadOnly(True)

    def enable_json_edit(self):
        self.viewer.setReadOnly(False)
        print(self.viewer.toPlainText())
    
    def save_edited_json(self):
        try:
            json_path = self.job_dis_path.text().strip()
            text = self.viewer.toPlainText()

            data = json.loads(text)
            with open( json_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            
            QMessageBox.information(
                self,   
                "Success",
                "JSON file saved successfully."
            )
            self.viewer.setReadOnly(True)
            
        except json.JSONDecodeError as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Invalid JSON format: {str(e)}"
            )
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Unable to save JSON file: {str(e)}"
            )

            

        
    def show_json_file(self):
        self.current_view = "json"

        try:

            json_path = self.job_dis_path.text().strip()

            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.viewer.setPlainText(
                json.dumps(
                    data,
                    indent=4,
                    ensure_ascii=False
                )
            )
            self.edit_json_btn.show()
            self.save_json_btn.show()
            
            self.viewer.setReadOnly(True)

        except Exception as e:

            self.viewer.setPlainText(
                f"Unable to load JSON file\n\n{str(e)}"
            )

        
    def update_json_path(self):

        file_name = self.file_name.text().strip()

        if file_name:
            json_path = os.path.join(DEFAULTS["BASE_JSON_DIR"], f"{file_name}.json")
            self.job_dis_path.setText(json_path)

    def toggle_job1(self):
        self.job1_update_state = self.job1_checkbox.isChecked()  # updates the variable (True/False)
        #self.status_label.setText(f"Job1 toggled to {self.job1_state}")
        print(f"job1_state = {self.job1_update_state}")
 
    def toggle_job2(self):
        self.job2_state = self.job2_checkbox.isChecked()  # updates the variable (True/False)
        #self.status_label.setText(f"Job2 toggled to {self.job2_state}")
        print(f"job2_state = {self.job2_state}")

    def run_pdf_ENV2(self):
    
            self.pdf_button.setText("Processing...")
            self.pdf_button.setEnabled(False)
    
            QApplication.processEvents()
    
            output_buffer = io.StringIO()
            tee = Tee(sys.stdout, output_buffer)
    
            try:
    
                with redirect_stdout(tee):
    
                    tex = TexBuilderV2(
                        tex_dir=self.out_dir.text().strip(),
                        job_dis_path=self.job_dis_path.text().strip(),
                        template=english_templateV2, 
                        keywords=True, 
                        english=True,
                        job1=self.job1_update_state, 
                        job2=self.job1_update_state
                    )
    
                    tex_file_path, file = tex.create_tex_file()
    
                    print(f"TEX FILE: {tex_file_path}")
    
                    pdf_builder = PDFBuilder(
                        tex_dir=self.out_dir.text().strip(),
                        pdf_name=file,
                    )
    
                    pdf_builder.render_to_pdf2()
    
                self.console_text += output_buffer.getvalue()
                self.show_console()
    
                self.log("✅ PDF Creation Complete")
    
                QMessageBox.information(
                    self,
                    "Success",
                    "PDF created successfully."
                )
    
            except Exception as e:
    
                self.log(f"❌ ERROR: {str(e)}")
    
                QMessageBox.critical(
                    self,
                    "Error",
                    str(e)
                )
    
            finally:
    
                self.pdf_button.setText("Create PDF")
                self.pdf_button.setEnabled(True)

    def run_pdf_DE2(self):
        
                self.pdf_button.setText("Processing...")
                self.pdf_button.setEnabled(False)
        
                QApplication.processEvents()
        
                output_buffer = io.StringIO()
                tee = Tee(sys.stdout, output_buffer)
        
                try:
        
                    with redirect_stdout(tee):
        
                        tex = TexBuilderV2(
                            tex_dir=self.out_dir.text().strip(),
                            job_dis_path=self.job_dis_path.text().strip(),
                            template=german_templateV2,
                            keywords=True, 
                            english=False,
                            job1=self.job1_update_state, 
                            job2=self.job1_update_state
                        )
        
                        tex_file_path, file = tex.create_tex_file()
        
                        print(f"TEX FILE: {tex_file_path}")
        
                        pdf_builder = PDFBuilder(
                            tex_dir=self.out_dir.text().strip(),
                            pdf_name=file,
                        )
        
                        pdf_builder.render_to_pdf2()
        
                    self.console_text += output_buffer.getvalue()
                    self.show_console()
        
                    self.log("✅ PDF Creation Complete")
        
                    QMessageBox.information(
                        self,
                        "Success",
                        "PDF created successfully."
                    )
        
                except Exception as e:
        
                    self.log(f"❌ ERROR: {str(e)}")
        
                    QMessageBox.critical(
                        self,
                        "Error",
                        str(e)
                    )
        
                finally:
        
                    self.pdf_button.setText("Create PDF")
                    self.pdf_button.setEnabled(True)