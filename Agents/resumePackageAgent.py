from typing import List

from langchain.tools import Tool
from langchain.agents import (
    AgentExecutor,
    create_tool_calling_agent
)

from langchain_core.prompts import ChatPromptTemplate
import os
from langchain_openai import ChatOpenAI

#from ChatGPTHandler import ChatGPTHandler
from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel, Field
from llmHandler.ChatGptLLMHandler import ChatGPTHandler


# class ChatGPTHandler:

#     def __init__(self, model_name="gpt-5-nano"):

#         api_key = os.getenv("CHAT_GPT_API")

#         if not api_key:
#             raise ValueError(
#                 "CHAT_GPT_API environment variable is not set"
#             )

#         self.llm = ChatOpenAI(
#             model=model_name,
#             api_key=api_key,
#             temperature=0.2
#         )


class ResumePackageInput(BaseModel):
    about_me: str 
    keywords: List[str] = Field(default_factory=list)
    Job_1_suggested: List[str] = Field(default_factory=list)
    Job_2_suggested: List[str] = Field(default_factory=list)
    cover_letter_first: str
    cover_letter_last: str
    rationale: List[str] = Field(default_factory=list)

class ResumeTailorAgent:

    def __init__(self):

        self.llm = ChatGPTHandler().llm

        self.tools = self._create_tools()

        self.agent_executor = self._create_agent()

    ####################################################################
    # TOOL
    ####################################################################

    def generate_resume_package(
        self,
        inputs: str
    ) -> str:

        prompt = f"""
            You are an expert Resume Coach and ATS Specialist.

            Create a complete ATS optimized resume package.

            Rules:

            1. Generate 'about_me'
            - 5 - 6 sentences
            - Tailored to the job description
            - ATS optimized
            - must take refrenace from my about me, job1, and Job2 tasks (which I already complited ) 

            2. Generate keywords
            - 10-20 ATS keywords
            - Extract from the job description

            3. Generate Job_1_suggested
            - 7 to 8 bullets
            - Use only Job_1 experience
            - Action oriented
            - 15-20 words per bullet

            4. Generate Job_2_suggested
            - 6  bullets
            - Use only Job_2 experience
            - Highlight transferable skills
            - 15-20 words per bullet

            5. Generate cover_letter_first
            - 4-5 sentences
            - Tailored to the target role
            - No greeting
            - No Dear Hiring Manager

            6. Generate cover_letter_last
            - 3-4 sentences
            - Summarize qualifications
            - must take refrenace from my about me, job1, and Job2 tasks (which I already complited ) 
            - Demonstrate enthusiasm
            - No Sincerely
            - No Regards
            - No signature

            7. Generate rationale
            - Explain major alignment decisions
            YOU MUST RETURN ALL Keys.
            - about_me
            - keywords
            - Job_1_suggested
            - Job_2_suggested
            - cover_letter_first
            - cover_letter_last
            - rationale
            
            Important:
            

            - Never fabricate experience.
            - Never fabricate technologies.
            - Never fabricate certifications.
            - Never fabricate metrics.
            - Use only evidence contained in the input.

            Return ONLY JSON.

            Expected Schema:

            {{
                "about_me": "",
                "keywords": [],

                "Job_1_suggested": [],

                "Job_2_suggested": [],

                "cover_letter_first": "",

                "cover_letter_last": "",

                "rationale": []
            }}

            INPUT:

            {inputs}
            """
        strcuted_llm = self.llm.with_structured_output(ResumePackageInput)
        
        #response = self.llm.invoke(prompt)
        response = strcuted_llm.invoke(prompt)
        return response

    ####################################################################
    # TOOLS
    ####################################################################

    def _create_tools(self):

        return [

            Tool(
                name="ResumePackageGenerator",
                func=self.generate_resume_package,
                description="""
                    Generate a complete ATS-optimized resume package.

                    Responsibilities:

                    - Analyze target job description.
                    - Extract ATS keywords.
                    - Generate professional summary (about_me).
                    - Generate 7-8 tailored bullets for current role.
                    - Generate 6-7 tailored bullets for previous role.
                    - Generate first cover letter paragraph.
                    - Generate final cover letter paragraph.
                    - Generate rationale.
                    - Never fabricate experience.
                """
            )

        ]

    ####################################################################
    # PROMPT
    ####################################################################

    def _build_prompt(self):

        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                        You are a resume tailoring assistant.

                        Always use ResumePackageGenerator
                        to generate the final answer.

                        Return JSON only.
                    """
                ),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}")
            ]
        )

    ####################################################################
    # AGENT
    ####################################################################

    def _create_agent(self):

        prompt = self._build_prompt()

        agent = create_tool_calling_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=prompt
        )

        return AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=True,
            max_iterations=3,
            handle_parsing_errors=True
        )

    ####################################################################
    # BUILD INPUT
    ####################################################################

    def build_input(
        self,
        job_description: str,
        about_me: str,
        job1: List[str],
        job2: List[str]
        ):

        return f"""
                JOB DESCRIPTION
                ---------------
                {job_description}

                CURRENT ABOUT ME
                ----------------
                {about_me}

                JOB_1_CURRENT_ROLE
                ------------------

                {chr(10).join('- ' + x for x in job1)}

                JOB_2_PREVIOUS_ROLE
                -------------------

                {chr(10).join('- ' + x for x in job2)}
                """

    ####################################################################
    # RUN
    ####################################################################

    def run(
        self,
        job_description,
        about_me,
        job1,
        job2
    ):

        agent_input = self.build_input(
            job_description,
            about_me,
            job1,
            job2
        )

        result = self.agent_executor.invoke(
            {
                "input": agent_input
            }
        )

        return result["output"]