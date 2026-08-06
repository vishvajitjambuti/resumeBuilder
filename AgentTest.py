#from resumeTailorAgent import ResumeTailorAgent
from Agents.resumePackageAgent import ResumeTailorAgent
import os
import json
from dotenv import load_dotenv
load_dotenv()
from prompt.prompt_data import about_me, Job_1_details_FullTime, Job_2_details_Workstudent
#from prompt.prompt_data import about_me, Job_1_details_FullTime, Job_2_details_Workstudent, job_advertise_description

job_advertise_description =  """
Job description

To strengthen our team, we are looking for a software developer (m/f/d) specializing in robotics to develop and further optimize the ROS-based control software for our HERBIE automated guided vehicle (AGV) system. You will test your solutions both in simulation and directly on the actual vehicle and actively contribute to conceptual decisions. You will work in an agile development team and, if required, accompany our robotics solutions on international customer projects.

Your tasks

Commissioning of our systems at the customer's site
Development of the ROS-based control software for our driverless transport vehicle Herbie
Testing the software in simulation as well as on the real prototype
Influence on conceptual decisions
Working with agile methods (SCRUM)
Your profile

Willingness to travel
Experience in software development with ROS
Interest in robotics
Experience with Linux and Python is an advantage.
Safe handling of Git
Enjoyment of working in a team
Fluent English and/or German
You are creative and enjoy putting your own ideas into practice in a well-thought-out way.
Job type: Full-time

Application question(s):

Do you have programming experience with C++ and/or Python?
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


