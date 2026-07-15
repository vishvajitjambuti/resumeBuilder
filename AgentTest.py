#from resumeTailorAgent import ResumeTailorAgent
from Agents.resumePackageAgent import ResumeTailorAgent
import os
import json
from dotenv import load_dotenv
load_dotenv()
from prompt.prompt_data import about_me, Job_1_details_FullTime, Job_2_details_Workstudent
#from prompt.prompt_data import about_me, Job_1_details_FullTime, Job_2_details_Workstudent, job_advertise_description

job_advertise_description =  """
You'll be involved in:
Designing AI-powered business processes
Building intelligent AI Agents and Multi-Agent Systems
Developing workflow automations and orchestration layers
Integrating APIs, enterprise systems, and data platforms
Creating scalable AI architectures
Identifying automation opportunities across organizations
Running discovery workshops and solution design sessions
Supporting product innovation and new AI initiatives
Translating complex business challenges into AI-driven solutions


What We're Looking For


Technical Background
You have experience or strong interest in:
Artificial Intelligence & Generative AI
Workflow Automation Platforms
APIs and System Integrations
Process Engineering
Data-driven Applications
Digital Transformation
AI Agent Frameworks
Prompt Engineering
Solution Architecture


Bonus Points For:
Python, JavaScript, TypeScript or similar
n8n, Make, Zapier, LangChain, CrewAI, AutoGen
OpenAI, Anthropic, Gemini, Azure AI or AWS AI Services
CRM, ERP or enterprise software integrations
Experience in consulting or customer-facing projects
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


