import requests
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup

# Initialize Flask application
app = Flask(__name__)

# --- Tool Definition: Web Scraper ---
# This function takes a URL, fetches its content, and extracts all headings.

def scrape_headings(url):
    """
    Scrapes a webpage for all heading tags (h1, h2, h3, etc.).

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        dict: A dictionary containing lists of headings, categorized by tag.
              Returns an error message if scraping fails.
    """
    try:
        # Fetch the content from the URL
        response = requests.get(url, timeout=10)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all heading tags
        headings = {
            'h1': [h.get_text(strip=True) for h in soup.find_all('h1')],
            'h2': [h.get_text(strip=True) for h in soup.find_all('h2')],
            'h3': [h.get_text(strip=True) for h in soup.find_all('h3')],
            'h4': [h.get_text(strip=True) for h in soup.find_all('h4')],
        }
        return headings

    except requests.exceptions.RequestException as e:
        return {'error': f"Request failed: {e}"}
    except Exception as e:
        return {'error': f"An unexpected error occurred: {e}"}

# --- MCP Server Endpoint ---
# This endpoint exposes the web scraper tool to be used by an external agent.
@app.route('/scrape', methods=['POST'])
def handle_scrape():
    """
    Flask endpoint to handle scraping requests.
    Expects a JSON payload with a 'url' key.
    e.g., {"url": "http://example.com"}
    """
    # Get the JSON data from the request
    data = request.get_json()

    # Check if the 'url' key is present
    if not data or 'url' not in data:
        return jsonify({'error': "Missing 'url' in request payload."}), 400

    url_to_scrape = data['url']
    
    # Call the scraping tool
    scraped_data = scrape_headings(url_to_scrape)

    # Return the result as JSON
    if 'error' in scraped_data:
        return jsonify(scraped_data), 500
    else:
        return jsonify(scraped_data), 200

# --- Server Entry Point ---
if __name__ == '__main__':
    # Run the Flask app
    # Note: In a production environment, use a proper WSGI server like Gunicorn.
    app.run(host='0.0.0.0', port=5000, debug=True)

# Example of how to run this server and test it:
# 1. Run this script: `python mcp_server.py`
# 2. In a separate terminal, you can use curl to test the endpoint:
#    curl -X POST -H "Content-Type: application/json" -d '{"url": "https://www.google.com"}' http://localhost:5000/scrape