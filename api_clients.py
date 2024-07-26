
# pip install langchain streamlit groq tavily firecrawl requests beautifulsoup4
import os
from groq import Groq
from firecrawl import FirecrawlApp

class GroqClient:
    def __init__(self, api_key_env_var, model):
        self.api_key = os.environ.get(api_key_env_var)
        self.model = model
        self.client = Groq(api_key=self.api_key)

    def generate_answer(self, content, query):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "user", "content": query}
            ],
            model=self.model
        )
        return chat_completion.choices[0].message.content


class FireCrawlClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.app = FirecrawlApp(api_key=self.api_key)

    def crawl_url(self, url, options={}):
        crawl_result = self.app.crawl_url(url, options)
        return crawl_result

    def check_crawl_status(self, job_id):
        status = self.app.check_crawl_status(job_id)
        return status

    def scrape_url(self, url):
        content = self.app.scrape_url(url)
        return content
