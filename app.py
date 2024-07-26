import streamlit as st
import os
from api_clients import GroqClient, FireCrawlClient
from content_extraction import scrape_url
from web_search import web_search

# Initialize API clients
GROQ_API_KEY = os.getenv('GROQ_API_KEY', 'YOUR_GROQ_API_KEY')
FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY', 'YOUR_FIRECRAWL_API_KEY')

groq_client = GroqClient(api_key_env_var='GROQ_API_KEY', model='llama3-8b-8192')
firecrawl_client = FireCrawlClient(api_key=FIRECRAWL_API_KEY)

def main():
    st.title("Corrective RAG Application")

    # User inputs
    url = st.text_input("Enter URL:")
    query = st.text_input("Enter your question:")
    
    if st.button("Get Answer"):
        if url:
            # Scrape content from URL
            content = scrape_url(url)
        else:
            content = ''
        
        # Generate answer using Llama3 (Groq API)
        answer = groq_client.generate_answer(content, query)
        
        # If answer is insufficient, perform web search
        if not answer:
            search_results = web_search(query)
            combined_content = " ".join([result['content'] for result in search_results])
            answer = groq_client.generate_answer(combined_content, query)
        
        st.write("Answer:", answer)

if __name__ == "__main__":
    main()
