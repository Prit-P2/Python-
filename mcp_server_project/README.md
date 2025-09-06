
# Educational MCP Server for Web Scraping

This project is a simple, educational implementation of a Model Context Protocol (MCP) server in Python. It is designed to demonstrate how an external agent (like an AI model) can leverage a tool-providing server to perform tasks it cannot do on its own, such as accessing live web data.

This server exposes a single tool via a REST API: a web scraper that can extract all headings from a given URL.

## Core Concepts

An MCP server acts as a secure and controlled gateway for AI models to interact with the outside world. Instead of granting an AI direct access to the internet or sensitive systems, the AI can make requests to an MCP server that offers a pre-approved set of "tools."

This project is inspired by research into Tool-Augmented Language Models (TALM), which have shown that enabling Large Language Models (LLMs) to use external tools significantly enhances their capabilities.

## Project Structure

- `mcp_server.py`: The main Flask application that runs the server and exposes the `/scrape` endpoint.
- `client_example.py`: A simple Python script that acts as the "agent" or "AI," calling the server to request a scraping job.
- `requirements.txt`: A list of the necessary Python libraries.
- `README.md`: This documentation file.

## Setup and Usage

### 1. Create a Virtual Environment

It is highly recommended to run this project in a dedicated Python virtual environment.

```bash
# Navigate to the project directory
cd mcp_server_project

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS and Linux:
source venv/bin/activate
# On Windows:
# .\venv\Scripts\activate
```

### 2. Install Dependencies

Install the required libraries using pip and the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 3. Run the MCP Server

Start the Flask server. It will listen on `localhost` at port `5000`.

```bash
python mcp_server.py
```

You should see output indicating that the server is running.

### 4. Run the Client

In a **new terminal window** (while the server is still running), run the example client script. This script will call the server and ask it to scrape `example.com`.

```bash
# Make sure your virtual environment is activated in this terminal as well
source venv/bin/activate

python client_example.py
```

You will see the client send a request and then print the JSON data it receives back from the server.

## Publication Details and References

This project, while simple, is grounded in the following academic and technical principles.

### Academic Research

The foundational concept of AI models using external tools is a significant area of modern AI research. This approach allows models to access real-time, dynamic information and perform complex calculations, overcoming the limitations of their static training data.

- **Primary Reference**: A key paper in this field is **"TALM: Tool Augmented Language Models"** by Parisian et al. (2022). This paper introduces a method for teaching language models to use external tools through a text-only interface and demonstrates significant performance improvements on knowledge-intensive tasks.
  - **Link**: [https://arxiv.org/abs/2205.12255](https://arxiv.org/abs/2205.12255)

### Technical Documentation (Libraries Used)

The server and client are built using standard, well-documented Python libraries.

- **Flask**: A lightweight WSGI web application framework used to create the server and its API endpoint.
  - **Docs**: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

- **Requests**: A simple, yet powerful, HTTP library for Python, used by the client to make requests to the server and by the server to fetch web pages.
  - **Docs**: [https://requests.readthedocs.io/](https://requests.readthedocs.io/)

- **Beautiful Soup**: A library for pulling data out of HTML and XML files. It is used in our server's scraping tool to parse the HTML from a URL.
  - **Docs**: [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
