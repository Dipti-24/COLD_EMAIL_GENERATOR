import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
#from langchain.document_loaders import WebBaseLoader


from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    st.title("📧 Cold Mail Generator")

    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-48627?from=job%20search%20funnel")
    submit_button = st.button("Submit")

    # Follow-up email input
    follow_up_days = st.number_input("Enter days since last email for follow-up:", min_value=1, max_value=30, step=1, value=7)

    if submit_button:
        try:
            # Load and clean the web page
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)

            # Load portfolio data and job listings
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)

            if not jobs:
                st.warning("No job postings found on the page.")
                return

            for idx, job in enumerate(jobs):
                skills = job.get('skills', [])
                job_title = job.get("role", f"Job {idx + 1}")

                # Query relevant portfolio links
                links = portfolio.query_links(skills, job_title)

                # Generate cold email
                email = llm.write_mail(job, links)

                with st.expander(f"📬 Email for {job_title}", expanded=True):
                    st.code(email, language='markdown')

                    checkbox_key = f"followup_{idx}_{job_title.replace(' ', '_')}"
                    if st.checkbox(f"Generate Follow-Up Email", key=checkbox_key):
                        follow_up_email = llm.write_follow_up(job, links, follow_up_days)
                        st.code(follow_up_email, language='markdown')

        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)
