import json
from typing import Any, List

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
from pydantic import BaseModel, ConfigDict, Field
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
    model_config = ConfigDict(extra="ignore")

    about_me: str = ""
    keywords: List[str] = Field(default_factory=list)
    Job_1_suggested: List[str] = Field(default_factory=list)
    Job_2_suggested: List[str] = Field(default_factory=list)
    cover_letter_first: str = ""
    cover_letter_last: str = ""
    rationale: List[str] = Field(default_factory=list)

    @classmethod
    def from_response(cls, payload: Any) -> "ResumePackageInput":
        if isinstance(payload, cls):
            return payload

        if isinstance(payload, str):
            try:
                payload = json.loads(payload)
            except json.JSONDecodeError:
                payload = {}

        if isinstance(payload, dict):
            normalized_payload = {
                "about_me": payload.get("about_me", ""),
                "keywords": payload.get("keywords") or [],
                "Job_1_suggested": payload.get("Job_1_suggested") or [],
                "Job_2_suggested": payload.get("Job_2_suggested") or [],
                "cover_letter_first": payload.get("cover_letter_first", ""),
                "cover_letter_last": payload.get("cover_letter_last", ""),
                "rationale": payload.get("rationale") or [],
            }
            return cls.model_validate(normalized_payload)

        return cls()

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
            - I have around 4 years of experience in software development 
            - 4-5 sentences
            - Tailored to the job description
            - ATS optimized use ATS friendly keywords from the job description
            - must take refrenace from my about me, job1, and Job2 tasks (which I already complited )
            - also express my enthusiasm  about learning new technologies and adapting to new challenges when the job discription doent extacly match with my current and previous role


            2. Generate keywords
            - 20-25 ATS keywords
            - Extract from the job description

            3. Generate Job_1_suggested
            - 7 to 8 bullets
            - Use only Job_1 experience
            - Action oriented
            - use ATS friendly keywords from the job description
            - 15-20 words per bullet
            - resume points needs to be conceise,(short) technical, and achievement‑oriented for german industry oriented
            - Use present tense.
            - Use non‑imperative, third‑person, neutral phrasing (no ‘I’, no ‘Responsible for’, no commands).
            - Start each bullet with a noun phrase or descriptive action phrase.
            

            4. Generate Job_2_suggested
            - 7  bullets
            - Use only Job_2 experience
            - use ATS friendly keywords from the job description
            
            - Highlight transferable skills
            - 15-20 words per bullet
            - this is my previous role(as working student in industry), so you can use past tense

            5. Generate cover_letter_first
            - 4-5 sentences
            - Tailored to the target role
            - No greeting
            - No Dear Hiring Manager

            6. Generate cover_letter_last
            - 3-4 sentences
            - Summarize qualifications
            -  if i am missing some teche skills focus on transferable skills highlight my learning speed  keep it focus on positive aspect
            - must take refrenace from my about me, job1, and Job2 tasks (which I already complited ) 
            - also express my enthusiasm  about learning new technologies and adapting to new challenges when the job discription doent extacly match with my current and previous role
            
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

            Return ONLY the JSON object

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
        structured_llm = self.llm.with_structured_output(ResumePackageInput)

        response = structured_llm.invoke(prompt)
        normalized_response = ResumePackageInput.from_response(response)
        print('#'*50)
        print(normalized_response.model_dump())
        print('#'*50)
        return normalized_response.model_dump()

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
                    - Generate tailored bullets for current role.
                    - Generate tailored bullets for previous role.
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
            handle_parsing_errors=True,
            return_intermediate_steps=True
        )

    ####################################################################
    # BUILD INPUT
    ####################################################################

    def build_input(
        self,
        job_description: str,
        about_me: str,
        #job1: List[str],
        job1: str,
        job2: List[str]
        ):

        return f"""
                JOB DESCRIPTION
                ---------------
                {job_description}

                CURRENT ABOUT ME
                ----------------
                {about_me}

                JOB_1_CURRENT_ROLE Project profile including the tasks and responsibilities
                ------------------

              {job1}

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

        output = result.get("output", "")
        if not output or "max iterations" in output.lower():
            fallback = self._extract_fallback_output(result)
            if fallback is not None:
                return fallback

        print('#Re'*50)
        print(output)
        print('#'*50)

        return output

    def _extract_fallback_output(self, result: Any) -> Any:
        intermediate_steps = result.get("intermediate_steps", [])
        for step in intermediate_steps:
            action = step.get("action")
            observation = step.get("observation")
            if action and getattr(action, "tool", None) == "ResumePackageGenerator" and observation:
                if isinstance(observation, dict):
                    return observation
                if isinstance(observation, str):
                    try:
                        return json.loads(observation)
                    except json.JSONDecodeError:
                        return observation

        return None
    