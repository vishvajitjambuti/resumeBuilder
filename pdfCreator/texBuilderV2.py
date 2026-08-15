import os
from typing import Optional
import json
#from pdfCreator.template.Template2 import template
JOB1 = r"""\begin{itemize}
\item Design and implement test scenarios for DMS ECU validation to meet KPIs and functional requirements
\item Develop Python/Bash automation scripts to process data, generate KPIs, and optimize test workflows across multiple test benches and CI pipelines
\item Develop automated test case generation tools by integrating Agents, LLMs, RAG, and vector databases to accelerate validation process by using LangChain and LangGraph
\item Create FastAPI backend services and React-based web components for system testing and integration in enterprise environments with robust API validation
\item Develop and maintain automated unit tests and API validation to improve code quality and reliability
\item Contribute to CI/CD pipelines by creating API tests and test automation scripts for seamless deployments across multiple projects
\item Collaborate on WebSocket-based real-time data streaming and dashboard development using React for system monitoring and validation
\item Support test automation frameworks and version control with Git for reliable, auditable workflows across projects, and created docker deployment pipeline for Azure and claude environments
\end{itemize}
"""
JOB2 = r"""
\begin{itemize}
\item Developed dashboards for data visualization to provide actionable insights into system performance and testing results
\item Created automated test suites for REST APIs and Android applications to ensure functionality and high code quality
\item Collaborated with cross-functional teams to troubleshoot issues and optimize test cases for improved reliability across projects
\item Contributed to CI/CD validation and ensured stable software deployments through automated testing workflows across multiple projects
\item Assisted in automating testing processes to reduce manual effort and accelerate validation timelines across platforms and deployments
\item Analyzed test results to drive continuous improvement of software quality and testing workflows across teams and products
\end{itemize}

"""
ABOUT_ME = r"""
Software Engineer with experience in vehicle systems, ECU data analysis, process automation and test automation. Proficient in Python, Bash scripting, C++, API development (FastAPI), and automated testing frameworks with a strong focus on software quality. I have hands-on experience applying HiL/SiL simulations and CAN bus signal analysis to validate complex systems against KPIs. I leverage machine learning, deep learning, computer vision, data analysis, and cloud technologies to build AI-enabled automation tools. My work with agentic AI, LLM, RAG, and vector databases supports internal tooling for test case generation and workflow optimization. I am excited to apply these capabilities to develop enterprise AI applications and drive reliable, scalable deployments.
"""
JOB1_DE = r"""\begin{itemize}
\item Konzeption und Implementierung von Testszenarien für die DMS-Steuergeräte-Validierung zur Erfüllung von KPIs und funktionalen Anforderungen
\item Entwicklung von Python/Bash-Automatisierungsskripten zur Datenverarbeitung, KPI-Generierung und Optimierung von Testabläufen über mehrere Prüfstände und CI-Pipelines hinweg
\item Entwicklung von Tools zur automatisierten Testfallgenerierung durch Integration von Agents, LLMs, RAG und Vektordatenbanken zur Beschleunigung des Validierungsprozesses mittels LangChain und LangGraph
\item Erstellung von FastAPI-Backend-Services und React-basierten Webkomponenten für Systemtests und Integration in Unternehmensumgebungen mit robuster API-Validierung
\item Entwicklung und Pflege automatisierter Unit-Tests und API-Validierung zur Verbesserung von Codequalität und Zuverlässigkeit
\item Mitwirkung an CI/CD-Pipelines durch Erstellung von API-Tests und Testautomatisierungsskripten für nahtlose Deployments über mehrere Projekte hinweg
\item Zusammenarbeit bei WebSocket-basiertem Echtzeit-Datenstreaming und Dashboard-Entwicklung mit React für Systemüberwachung und Validierung
\item Unterstützung von Testautomatisierungs-Frameworks und Versionskontrolle mit Git für zuverlässige, nachvollziehbare Workflows über Projekte hinweg, sowie Erstellung einer Docker-Deployment-Pipeline für Azure- und Claude-Umgebungen
\end{itemize}
"""
JOB2_DE = r"""
\begin{itemize}
\item Entwickelte Dashboards zur Datenvisualisierung, um umsetzbare Erkenntnisse über Systemleistung und Testergebnisse bereitzustellen
\item Erstellte automatisierte Testsuiten für REST-APIs und Android-Anwendungen, um Funktionalität und hohe Codequalität sicherzustellen
\item Arbeitete mit funktionsübergreifenden Teams zusammen, um Probleme zu beheben und Testfälle für eine höhere Zuverlässigkeit über Projekte hinweg zu optimieren
\item Leistete Beiträge zur CI/CD-Validierung und stellte durch automatisierte Test-Workflows stabile Softwarebereitstellungen in mehreren Projekten sicher
\item Unterstützte die Automatisierung von Testprozessen, um manuellen Aufwand zu reduzieren und Validierungszeiten über Plattformen und Deployments hinweg zu beschleunigen
\item Analysierte Testergebnisse, um die kontinuierliche Verbesserung der Softwarequalität und der Test-Workflows über Teams und Produkte hinweg voranzutreiben
\end{itemize}

"""
ABOUT_ME_DE = r"""
Software Engineer mit Erfahrung in Fahrzeugsystemen, Steuergeräte-Datenanalyse, Prozessautomatisierung und Testautomatisierung. Versiert in Python, Bash-Scripting, C++, API-Entwicklung (FastAPI) und automatisierten Test-Frameworks mit starkem Fokus auf Softwarequalität. Ich habe praktische Erfahrung in der Anwendung von HiL/SiL-Simulationen und CAN-Bus-Signalanalyse zur Validierung komplexer Systeme anhand von KPIs. Ich nutze Machine Learning, Deep Learning, Computer Vision, Datenanalyse und Cloud-Technologien, um KI-gestützte Automatisierungstools zu entwickeln. Meine Arbeit mit agentenbasierter KI, LLM, RAG und Vektordatenbanken unterstützt interne Tools zur Testfallgenerierung und Workflow-Optimierung. Ich freue mich darauf, diese Fähigkeiten bei der Entwicklung von Enterprise-KI-Anwendungen einzusetzen und zuverlässige, skalierbare Deployments voranzutreiben.
"""


class TexBuilder:
    def __init__(self,  tex_dir: str, job_dis_path: str,  template: str, 
                 job1:Optional[bool] = False, job2:Optional[bool] = False,
                   keywords:Optional[bool] = True,
                    english:Optional[bool] = False):
        self.tex_dir = tex_dir

        self.job_dis_path = job_dis_path
        self.template = template
        self.job1 = job1
        self.job2 = job2
        self.keywords = keywords
        self.english = english
        self.image_path = os.path.normpath(r"C:\Users\vishv\Working_Dir\resumeBuilder\vish.png").replace('\\', '/')

    def create_tex_file(self) -> str:
        """Create a .tex file named `{pdf_name}.tex` inside `tex_dir` using the template.

        Returns:
            Full path to the created .tex file.
        """
        if self.english:
            job1, job2, profile_details, keywords = self.get_job_details_english(self.job_dis_path)
            fname =  os.path.splitext(os.path.basename(self.job_dis_path))[0].replace("lebenslauf", "resume")
        if not self.english:
            job1, job2, profile_details, keywords = self.get_job_details_german(self.job_dis_path)
            fname =  os.path.splitext(os.path.basename(self.job_dis_path))[0]
        filename = fname + '.tex'
        file = fname

        if not self.tex_dir:
            raise ValueError('tex_dir is required and must be a directory path')
        work_dir = self.tex_dir
        os.makedirs(work_dir, exist_ok=True)
        tex_path = os.path.join(work_dir, filename)

        

        job1_str = self.job_details_to_latex(job1)
        job2_str = self.job_details_to_latex(job2)
        keywords_str = self.list_to_latex_items_keywords(keywords)


        print('#'*50)
        print(keywords_str)

        if self.template is None:
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
            tpl = self.template

        # Build content from template and replace placeholders
        content = tpl.replace('__IMAGE_PATH__', self.image_path)
        #content = content.replace('__PROFILE_DETAILS__', profile_details)
        # content = content.replace('__NAME__', name)
        
        if self.job1:
            content = content.replace('__JOB_1_DETAILS__', job1_str)
            content = content.replace('__PROFILE_DETAILS__', profile_details)
        else:
            if self.english:
                content = content.replace('__JOB_1_DETAILS__', JOB1)
                content = content.replace('__PROFILE_DETAILS__', ABOUT_ME)
            else:
                print('Using German job details')
                print('#'*50)
                content = content.replace('__JOB_1_DETAILS__', JOB1_DE)
                content = content.replace('__PROFILE_DETAILS__', ABOUT_ME_DE)
        if self.job2:
            content = content.replace('__JOB_2_DETAILS__', job2_str)
        else:
            if self.english:
                content = content.replace('__JOB_2_DETAILS__', JOB2)
            else:
                content = content.replace('__JOB_2_DETAILS__', JOB2_DE)
        if self.keywords:
            content = content.replace('__KEYWORDS__', keywords_str)
        else:
            content = content.replace('__KEYWORDS__', '')

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
        #latex = "{\color{sidebarbg} {"
        latex = ", ".join(keywords)
        #latex += "}"
        return latex

    def list_to_latex_items_keywords(self, skills, chunk_size=4):
        """
        Convert a flat list of skills into a LaTeX itemize block,
        with 3–4 items per bullet.
        """
        def chunks(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i:i+n]

        latex_lines = ["\\begin{itemize}[leftmargin=10pt]"]

        for chunk in chunks(skills, chunk_size):
            latex_lines.append("\\item " + ", ".join(chunk))

        latex_lines.append("\\end{itemize}")

        return "\n".join(latex_lines)

    def get_job_details_english(self, jsonPath):
        with open(jsonPath, 'r', encoding='utf-8') as f:
            job_details = json.load(f)
        parsed_job_details =  job_details.get("result_english", {})
        job1 = parsed_job_details.get("Job_1_suggested", [])
        job2 = parsed_job_details.get("Job_2_suggested", [])
        profile_details = parsed_job_details.get("about_me", "")
        keywords = parsed_job_details.get("keywords", [])
        return job1, job2, profile_details, keywords

    def get_job_details_german(self, jsonPath):
        with open(jsonPath, 'r', encoding='utf-8') as f:
            job_details = json.load(f)
        parsed_job_details =  job_details.get("result_german", {})
        parsed_job_details_english =  job_details.get("result_english", {})
        job1 = parsed_job_details.get("Job_1_suggested_german", [])
        job2 = parsed_job_details.get("Job_2_suggested_german", [])
        profile_details = parsed_job_details.get("about_me_german", "")
        keywords = parsed_job_details_english.get("keywords", [])
        return job1, job2, profile_details, keywords