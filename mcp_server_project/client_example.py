
import requests
import json

# --- Configuration ---
# The address of the running MCP server
MCP_SERVER_URL = "http://127.0.0.1:5000/scrape"

# The URL we want the MCP server to scrape
TARGET_URL = "https://www.python.org"

# --- Client Logic ---
def call_mcp_scraper(server_url, target_url):
    """
    Calls the MCP server's /scrape endpoint to request a scrape job.

    Args:
        server_url (str): The URL of the MCP server's endpoint.
        target_url (str): The URL of the site to be scraped.

    Returns:
        dict: The JSON response from the server.
    """
    print(f"Sending request to MCP server at: {server_url}")
    print(f"Requesting to scrape URL: {target_url}")

    # The payload to send to the server, as expected by the /scrape endpoint
    payload = {"url": target_url}

    try:
        # Make the POST request to the server
        response = requests.post(server_url, json=payload)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Return the JSON response from the server
        return response.json()

    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to connect to MCP server: {e}"}

# --- Main Execution ---
if __name__ == "__main__":
    # Call the function to interact with the server
    result = call_mcp_scraper(MCP_SERVER_URL, TARGET_URL)

    # Pretty-print the JSON result
    print("\n--- Response from MCP Server ---")
    print(json.dumps(result, indent=2))
