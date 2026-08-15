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
    QCheckBox,
)
from PyQt5.QtWidgets import QFrame
from services.JsonCreator import JsonCreator
from pdfCreator.texBuilder import TexBuilder
from pdfCreator.pdfBuilder import PDFBuilder
from GUI.guiStyleSheet import gui_style, tab_style, json_button_style, pdf_button_style
from GUI.guiHelper import guiHelper

DEFAULTS = {
    "file_name": "Vishvajit_jambuti_lebenslauf",
    "job_dis_path": r"C:\Users\vishv\Working_Dir\resumeBuilder\data\Vishvajit_jambuti_lebenslauf.json",
    "out_dir": r"C:\Users\vishv\Working_Dir\resumeBuilder\out_dir\NI",
    "img_path":  r"C:\Users\vishv\Working_Dir\resumeBuilder\out_dir\NI",
    "pdf_name": "Vishvajit_jambuti",
    "BASE_JSON_DIR": r"C:\Users\vishv\Working_Dir\resumeBuilder\data"
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
        
        self.english_json_button = QPushButton("Create Eng JSON")
        self.english_json_button.clicked.connect(self.run_json_english)
        self.english_json_button.setStyleSheet(json_button_style)
        
        
        self.translate_json_button = QPushButton("Translate to German")
        self.translate_json_button.clicked.connect(self.run_json_translate)
        self.translate_json_button.setStyleSheet(json_button_style)
        
        #layout.addWidget(self.json_button)

        self.pdf_button = QPushButton("Create PDF")
        self.pdf_button.setStyleSheet(pdf_button_style)
        self.pdf_button.clicked.connect(self.run_pdf)

        
        self.pdf_CoverLetter_button = QPushButton("CL PDF")
        self.pdf_CoverLetter_button.setStyleSheet(pdf_button_style)
        self.pdf_CoverLetter_button.clicked.connect(self.run_pdf_cover_letter)
        
        self.pdf_EnglishCV_button = QPushButton("CreateEnglishCVPDF")
        self.pdf_EnglishCV_button.setStyleSheet(pdf_button_style)
        self.pdf_EnglishCV_button.clicked.connect(self.run_pdf_EnglishCV)
        
        
        self.creat_json_withoutAgent =  QPushButton("No Agent Json")
        self.creat_json_withoutAgent.clicked.connect(self.run_json_no_agent)
        self.creat_json_withoutAgent.setStyleSheet(json_button_style)
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
        button_row.addWidget(self.creat_json_withoutAgent)
        
        button_row.addStretch()

        # button_row.addWidget(self.json_button)
        # button_row.addWidget(self.pdf_button)

        button_row.addStretch()



        layout.addLayout(button_row)
        button_row2 = QHBoxLayout()

       
        # ---- Tick mark checkboxes (True/False) ----
        self.job1_checkbox = QCheckBox("Job1")
        self.job1_checkbox.setChecked(self.job1_update_state)
        self.job1_checkbox.stateChanged.connect(lambda: self.toggle_job1())
 
        self.job2_checkbox = QCheckBox("workstudent")
        self.job2_checkbox.setChecked(self.job2_update_state)
        self.job2_checkbox.stateChanged.connect(lambda: self.toggle_job2())

        # ---- Action buttons ----
        self.german_cv_btnV2 = QPushButton("German CV")
        self.german_cv_btnV2.clicked.connect(self.run_pdf_DE2)
 
        self.english_cv_btnV2 = QPushButton("English CV")
        self.english_cv_btnV2.clicked.connect(self.run_pdf_ENV2)

        button_row2.addWidget(self.job1_checkbox)
        button_row2.addWidget(self.job2_checkbox)
        button_row2.addWidget(self.german_cv_btnV2)
        button_row2.addWidget(self.english_cv_btnV2)

        layout.addLayout(button_row2)
 


       

        
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