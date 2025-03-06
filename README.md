# COLD_EMAIL_GENERATOR

**Overview**

The Cold Email Generator is a Python-based tool that automates the process of crafting personalized cold emails for job opportunities. The application scrapes job listings from a given URL, extracts relevant job details, and generates well-structured cold emails and follow-up emails. It leverages LangChain, ChromaDB, and Streamlit for data processing and interaction.

**Features**

1. Job Scraping & Processing: Extracts job details such as role, experience, skills, and description from the given URL.
2. Cold Email Generation: Generates personalized cold emails based on job descriptions and a predefined AI prompt.
3. Follow-up Email: Creates follow-up emails based on the number of days since the initial contact.
4. Portfolio Integration: Matches job-related skills with relevant portfolio links stored in a ChromaDB vector database.
5. Interactive UI: Uses Streamlit for an intuitive user interface.

**Tech Use**

**1.Python**

**2.LangChain**  : For LLM-based text generation

**3.ChromaDB** : For portfolio-based retrieval

**4.Streamlit**  : For UI

**5.Pandas** :  For handling job and portfolio data

**6.Groq API** : For LLM-powered text generation

**Installation & Setup**

**1️. Clone the Repository**

git clone https://github.com/Dipti-24/COLD_EMAIL_GENERATOR
cd cold-email-generator

**2️2. Install Dependencies**

Ensure you have Python 3.8+ installed, then run:

pip install -r requirements.txt

**3️. Set Up Environment Variables**

Create a .env file in the root directory and add your Groq API key:

GROQ_API_KEY=your_groq_api_key_here

**4️. Run the Application**

streamlit run app.py

This will launch the Cold Email Generator in your browser.

**Usage**

1️. Enter a job listing URL in the input box and press "Submit".

2️. The app scrapes the job page and extracts relevant details.

3️. It generates a cold email tailored to the job description.

4️. Optionally, generate a follow-up email by selecting the checkbox.

**Future Enhancements**

Add email templates & customization options.

**License**

MIT License. Feel free to modify and contribute! 

**Contact**
For any query reach out to me at mishradipti2402@gmail.com

