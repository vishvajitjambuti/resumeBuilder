from services.JsonCreator import JsonCreator
from pdfCreator.texBuilder import TexBuilder
from pdfCreator.pdfBuilder import PDFBuilder
jD = """Your tasks:
Identification, analysis and evaluation of automation potential with a focus on savings and efficiency gains
Conception, development and implementation of AI-supported workflows and automation solutions
Purchasing & Order Management: Automation of purchase requisitions, order processing, and email distribution
Engineering: Support and automation of life-cycle applications and technical change processes
Order management: Optimization of offer processing, order communication and status tracking
QM: Maintenance/automation of forms, compliance with ISO standards, support during audits
HR processes: Digitization of personnel administration processes (onboarding/offboarding, vacation requests, time tracking)
Integration of AI services (ChatGPT, Claude) into existing business processes and system landscape
Integration/orchestration of the system landscape (SAP ECC6 EHP8, Microsoft 365, n8n, in-house solutions)


Your profile:
Completed vocational training or studies in the field of IT, business informatics, business administration with a focus on IT, or similar.
Experience in process analysis and optimization, ideally in a manufacturing company
Knowledge in the field of Artificial Intelligence (LLMs, Prompt Engineering, AI-supported automation)
Practical experience with workflow/automation platforms (e.g., n8n, Power Automaten, or similar)
Basic knowledge of SAP ECC6 and/or willingness to learn SAP processes
Safe handling of Microsoft 365 (SharePoint, Teams, Power Platform)
Understanding of business processes in the areas of purchasing, engineering, quality management, order management and HR
Experience with API integrations and data flow concepts (REST, JSON, Webhooks)
Basic programming skills (e.g., Python, JavaScript) are an advantage.
Analytical thinking, structured work methods, and high self-motivation
Strong communication skills – ability to explain technical solutions clearly to specialist departments and external partners
Willingness to continuously develop oneself in the field of AI and automation
Teamwork skills, organizational talent and the ability to work independently"""


def jason():

    jason_creator = JsonCreator()
    
    
    jason_creator.create_jason(filename = 'bertrandt_v2', job_description = jD)

def pdf():
    job_dis_path = r"C:\Users\jambutiv\WorkingDir\AI_crash_course\rb\Builder\data\bertrandt.json"
    tex_dir = r"C:\Users\jambutiv\WorkingDir\AI_crash_course\rb\Builder\out_dir\NI"
    tex = TexBuilder(tex_dir=tex_dir, job_dis_path=job_dis_path, img_path = None, pdf_name = "Vishvajit_jambuti")
    tex_file_path , file = tex.create_tex_file()
    print(tex_file_path)
    pdf = PDFBuilder(tex_dir= tex_dir, pdf_name=file, )
    pdf = pdf.render_to_pdf()

jason()

#pdf()
