Image Downloader API
A FastAPI application to download and resize images from Google search queries, storing them in a PostgreSQL database.

Features
Fetch images using Google Custom Search API
Download and resize images asynchronously
Store images in PostgreSQL
Dockerized for easy setup
Includes unit tests
Prerequisites
Python 3.8+
PostgreSQL
Google API Key and Custom Search Engine ID
Docker (optional)
Git
Installation and Setup
Clone the Repository

bash
Copy code
git clone https://github.com/your-username/image_downloader.git
cd image_downloader
Set Up Environment Variables

Create a .env file:

bash
Copy code
touch .env
Add your credentials:

env
Copy code
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_custom_search_engine_id
DATABASE_URL=postgresql://username:password@host:port/database_name
Install Dependencies

Create a virtual environment and install requirements:

bash
Copy code
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
pip install -r requirements.txt
Set Up the Database

Ensure PostgreSQL is installed and running.

Create the database tables:

bash
Copy code
python create_tables.py
Running the Application
Without Docker
Start the application using Uvicorn:

bash
Copy code
uvicorn app:app --reload
Access the API at http://localhost:8000.

With Docker
Build and run the Docker container:

bash
Copy code
docker-compose up --build
Usage
Send a POST request to:

bash
Copy code
http://localhost:8000/download-images/
Request Body Example:

json
Copy code
{
  "query": "cute kittens",
  "max_images": 5,
  "resize_width": 800,
  "resize_height": 600
}
Running Tests
Execute tests using pytest:

bash
Copy code
pytest
Project Structure
app.py: FastAPI application
utils.py: Image processing utilities
models.py: Database models
schemas.py: Request and response models
database.py: Database connection setup
create_tables.py: Script to create database tables
tests/: Contains unit tests
Dockerfile and docker-compose.yml: Docker configuration
requirements.txt: Python dependencies
