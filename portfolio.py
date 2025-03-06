
import pandas as pd
import chromadb
import uuid


class Portfolio:
    def __init__(self, file_path=r"C:\Users\mishr\Downloads\ColdEmailGen\app\resource\my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                                    metadatas={"links": row["Links"]},
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills, job_title):
        query_texts = [job_title] + skills  # Combine job role + skills for better matching
        results = self.collection.query(query_texts=query_texts, n_results=3)
        links = [item["links"] for item in results.get("metadatas", [])]

        return links