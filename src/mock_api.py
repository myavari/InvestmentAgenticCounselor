from openai import OpenAI
import os
from dotenv import load_dotenv

def mock_api(api_name, query, num_results=20):
    """
    Parameters:
    api_name (str): The name of the API to simulate (e.g., "twitter", "newsdata", "tiingo").
    query (str): The query string to simulate the API response for.
    num_results (int, optional): The number of results to include in the simulated response. Defaults to 20.

    Returns:
    str: The simulated API response as a string.
    """
    # Define the prompt
    if (api_name == "twitter"):
        prompt = f"""
        Simulate a Twitter API response to the query {query}. Provide exactly {num_results} tweets in the response. 
        Format the response in the same structure as the official Twitter API, including fields like id, text, 
        author_id, and created_at. Do not include any explanations or additional commentary, and act as if you 
        are the Twitter API server responding to a live request.
        """
    elif api_name == "newsdata":
        prompt = f"""
        Simulate a NewsData.io API response to the query {query}. Provide exactly {num_results} news articles in the response. 
        Format the response in the same structure as the official NewsData.io API, including fields like title, link, 
        source_id, pubDate, and description. Do not include any explanations or additional commentary, and act as 
        if you are the NewsData.io API server responding to a live request.
        """
    elif api_name == "tiingo":
        prompt = f"""
        Simulate a Tiingo API response to the query {query}. Provide exactly {num_results} stock price entries in the response. 
        Format the response in the same structure as the official Tiingo API, including fields like date, close, high, 
        low, open, and volume. Do not include any explanations or additional commentary, and act as if you are the 
        Tiingo API server responding to a live request.
        """
    
    # Load environment variables
    load_dotenv()

    # Initialize OpenAI client
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    except Exception as e:
        print(f"Failed to initialize OpenAI client: {e}")
        exit(0)
    
    # OpenAI API call
    response = client.chat.completions.create(model="gpt-4o",  # Replace with "gpt-3.5-turbo" if needed for cost-efficiency
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7)
    return response.choices[0].message.content