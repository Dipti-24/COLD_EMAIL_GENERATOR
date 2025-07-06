import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        print("Loaded GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))

        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile"
        )
        
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        company_name = job.get('company', 'your company')
        role = job.get('role', 'this position')
        skills = ", ".join(job.get('skills', []))

        prompt_email = PromptTemplate.from_template(
            f"""
            ### JOB DESCRIPTION:
            {job['description']}

            ### INSTRUCTION:
            You are Dipti, a business development executive at Qi, an AI & Software Consulting company.  
            You are reaching out to **{company_name}** regarding their opening for **{role}**.  

            Personalize the email by:
            - Mentioning the role and key required skills: {skills}
            - Highlighting how Qi has experience in similar projects.
            - Adding the most relevant portfolio links: {{link_list}}

            Do not include a preamble.

            ### EMAIL (NO PREAMBLE):
            """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({
            "job_description": str(job),
            "link_list": "\n".join(links)
        })
        return res.content

    def write_follow_up(self, job, links, days_since_last_email):
        follow_up_prompt = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Dipti, a business development executive at Qi. Qi is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            You are writing a follow-up email for a job application where you sent the initial email {days_since_last_email} days ago and have not received a response.
            In this follow-up email, acknowledge that it's been {days_since_last_email} days since you reached out and reiterate your interest in the position.
            Include the key points from your initial email and offer any additional information that might help.
            You can also add the most relevant portfolio links from the following: {link_list}
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )
        chain_follow_up = follow_up_prompt | self.llm
        res = chain_follow_up.invoke({
            "job_description": str(job),
            "link_list": "\n".join(links),
            "days_since_last_email": days_since_last_email
        })
        return res.content
