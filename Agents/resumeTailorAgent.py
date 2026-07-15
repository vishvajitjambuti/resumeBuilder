from typing import List, Dict, Any
import json
#from ..llmHandler.ChatGptLLMHandler import ChatGPTHandler

from langchain.agents import (
    AgentExecutor,
    create_tool_calling_agent,
    Tool
)

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class ChatGPTHandler:
    """Handler for OpenAI ChatGPT interactions."""

    def __init__(self, model_name: str = "gpt-5-nano"):
        self.model_name = model_name
        self.api_key = os.getenv("CHAT_GPT_API")

        if not self.api_key:
            raise ValueError("CHAT_GPT_API environment variable is not set.")

        self.client = OpenAI(api_key=self.api_key)




class ResumeTailorAgent:

    def __init__(
        self,
        azure_endpoint: str = None,
        api_key: str = None,
        deployment_name: str = "gpt-4.1",
        api_version: str = "2024-10-21"
    ):

        # self.llm = AzureChatOpenAI(
        #     azure_endpoint=azure_endpoint,
        #     api_key=api_key,
        #     deployment_name=deployment_name,
        #     api_version=api_version,
        #     temperature=0.2
        # )
        self.llm = ChatGPTHandler(model_name="gpt-5-nano")  # or AzureLLMHandler(moel_name="gpt-4.1") depending on your preference

        self.tools = self._create_tools()
        self.agent_executor = self._create_agent()

    ########################################################################
    # TOOLS
    ########################################################################

    def extract_keywords(self, job_description: str) -> str:
        """
        Extract ATS keywords from JD.
        """

        prompt = f"""
        Extract:
        - technical_skills
        - soft_skills
        - tools
        - responsibilities

        Return JSON only.

        Job Description:
        {job_description}
        """

        response = self.llm.invoke(prompt)

        return response.content

    def gap_analysis(self, inputs: str) -> str:
        """
        Compare resume content against JD.
        """

        prompt = f"""
        Analyze alignment between resume experience and Job Description.

        Return JSON:

        {{
            "matching_skills": [],
            "missing_skills": [],
            "recommendations": []
        }}

        Input:
        {inputs}
        """

        response = self.llm.invoke(prompt)

        return response.content

    def generate_resume_package(self, inputs: str) -> str:
        """
        Generate a complete job-tailored resume package.
        """

        
        prompt = f"""
            Create a complete ATS-optimized resume package.

            Requirements:

            1. Generate 'about_me'
            - 4-5 sentences
            - Tailored to the job description
            - ATS optimized

            2. Generate 'keywords'
            - 10-20 relevant ATS keywords from the job description

            3. Generate 'Job_1_suggested'
            - 7-8 concise action-oriented bullets
            - Use evidence from Job_1 experience
            - 15-30 words per bullet

            4. Generate 'Job_2_suggested'
            - 6-7 concise bullets
            - Highlight transferable skills
            - Use evidence from Job_2 experience

            5. Generate 'cover_letter_first'
            - 4-5 sentences
            - Tailored to the role
            - No greeting or salutation

            6. Generate 'cover_letter_last'
            - 3-4 sentences
            - Summarize experience and strengths
            - Show interest in the position
            - No Sincerely, Regards, Thanks, or signature

            7. Generate 'rationale'
            - Explain key alignment decisions
            - Mention unsupported skills if applicable

            Important Rules:
            - Never invent experience.
            - Never invent technologies.
            - Never invent certifications.
            - Never invent metrics.
            - Use only evidence available in the input.
            - Return valid JSON only.

            Return JSON schema:

            {{
                "about_me": "",
                "keywords": [],
                "Job_1_suggested": [],
                "Job_2_suggested": [],
                "cover_letter_first": "",
                "cover_letter_last": "",
                "rationale": []
            }}

            Input:
            {inputs}
        """


        response = self.llm.invoke(prompt)

        return response.content
    
    

    def validate_content(self, generated_text: str) -> str:
        """
        Validate generated bullets.
        """

        prompt = f"""
        Verify all claims are supported.

        Return JSON:

        {{
            "valid": true,
            "issues": []
        }}

        Content:
        {generated_text}
        """

        response = self.llm.invoke(prompt)

        return response.content

    ########################################################################
    # TOOL REGISTRATION
    ########################################################################

    def _create_tools(self):

        return [

            Tool(
                name="JDKeywordExtractor",
                func=self.extract_keywords,
                description="""
                Extract ATS keywords, skills,
                tools and responsibilities from job description.
                """
            ),

            Tool(
                name="ResumeGapAnalyzer",
                func=self.gap_analysis,
                description="""
                Compare resume experience to JD and
                identify matching and missing skills.
                """
            ),

            Tool(
                name="ResumePackageGenerator",
                func=self.generate_resume_package,
                description="""
                
                Generate a complete job-tailored resume package based on the provided
                job description and candidate experience.

                """
            ),

            Tool(
                name="FactValidator",
                func=self.validate_content,
                description="""
                Validate generated content and detect hallucinations.
                """
            )

        ]

    ########################################################################
    # PROMPT
    ########################################################################

    def _build_prompt(self):

        return ChatPromptTemplate.from_messages(

            [
                (
                    "system",
                    """
                    You are an expert Resume Coach and ATS Specialist.

                    Workflow:

                    1. Analyze JD(Job Description).
                    2. Call JDKeywordExtractor.
                    3. Call ResumeGapAnalyzer.
                    4. Call ResumeBulletGenerator.
                    5. Call FactValidator.
                    6. Return final JSON.

                    HARD RULES:

                    - Never fabricate projects.
                    - Never fabricate technologies.
                    - Never fabricate metrics.
                    - Use only evidence provided.
                    - 
                    - Return JSON only.
                    

                    """
                ),

                (
                    "human",
                    "{input}"
                ),

                (
                    "placeholder",
                    "{agent_scratchpad}"
                )
            ]

        )

    ########################################################################
    # AGENT
    ########################################################################

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
            max_iterations=10,
            handle_parsing_errors=True,
            return_intermediate_steps=True
        )

    ########################################################################
    # INPUT CONSTRUCTION
    ########################################################################

    def build_input(
        self,
        job_description: str,
        about_me: str,
        job1: List[str],
        job2: List[str]
    ) -> str:

        return f"""
        JOB DESCRIPTION
        ----------------
        {job_description}

        ABOUT ME
        ----------------
        {about_me}

        CURRENT ROLE
        ----------------
        {chr(10).join('- ' + x for x in job1)}

        PREVIOUS ROLE
        ----------------
        {chr(10).join('- ' + x for x in job2)}

        Target Output:

        {{
            "about_me": "...",
            "keywords": [],
            "Job_1_suggested": [
                {""}
            ],

            "Job_2_suggested": [
                {""}
            ],
            "cover_letter_first": " ...",
            "cover_letter_last": " ...",
            "rationale": []
        }}
        """

    ########################################################################
    # EXECUTE
    ########################################################################

    def run(
        self,
        job_description: str,
        about_me: str,
        job1: List[str],
        job2: List[str]
    ) -> Dict[str, Any]:

        agent_input = self.build_input(
            job_description=job_description,
            about_me=about_me,
            job1=job1,
            job2=job2
        )

        result = self.agent_executor.invoke(
            {
                "input": agent_input
            }
        )

        try:
            return json.loads(result["output"])
        except Exception:
            return {
                "raw_output": result["output"],
                "intermediate_steps": result.get(
                    "intermediate_steps",
                    []
                )
            }