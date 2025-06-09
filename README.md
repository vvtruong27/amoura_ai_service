# Amoura AI Service

This is the backend AI Service module for the Amoura online dating application. This module is built with FastAPI and is responsible for providing APIs for the application's Artificial Intelligence (AI) based features, including:

*   **AI Matching Support (E2):** Suggest suitable matches, display common interests.
*   **AI Communication Behavior Analysis (E3):** Analyze message sentiment, suggest conversation topics.
*   **AI Content Moderation & User Safety (E4):** Filter inappropriate messages, validate user names.

This module is designed to operate independently or as a microservice, interacting with the main backend of the Amoura application.

## 📂 Directory Structure

```text
amoura_ai_service/
├── app/                                # Main source code of the FastAPI application
│   ├── __init__.py
│   ├── ai_models/                      # Machine learning models and preprocessors
│   │   ├── __init__.py
│   │   ├── model_loader.py
│   │   └── ml_models/
│   │       ├── best_model_summary.json
│   │       ├── best_overall_model.joblib
│   │       └── preprocessors/          # Feature transformers and encoders
│   │
│   ├── api/                            # API routers
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── api.py                  # Aggregation of v1 routers
│   │       └── endpoints/              # Endpoint route handlers
│   │           ├── __init__.py
│   │           ├── ai_matching.py
│   │           ├── ai_communication.py
│   │           └── ai_moderation.py
│   │
│   ├── core/                           # Configuration and settings
│   │   ├── __init__.py
│   │   └── config.py
│   │
│   ├── db/                             # Database utilities and session setup
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── base_class.py
│   │   └── session.py
│   │
│   ├── models/                         # Pydantic models for request/response
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── communication.py
│   │   ├── db_models.py
│   │   ├── matching.py
│   │   └── moderation.py
│   │
│   ├── services/                       # Core logic and orchestration layer
│   │   ├── __init__.py
│   │   ├── communication_analysis_service.py
│   │   ├── content_moderation_service.py
│   │   ├── feature_engineering_service.py
│   │   └── matching_service.py
│   │
│   └── utils/                          # Shared utility functions
│       ├── __init__.py
│       └── main.py                     # Entry point for FastAPI app
│
├── test/                               # Unit and integration tests
│   ├── __init__.py
│   └── test_api/
│       ├── __init__.py
│       └── v1/
│           ├── __init__.py
│           ├── test_ai_matching.py
│           ├── test_ai_communication.py
│           └── test_ai_moderation.py
│
├── .env                                # Environment variables (local use)
├── .env.example                        # Template environment config
├── .gitignore                          # Git ignore rules
├── README.md                           # Project description and instructions
└── requirements.txt                    # List of Python dependencies

```
## 📋 Prerequisites

*   Python 3.12+
*   Pip (Python package installer)
*   Git

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/vvtruong27/amoura_ai_service
cd amoura_ai_service
```
### 2. Create and Activate Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

**For Windows:**

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**For macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, you'll see (.venv) at the beginning of the command line.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The requirements.txt file contains a list of all Python libraries needed for the project.

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

Open the .env file and update the necessary values (e.g., API keys for third-party AI services if any, paths to models, etc.).

### 5. Run the Application (Development)

```bash
uvicorn app.main:app --reload
```

*   **app.main:app:** Points to the FastAPI app instance in the app/main.py file.
*   **--reload:** Automatically reloads the server when code changes (only for development).

After the server starts, you can access the application at: http://localhost:8000

## 📖 API Documentation (Swagger UI & ReDoc)

FastAPI automatically generates interactive API documentation. Once the application is running, you can access:

* **Swagger UI**: http://localhost:8000/docs
* **ReDoc:** http://localhost:8000/redoc

Here, you can view all endpoints, request/response schemas, and test the API directly.

## 🧪 Running Tests

The project uses pytest for testing. To run all tests:

```bash
pytest
```
