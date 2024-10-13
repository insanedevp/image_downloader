# Image Downloader API

A FastAPI application to download and resize images from Google search queries, storing them in a PostgreSQL database.

## Features
- Fetch images using Google Custom Search API
- Download and resize images asynchronously
- Store images in PostgreSQL
- Dockerized for easy setup
- Includes unit tests

## Prerequisites
- Python 3.8+
- PostgreSQL
- Google API Key and Custom Search Engine ID
- Docker (optional)
- Git

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/image_downloader.git
cd image_downloader
```

### 2. Set Up Environment Variables
Create a `.env` file:

```bash
touch .env
```

Add your credentials to the `.env` file:

```
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_custom_search_engine_id
DATABASE_URL=postgresql://username:password@host:port/database_name
```

### 3. Install Dependencies
Create a virtual environment and install requirements:

```bash
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Set Up the Database
Ensure PostgreSQL is installed and running.

Create the database tables:

```bash
python create_tables.py
```

## Running the Application

### Without Docker
Start the application using Uvicorn:

```bash
uvicorn app:app --reload
```

Access the API at [http://localhost:8000](http://localhost:8000).

### With Docker
Build and run the Docker container:

```bash
docker-compose up --build
```

## Usage
Send a POST request to download and resize images:

**Endpoint:**
```
POST http://localhost:8000/download-images/
```

**Request Body Example:**
```json
{
  "query": "cute kittens",
  "max_images": 5,
  "resize_width": 800,
  "resize_height": 600
}
```

## Running Tests
Execute tests using pytest:

```bash
pytest
```

## Project Structure
- **app.py**: FastAPI application
- **utils.py**: Image processing utilities
- **models.py**: Database models
- **schemas.py**: Request and response models
- **database.py**: Database connection setup
- **create_tables.py**: Script to create database tables
- **tests/**: Contains unit tests
- **Dockerfile** and **docker-compose.yml**: Docker configuration
- **requirements.txt**: Python dependencies

---
Feel free to reach out if you have any questions or issues while setting up the project!

