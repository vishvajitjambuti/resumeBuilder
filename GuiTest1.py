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
from PyQt5.QtWidgets import QFrame
from services.JsonCreator import JsonCreator
from pdfCreator.texBuilder import TexBuilder
from pdfCreator.pdfBuilder import PDFBuilder
from GUI.guiStyleSheet import gui_style, tab_style, json_button_style, pdf_button_style
from GUI.guiHelper import guiHelper

DEFAULTS = {
    "file_name": "Vishvajit_jambuti_lebenslauf",
    "job_dis_path": r"F:\Vishvajit work\Builder\data\Vishvajit_jambuti_lebenslauf.json",
    "out_dir": r"F:\Vishvajit work\Builder\out_dir\NI",
    "img_path":  r"F:\Vishvajit work\Builder\out_dir\NI",
    "pdf_name": "Vishvajit_jambuti",
    "BASE_JSON_DIR": r"F:\Vishvajit work\Builder\data"
}


class ResumeBuilderGUI(QWidget, guiHelper):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Resume Builder")
        self.resize(800, 600)
        self.console_text = ""
        self.current_view = "console"  # Track the current view (console or JSON)
        self.img_path = DEFAULTS["img_path"]
        self.pdf_name = DEFAULTS["pdf_name"]

        self.init_ui()

    def init_ui(self):

        layout = QVBoxLayout()

        # ------------------------------
        # JSON filename
        # ------------------------------
        layout.addWidget(QLabel("File Name"))

        #self.file_name = QLineEdit()
        
                
        self.file_name = QLineEdit(DEFAULTS["file_name"])
       

        #self.file_name = QLineEdit("bertrandt")
        self.file_name.setText(DEFAULTS["file_name"])
        self.file_name.textChanged.connect(self.update_json_path)
        self.file_name.setPlaceholderText("bertrandt")
        layout.addWidget(self.file_name)

        # ------------------------------
        # Job Description JSON Path
        # ------------------------------
        layout.addWidget(QLabel("Job Description JSON Path"))

        json_layout = QHBoxLayout()

        #self.job_dis_path = QLineEdit()
        self.job_dis_path = QLineEdit(DEFAULTS["job_dis_path"])

        json_btn = QPushButton("Browse")

        json_btn.clicked.connect(self.select_json)

        json_layout.addWidget(self.job_dis_path)
        json_layout.addWidget(json_btn)

        layout.addLayout(json_layout)

        # ------------------------------
        # Output Directory
        # ------------------------------
        layout.addWidget(QLabel("Output Directory"))

        out_layout = QHBoxLayout()

        #self.out_dir = QLineEdit()
        self.out_dir = QLineEdit(DEFAULTS["out_dir"])

        out_btn = QPushButton("Browse")

        out_btn.clicked.connect(self.select_output_dir)

        out_layout.addWidget(self.out_dir)
        out_layout.addWidget(out_btn)

        layout.addLayout(out_layout)

        # ------------------------------
        # Image Path
        # ------------------------------
        # layout.addWidget(QLabel("Image Path"))

        img_layout = QHBoxLayout()

        #self.img_path = QLineEdit()
        self.img_path = QLineEdit(DEFAULTS["img_path"])
        img_btn = QPushButton("Browse")

        img_btn.clicked.connect(self.select_image)

        img_layout.addWidget(self.img_path)
        img_layout.addWidget(img_btn)

        #layout.addLayout(img_layout)

        # ------------------------------
        # PDF Name
        # ------------------------------
        # layout.addWidget(QLabel("PDF Name"))

        # #self.pdf_name = QLineEdit()
        self.pdf_name = QLineEdit(DEFAULTS["pdf_name"])
        self.pdf_name.setPlaceholderText("Vishvajit_jambuti")

        #layout.addWidget(self.pdf_name)


        
        # ------------------------------
        # User Input
        # ------------------------------
        layout.addWidget(QLabel("Job Description /what we offer / what you bring to the table "))

        self.custom_input_job_description = QTextEdit()
        self.custom_input_job_description.setPlaceholderText(
            "Enter the job description here..."
        )
        self.custom_input_job_description.setMaximumHeight(250)

        layout.addWidget(self.custom_input_job_description)


        # ------------------------------
        # Buttons
        # ------------------------------
        button_row = QHBoxLayout()

        self.json_button = QPushButton("Create JSON")
        self.json_button.clicked.connect(self.run_json)
        self.json_button.setStyleSheet(json_button_style)
        
        self.english_json_button = QPushButton("Create English JSON")
        self.english_json_button.clicked.connect(self.run_json_english)
        self.english_json_button.setStyleSheet(json_button_style)
        
        
        self.translate_json_button = QPushButton("Translate JSON to German")
        self.translate_json_button.clicked.connect(self.run_json_translate)
        self.translate_json_button.setStyleSheet(json_button_style)
        
        #layout.addWidget(self.json_button)

        self.pdf_button = QPushButton("Create PDF")
        self.pdf_button.setStyleSheet(pdf_button_style)
        self.pdf_button.clicked.connect(self.run_pdf)

        
        self.pdf_CoverLetter_button = QPushButton("CreateCoverLetterPDF")
        self.pdf_CoverLetter_button.setStyleSheet(pdf_button_style)
        self.pdf_CoverLetter_button.clicked.connect(self.run_pdf_cover_letter)
        
        self.pdf_EnglishCV_button = QPushButton("CreateEnglishCVPDF")
        self.pdf_EnglishCV_button.setStyleSheet(pdf_button_style)
        self.pdf_EnglishCV_button.clicked.connect(self.run_pdf_EnglishCV)
        # disabled initially
        #self.pdf_button.setEnabled(False)

        #layout.addWidget(self.pdf_button)
        # ================================
        # button_row.addWidget(self.json_button)
        
        button_row.addWidget(self.english_json_button)
        button_row.addWidget(self.translate_json_button)
        button_row.addWidget(self.pdf_button)
        button_row.addWidget(self.pdf_CoverLetter_button)
        button_row.addWidget(self.pdf_EnglishCV_button)
        
        button_row.addStretch()

        # button_row.addWidget(self.json_button)
        # button_row.addWidget(self.pdf_button)

        button_row.addStretch()



        layout.addLayout(button_row)


        # ------------------------------
        # Console Output
        # ------------------------------

        # layout.addWidget(QLabel("Console Output"))

        # self.console = QTextEdit()
        # self.console.setReadOnly(True)

        # layout.addWidget(self.console)

        # self.setLayout(layout)


        
        # ------------------------------
        # Viewer Section
        # ------------------------------

        button_layout = QHBoxLayout()

        self.console_view_btn = QPushButton("Console Output")
        #self.console_view_btn.setStyleSheet(tab_style)
        self.console_view_btn.clicked.connect(self.show_console)

        self.json_view_btn = QPushButton("View Created JSON")
        #self.json_view_btn.setStyleSheet(tab_style)
        self.json_view_btn.clicked.connect(self.show_json_file)
        


        button_layout.addWidget(self.console_view_btn)
        button_layout.addWidget(self.json_view_btn)

        layout.addLayout(button_layout)
        # ====================================================
        #  Edit and save buttons
        # ====================================================
        self.edit_json_btn = QPushButton("Edit JSON")
        self.save_json_btn = QPushButton("Save JSON")
        
        self.edit_json_btn.clicked.connect(self.enable_json_edit)
        self.save_json_btn.clicked.connect(self.save_edited_json)
        # hide initially
        self.save_json_btn.hide()
        self.edit_json_btn.hide()
        edit_layout = QHBoxLayout()
        edit_layout.addWidget(self.edit_json_btn)
        edit_layout.addWidget(self.save_json_btn)
        layout.addLayout(edit_layout) 
        # ===================================================       

        # Common Viewer
        self.viewer = QTextEdit()
        self.viewer.setReadOnly(True)

        layout.addWidget(self.viewer)
        self.setLayout(layout)


    # ====================================================
    # File Browsers
    # ====================================================

    # def select_json(self):
    #     path, _ = QFileDialog.getOpenFileName(
    #         self,
    #         "Select JSON File",
    #         "",
    #         "JSON Files (*.json)"
    #     )

    #     if path:
    #         self.job_dis_path.setText(path)

    # def select_output_dir(self):
    #     path = QFileDialog.getExistingDirectory(
    #         self,
    #         "Select Output Directory"
    #     )

    #     if path:
    #         self.out_dir.setText(path)

    # def select_image(self):
    #     path, _ = QFileDialog.getOpenFileName(
    #         self,
    #         "Select Image",
    #         "",
    #         "Images (*.png *.jpg *.jpeg)"
    #     )

    #     if path:
    #         self.img_path.setText(path)

    # # ====================================================
    # # Helper
    # # ====================================================

    # def log(self, text):
    #     self.console_text += text + "\n"
    #     self.viewer.setPlainText(self.console_text)


    # # ====================================================
    # # JSON Function
    # # ====================================================


    
    # def run_json(self):

        
    #     custom_text_JD = self.custom_input_job_description.toPlainText().strip()

    #     # Store for later use
    #     self.user_prompt_JD = custom_text_JD

    #     self.log(f"User Input:\n{self.user_prompt_JD}\n")


    #     self.json_button.setText("Processing...")
    #     self.json_button.setEnabled(False)

    #     QApplication.processEvents()

    #     output_buffer = io.StringIO()

    #     try:

    #         with redirect_stdout(output_buffer):

    #             jason_creator = JsonCreator()

    #             jason_creator.create_jason(
    #                 filename=self.file_name.text().strip(),
    #                 job_description=self.user_prompt_JD
    #             )

    #         self.console_text += output_buffer.getvalue()
    #         self.show_console()

    #         self.log("✅ JSON Creation Complete")

    #         QMessageBox.information(
    #             self,
    #             "Success",
    #             "JSON file created successfully."
    #         )

    #     except Exception as e:

    #         self.log(f"❌ ERROR: {str(e)}")

    #         QMessageBox.critical(
    #             self,
    #             "Error",
    #             str(e)
    #         )

    #     finally:

    #         self.json_button.setText("Create JSON")
    #         self.json_button.setEnabled(True)


    # # ====================================================
    # # PDF Function
    # # ====================================================

    
    # def run_pdf(self):

    #     self.pdf_button.setText("Processing...")
    #     self.pdf_button.setEnabled(False)

    #     QApplication.processEvents()

    #     output_buffer = io.StringIO()

    #     try:

    #         with redirect_stdout(output_buffer):

    #             tex = TexBuilder(
    #                 tex_dir=self.out_dir.text().strip(),
    #                 job_dis_path=self.job_dis_path.text().strip(),
    #                 img_path=self.img_path.text().strip() or None,
    #                 pdf_name=self.pdf_name.text().strip(),
    #             )

    #             tex_file_path, file = tex.create_tex_file()

    #             print(f"TEX FILE: {tex_file_path}")

    #             pdf_builder = PDFBuilder(
    #                 tex_dir=self.out_dir.text().strip(),
    #                 pdf_name=file,
    #             )

    #             pdf_builder.render_to_pdf()

    #         self.console_text += output_buffer.getvalue()
    #         self.show_console()

    #         self.log("✅ PDF Creation Complete")

    #         QMessageBox.information(
    #             self,
    #             "Success",
    #             "PDF created successfully."
    #         )

    #     except Exception as e:

    #         self.log(f"❌ ERROR: {str(e)}")

    #         QMessageBox.critical(
    #             self,
    #             "Error",
    #             str(e)
    #         )

    #     finally:

    #         self.pdf_button.setText("Create PDF")
    #         self.pdf_button.setEnabled(True)


    # def show_console(self):
    #     self.viewer.setPlainText(self.console_text)


    # def show_json_file(self):

    #     try:

    #         json_path = self.job_dis_path.text().strip()

    #         with open(json_path, "r", encoding="utf-8") as f:
    #             data = json.load(f)

    #         self.viewer.setPlainText(
    #             json.dumps(
    #                 data,
    #                 indent=4,
    #                 ensure_ascii=False
    #             )
    #         )

    #     except Exception as e:

    #         self.viewer.setPlainText(
    #             f"Unable to load JSON file\n\n{str(e)}"
    #         )

        
    # def update_json_path(self):

    #     file_name = self.file_name.text().strip()

    #     if file_name:
    #         json_path = os.path.join(DEFAULTS["BASE_JSON_DIR"], f"{file_name}.json")
    #         self.job_dis_path.setText(json_path)

        

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyleSheet(gui_style)  # Apply the stylesheet to the application
                

    window = ResumeBuilderGUI()
    window.show()
    
    input_frame = QFrame()
    input_frame.setStyleSheet("""
            QFrame {
                background: white;
                border: 1px solid #d0d0d0;
                border-radius: 12px;
            }
            """)


    sys.exit(app.exec_())