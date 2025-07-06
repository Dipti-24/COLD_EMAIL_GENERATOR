
import pandas as pd
import chromadb
import uuid
import os


os.environ["CHROMA_TELEMETRY"] = os.getenv("CHROMA_TELEMETRY", "False")

class Portfolio:
    def __init__(self, file_path=None):
        if file_path is None:
            base_dir = os.path.dirname(__file__)
            file_path = os.path.join(base_dir, "resource", "my_portfolio.csv")
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient("vectorstore")
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")


    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                                    metadatas={"links": row["Links"]},
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills, job_title):
       
    # Ensure job_title is string
        if not isinstance(job_title, str):
            job_title = str(job_title) if job_title is not None else ""

        # Ensure skills is a list of strings
        if isinstance(skills, str):
            skills = [skills]
        elif not isinstance(skills, list):
            skills = []
        skills = [str(skill) for skill in skills if skill]

        query_texts = [job_title] + skills

        # Run query
        results = self.collection.query(query_texts=query_texts, n_results=3)

        # metadatas is a list of list of dicts → extract "links" from inner list
        links = [meta.get("links", "") for meta in results.get("metadatas", [[]])[0]]
        return links



        
    