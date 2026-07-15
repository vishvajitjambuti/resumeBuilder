#from resumeTailorAgent import ResumeTailorAgent
from resumePackageAgent import ResumeTailorAgent
import os
import json
from dotenv import load_dotenv
load_dotenv()
#from prompt.prompt_data import about_me, Job_1_details_FullTime, Job_2_details_Workstudent, job_advertise_description
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
print(f"AZURE_ENDPOINT: {AZURE_ENDPOINT}")
print(f"API_KEY: {API_KEY}")
about_me =  """Software Engineer with experience in vehicle systems, ECU testing, data analysis, and test automation. Proficient in HiL/SiL simulations, 
CAN bus analysis using CANoe, and KPI-based performance evaluation. Skilled in Python/Bash scripting, API development (FastAPI),
 and automated testing frameworks, 
with a strong focus on software quality, reliability, and end-to-end lifecycle support for complex systems.
good knowledge of Agentic AI, LLM, RAG and vector database for building internal automation tools for test case generation.


programming language known: Python, Bash, SQL, C++, flutter
frameworks: FastAPI, Scikit-learn, TensorFlow, PyTorch, ROS2, React, c#
tools: Git, Docker,  CANoe, MATLAB/Simulink, , .Net,
skills: machine learning, deep learning, computer vision, NLP, data analysis, data visualization, docker containerization, CI
"""

output_scema = {
    "about_me": "",
    "Job_1_details_FullTime": [],
    "Job_2_details_Workstudent": []
}

Job_1_details_FullTime= [
    "Conduct HiL/SiL simulations for DMS ECUs to validate system performance against KPIs and functional requirements",
    "Analyze ECU and CAN bus data using CANoe for  comparative system studies",                                                          
    "Develop automation scripts (Python/Bash) for data processing, KPI generation, and optimization of test workflows",
    "Bash Scripting for HIL testing",
    "Design and implement FastAPI-based backend services and web components for test system orchestration and integration",

    "worked with LLM, RAG and vector database for building internal automation tools for test case generation",      
    "Create and maintain automated unit tests and perform API validation to improve code quality and system reliability",
    "Support test automation frameworks and CI-based workflows using Git for continuous integration and validation",
    "Contribute to software lifecycle activities including testing, debugging, and continuous improvement of system performance"
]

Job_2_details_Workstudent=  [
    "Develop dashboards for data visualization to provide insights into system performance and testing results",
    "Implement unit and integration tests for REST APIs and Android applications to ensure functionality and high code quality",
    "Create automated test suites to improve code coverage and support continuous integration processes",
    "Collaborate with development teams to troubleshoot issues and optimize test cases for improved reliability",
    "Assist in test automation processes to reduce manual testing effort and enhance validation efficiency",
    "Analyze test results and support continuous improvement of software quality and testing workflows",
    "Contribute to CI/CD validation and ensure stable and reliable software deployments", 
   " Development of a product recommendation system",
        
    "worked on product classification algorithm "
    " Development of a mobile Android application for data collection of products in the warehouse (in Flutter, Dart)"
]

job_advertise_description =  """
What to Expect
Software Development: Responsible for developing software to orchestrate HiL systems
Programming: Implementing software solutions in Python and C#
Test automation: Design and implementation of a platform for the automated control of test systems. This includes the development of scripts and frameworks to increase the efficiency of test processes
Life cycle management: Involvement throughout the entire software life cycle, including specification, design, implementation, and acceptance testing
Software architecture: Further development of the software architecture while adhering to the specified interfaces
Test management: Definition, implementation, and monitoring of automated tests, as well as analysis of test results to continuously improve the software (e.g., Jenkins, Git, VeriStand)
Process Optimization: Application and integration of a V-model approach in combination with agile methods for efficient project implementation
Documentation: Creation and maintenance of comprehensive documentation to ensure quality and traceability
=============================================================
What You Bring to the Table
A bachelor’s or master’s degree in computer science or a related field, supplemented by relevant professional experience in software development
In-depth knowledge of software development using Python and Git, particularly in the development of automation solutions and the implementation of continuous integration (CI) pipelines
Experience with the C# programming language is a plus
Knowledge of and experience with the real-time test and simulation software VeriStand, as well as real-time systems from National Instruments (NI), are desirable
Very good command of German and good written and spoken English
An independent, solution-oriented approach to work, combined with a high degree of reliability, commitment, and a willingness to take on responsibility
Strong communication skills and the ability to work effectively as part of a team
For our renowned client, a leader in the manufacture of aircraft engines, we are seeking a Software Developer for Test Systems (m/f/d) to join our Munich office as soon as possible on a temporary assignment basis.

"""
















# agent = ResumeTailorAgent(
#     azure_endpoint=AZURE_ENDPOINT,
#     api_key=API_KEY,
#     deployment_name="gpt-4.1"
# )
# agent = ResumeTailorAgent()

# result = agent.run(
#     job_description=job_advertise_description,
#     about_me=about_me,
#     job1=Job_1_details_FullTime,
#     job2=Job_2_details_Workstudent
# )

agent = ResumeTailorAgent()

response = agent.run(
    job_description=job_advertise_description,
    about_me=about_me,
    job1=Job_1_details_FullTime,
    job2=Job_2_details_Workstudent
)
print('Generated Resume Content:')
print(response)


print('Generated Resume Content:')
#print(json.dumps(response, indent=2))

test = """  - for Job_1_suggested produce up to 8 concise action-oriented bullets tailored to the JD using evidence compared with job1(provided all the data in detailed) from the input 
                    - for Job_2_suggested produce up to 6 bullets showing how the candidate could rephrase or emphasize skills to match the alternate role using evidence compared with job2(provided all the data in detailed) from the input
                    - Extract the most relevant ATS keywords from the Job Description.
                    - Store them in the 'keywords' field.
                    - Include only keywords strongly relevant to the target role.
                    - Return 10-20 keywords when available"""