# COLD_EMAIL_GENERATOR

## Overview

The Cold Email Generator is a Python-based tool that automates the process of crafting personalized cold emails for job opportunities. The application scrapes job listings from a given URL, extracts relevant job details, and generates well-structured cold emails and follow-up emails. It leverages LangChain, ChromaDB, and Streamlit for data processing and interaction.

## Features

1. Job Scraping & Processing: Extracts job details such as role, experience, skills, and description from the given URL.
2. Cold Email Generation: Generates personalized cold emails based on job descriptions and a predefined AI prompt.
3. Follow-up Email: Creates follow-up emails based on the number of days since the initial contact.
4. Portfolio Integration: Matches job-related skills with relevant portfolio links stored in a ChromaDB vector database.
5. Interactive UI: Uses Streamlit for an intuitive user interface.

## Tech Use

**1.Python**

**2.LangChain**  : For LLM-based text generation

**3.ChromaDB** : For portfolio-based retrieval

**4.Streamlit**  : For UI

**5.Pandas** :  For handling job and portfolio data

**6.Groq API** : For LLM-powered text generation

**7. Docker** – Containerization

## Installation & Setup

### 1️. Clone the Repository

 git clone https://github.com/Dipti-24/COLD_EMAIL_GENERATOR

 cd COLD_EMAIL_GENERATOR

### 2. Set Up Environment Variables

 Create a .env file in the root directory and add your Groq API key:

 GROQ_API_KEY=your_groq_api_key_here

### 4️. Run the Application

#### Without Docker
1. Install DependencieS

   Ensure you have Python 3.8+ installed, then run:

   pip install -r requirements.txt


2. streamlit run main.py

   This will launch the Cold Email Generator in your browser

#### With DOcker
1. Build the docker image
   docker build -t cold-mail-generator .
   
2. Run the App (Windows)
  docker run -it --rm -p 8501:8501   -v "${PWD}\vectorstore:/app/vectorstore" --env-file .env ` cold-mail-generator

3. Access the app
   Visit: http://localhost:8501


## Usage

1️. Enter a job listing URL in the input box and press "Submit".

2️. The app scrapes the job page and extracts relevant details.

3️. It generates a cold email tailored to the job description.

4️. Optionally, generate a follow-up email by selecting the checkbox.

## Future Enhancements

Add email templates & customization options.

## License

This project is licensed under  the [MIT License](https://github.com/Dipti-24/Cold_Email_Generatorr/blob/main/LICENSE). 

## Contact
For any query reach out to me at mishradipti2402@gmail.com

