import os
from exception.exception_handler import AppException 
from dotenv import load_dotenv
import fitz  # PyMuPDF
from openai import OpenAI
from apify_client import ApifyClient

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize the ApifyClient with your API token
client = ApifyClient("APIFY_API_TOKEN")


# Get job listings from LinkedIn using a search query and location.
def get_job_from_linkedin(search_query, location = "United Kingdom", num_results = 50):
    run_input = {
        "title": search_query,
        "location": location,
        "rows": num_results,
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"]
        }
    }
    run = client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
    job = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    if not job:
        raise AppException("No job listings found for the given search query and location.")
    return job

# Get job listings from Indeed using a search query and location.
def get_job_from_indeed(search_query, location = "United Kingdom", num_results = 50):
    run_input = {
        "query": search_query,
        "country": location,
        "maxRows": num_results,
        "sort": "relevance",
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"]
        }
    }

    run = client.actor("MXLpngmVpE8WTESQr").call(run_input=run_input)

    job = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    if not job:
        raise AppException("No job listings found for the given search query and location.")
    return job