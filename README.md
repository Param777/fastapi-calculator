# FastAPI Calculator

This is a simple calculator application built using FastAPI. It provides endpoints for basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Project Structure

```
fastapi-calculator
├── app
│   ├── main.py          # Entry point of the FastAPI application
│   ├── api
│   │   └── calculator.py # Defines calculator operations endpoints
│   └── models
│       └── __init__.py  # Placeholder for data models or schemas
├── requirements.txt      # Lists project dependencies
├── Dockerfile             # Instructions to build the Docker image
└── README.md              # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-calculator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   uvicorn app.main:app --reload

   ```
    To run uvicorn using the Python module

    ```
   python -m uvicorn app.main:app --reload

    ```

## Usage

Once the application is running, you can access the calculator endpoints at `http://localhost:8000/docs` to see the available operations and test them.

## Docker

To build and run the application using Docker, follow these steps:

1. Build the Docker image:
   ```
   docker build -t fastapi-calculator .
   ```

2. Run the Docker container:
   ```
   docker run -d -p 8000:8000 fastapi-calculator
   ```

You can then access the application at `http://localhost:8000/docs`.

## License

This project is licensed under the MIT License.