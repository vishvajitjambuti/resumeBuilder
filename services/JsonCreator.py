from typing import List, Dict, Any, Optional
from unittest import result
from prompt.prompt_data import about_me, Job_1_details_FullTime, Job_2_details_Workstudent
import json
from Agents.resumePackageAgent import ResumeTailorAgent
try:
    from llmHandler.AzureLLMHandler import AzureLLMHandler
except Exception:  # pragma: no cover - fallback for test environments
    AzureLLMHandler = None

try:
    from llmHandler.ChatGptLLMHandler import ChatGPTHandler
except Exception:  # pragma: no cover - fallback for test environments
    class ChatGPTHandler:
        def __init__(self, model_name: str = "gpt-5-nano"):
            self.model_name = model_name
            self.client = object()
            self.llm = object()

        def chat(self, messages):
            return "{}"


class JsonCreator:
    def __init__(self, base_json_dir: str = r"C:\Users\vishv\Working_Dir\resumeBuilder\data", job_discription= ""):
        self.job_description = job_discription
        self.job1_details = Job_1_details_FullTime
        self.job2_details = Job_2_details_Workstudent
        self.about_me = about_me
        self.job_details_json_path = base_json_dir
        self.model_name = "gpt-5-nano"  # or "gpt-5-nano" depending on your preference
        #self.LLM_handler = ChatGPTHandler(model_name="gpt-5-nano")  # or AzureLLMHandler(moel_name="gpt-4.1") depending on your preference
        self.LLM_handler = ChatGPTHandler(model_name=self.model_name)

    
    def _build_agent_prompt(self, job_description: str, job1: List[str], job2: List[str], about_me: str) -> str:
        
        #print(about_me)
        lines = []
        lines.append("You are a resume coach and career advisor.")
        lines.append("Task: Compare the provided job description (requirements + tasks) with the candidate's resume knowledge .")
        lines.append("Produce suggested updated bullets for the candidate's CURRENT full-time job (Job_1_details_FullTime) and one previous role (Job_2_details_Workstudent) included below. Also include a short 'about_me' section (4-5 sentences) tailored for the job description.")
        lines.append("While generating, need to take into consideration that the data from suggested bullet points is being extracted through Applicant Tracking Systems (ATS), where keywords are being extracted and compared with the job description. So, the suggested bullet points should be action-oriented, concise, and tailored to the job description, highlighting relevant skills and experiences.")
        lines.append("Do Not use orchestration for automation explain it in simple words, Do not use any new skills or experiences that are not present in the provided job details. Do not fabricate any details in the suggested bullets. Make sure the about_me, Job_1_details_FullTime, Job_2_details_Workstudent are used as the source of truth for the candidate's experience.")
        lines.append("Based on that also need to create first and last paragraph of the Cover letter for the candidate, highlighting the candidate's relevant skills and experiences, and expressing enthusiasm for the role.")
        lines.append("")
        lines.append("=== INPUT: Job description ===")
        lines.append(job_description.strip())
        lines.append("")
        lines.append("This is my current Job profile about me and Job dtails")
        lines.append("=== INPUT: Candidate about_me ===")
        lines.append(about_me.strip())
        lines.append("")
        lines.append("=== INPUT: Job_1_details_FullTime (current role)(all the project tasks) ===")
        for b in job1:
            lines.append(f"- {b}")
        lines.append("")
        lines.append("=== INPUT: Job_2_details_Workstudent (previous role) (all the project tasks) ===")
        for b in job2:
            lines.append(f"- {b}")
        lines.append("")
    
        lines.append("OUTPUT FORMAT:")
        lines.append("Return a JSON object with keys: 'about_me' (string), 'Job_1_suggested' (list of bullet strings), 'Job_2_suggested' (list of bullet strings), 'cover_letter_first' (string), 'cover_letter_last' (string), keywords (list of string) and optional 'rationale' (list of short strings explaining each suggested bullet).\n")
        lines.append("GUIDELINES:")
        lines.append("- For Job_1_suggested produce up to 8 concise action-oriented bullets tailored to the JD using evidence from the RAG when available.")
        lines.append("- For Job_2_suggested produce up to 7 bullets showing how the candidate could rephrase or emphasize skills to match the alternate role.")
        lines.append("- Use measurable outcomes where plausible; do not invent specific untrue numbers. Prefer phrasing like 'improved X' or 'reduced Y' only when supported by resume context.")
        lines.append("- Keep each bullet short (15-30 words) and focused.")
        lines.append ("- For cover_letter_first, write a 4-5 sentence paragraph introducing the candidate, highlighting relevant skills and experiences, and expressing enthusiasm for the role.")
        lines.append("- for Cover_letter  first do not add 'Dear Hiring Manager' or 'To whom it may concern' in the first paragraph, just write the paragraph without any salutation.")
        lines.append("- For cover_letter_last, write a 2-3 sentence paragraph summarizing the candidate's fit for the role, expressing interest in an interview, and thanking the reader.")
        lines.append("- for Cover_letter last do not add 'Sincerely' or 'Best regards' in the last paragraph, just write the paragraph without any closing salutation.")
        lines.append("- For keywords, extract 10-15 relevant keywords from the job description that that seems impoertant for the role and are likely to be used in ATS systems. Return them as a list of strings.")
        lines.append("- If you cannot find evidence in the resume RAG for a claim, flag it in the rationale rather than fabricating details.")
        lines.append("- Do not fibricate any details in the suggested bullets. make sure the about_me, Job_1_details_FullTime, Job_2_details_Workstudent are used as the source of truth for the candidate's experience. Do not add any new skills or experiences that are not present in the provided job details.")
        lines.append("")
        lines.append("Return ONLY the JSON object (no explanation text).")

        return "\n".join(lines)
    
    def translate_the_result_in_german(self,result):
        """Translate the result into German using the LLM. format the result in a JSON format with the same keys as the original result.
    
        Args:
            result: the original result from the resume RAG agent (JSON string or dict)
        return:
            Translated result in German (JSON string)
        """
        llm_handler = self.LLM_handler
        llm_client = llm_handler.client
        prompt =[]
        prompt.append(f"Translate the following JSON result into German, keeping the  structure adding _german to the keys:\n{result}")
        prompt.append("make sure keep the language technicle and professional, do not change the meaning of the content, keep the same structure of the JSON object, and add _german to the keys.")
        prompt.append("\nReturn ONLY the JSON object (no explanation text).")
        prompt = "\n".join(prompt)
        # llm_response = llm_client.chat.completions.create(
        #     model= self.model_name,
        #     messages=[
        #         {"role": "system", "content": "You are a helpful assistant."},
        #         {"role": "user", "content": prompt}
        #     ]
        # )
        #translated_result = llm_response.choices[0].message.content.strip()
        llm_response = llm_handler.chat(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return llm_response.strip()
    
    def run_agent(self, prompt):
        llm_handler = self.LLM_handler
        llm_client = llm_handler.client
        # LLM_response = llm_client.chat.completions.create(
        #     model="gpt-4.1",
        #     messages=[
        #         {"role": "system", "content": "You are a helpful assistant."},
        #         {"role": "user", "content": prompt}
        #     ]
        # )
        llm_response =llm_handler.chat(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return llm_response.strip()
    
    def save_result_to_json(self, result_english , result_german, filename):
        """Save the English and German results to a JSON file.

        Args:
            result_english: The result in English (JSON string or dict).
            result_german: The result in German (JSON string or dict).
            filename: The name of the file to save the results to.
        """
        # Convert strings to dictionaries if necessary
        filename = filename if filename.endswith('.json') else f"{filename}.json"
       
        if isinstance(result_english, str):
            result_english = json.loads(result_english)
        if isinstance(result_german, str):
            result_german = json.loads(result_german)

        # Combine results into a single dictionary
        combined_result = {
            "result_english": result_english,
            "result_german": result_german
        }
        out_filename = f"{self.job_details_json_path}/{filename}"

        # Save to JSON file
        with open(out_filename, 'w', encoding='utf-8') as f:
            json.dump(combined_result, f, ensure_ascii=False, indent=4)
    
    def create_jason(self, filename, job_description):
        prompt = self._build_agent_prompt(job_description, self.job1_details, self.job2_details, self.about_me)
        print(prompt)
        response_English = self.run_agent(prompt=prompt)
        response_German = self.translate_the_result_in_german(response_English)
        self.save_result_to_json(response_English, response_German, filename)
    
    def create_english_jason(self, filename, job_description):
        # prompt = self._build_agent_prompt(job_description, self.job1_details, self.job2_details, self.about_me)
        # print(prompt)
        # response_English = self.run_agent(prompt=prompt)
        agent = ResumeTailorAgent()
        response_English = agent.run(
            job_description=job_description,
            about_me=self.about_me,
            job1=self.job1_details,
            job2=self.job2_details
        )
        
        self.save_english_result_to_json(response_English, filename)
        print("English JSON file created successfully.")
    
    def create_english_jason_witoutAgent(self, filename, job_description):
        prompt = self._build_agent_prompt(job_description, self.job1_details, self.job2_details, self.about_me)
        print(prompt)
        response_English = self.run_agent(prompt=prompt)
        
        
        self.save_english_result_to_json(response_English, filename)
        print("English JSON file created successfully.")
    
    def save_english_result_to_json(self, result_english, filename):
        """Save the English result to a JSON file.

        Args:
            result_english: The result in English (JSON string or dict).
            filename: The name of the file to save the results to.
        """
        # Convert string to dictionary if necessary
        filename = filename if filename.endswith('.json') else f"{filename}.json"
       
        if isinstance(result_english, str):
            result_english = json.loads(result_english)

        final_structure = {
            "result_english": result_english
        }
        # Save to JSON file
        out_filename = f"{self.job_details_json_path}/{filename}"
        with open(out_filename, 'w', encoding='utf-8') as f:
            json.dump(final_structure, f, ensure_ascii=False, indent=4)
     
    
    
    def  update_json_with_translated_result(self, filename):
        """Update the existing JSON file with the translated result.

        Args:
            filename: The name of the existing JSON file to update.
            translated_result: The translated result in German (JSON string or dict).
        """
        # Convert string to dictionary if necessary
        
        input_filename = f"{self.job_details_json_path}/{filename}.json"
        
        with open(input_filename, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
            data_english = existing_data.get("result_english", {})
        print(f"Existing English result: {data_english}")
        
        response_German = self.translate_the_result_in_german(data_english)
        print(f"Translated result in German: {response_German}")
        
        #existing_data("result_german", {}) = response_German
        existing_data["result_german"] = json.loads(response_German) if isinstance(response_German, str) else response_German
        # add the job description to the existing data strip the \n from the job description
        existing_data["job_description"] = self.job_description.strip()
        
        with open(input_filename, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {input_filename} with translated result successfully.")

