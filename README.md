# FastAPI Motor Clean Architecture

This project is a FastAPI application that utilizes Motor as the asynchronous driver for MongoDB, following a clean architecture structure. 

## Project Structure

```
fastapi-motor-clean-arch
├── app
│   ├── api
│   │   ├── deps.py
│   │   └── v1
│   │       └── endpoints.py
│   ├── core
│   │   ├── config.py
│   │   └── database.py
│   ├── models
│   │   └── user.py
│   ├── repositories
│   │   └── user_repository.py
│   ├── schemas
│   │   └── user_schema.py
│   ├── services
│   │   └── user_service.py
│   ├── main.py
│   └── utils
│       └── security.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-motor-clean-arch.git
   cd fastapi-motor-clean-arch
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Update the configuration settings in `app/core/config.py` to match your environment, including MongoDB connection details.

## Running the Application

To start the FastAPI application, run:
```
uvicorn app.main:app --reload
```

You can access the API documentation at `http://127.0.0.1:8000/docs`.

## Usage

The application provides endpoints for user management, including creating, reading, updating, and deleting users. Refer to the API documentation for detailed usage instructions.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.