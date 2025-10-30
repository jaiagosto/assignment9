# main.py

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field, field_validator
from fastapi.exceptions import RequestValidationError
from app.operations import add, subtract, multiply, divide
import uvicorn
import logging

# Setting up logging so we can track what's happening in the app
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the FastAPI app instance
app = FastAPI()

# Tell FastAPI where to find our HTML templates
templates = Jinja2Templates(directory="templates")

# Define what data we expect in requests using Pydantic
class OperationRequest(BaseModel):
    a: float = Field(..., description="The first number")
    b: float = Field(..., description="The second number")

    @field_validator('a', 'b')
    def validate_numbers(cls, value):
        # Make sure both values are actually numbers
        if not isinstance(value, (int, float)):
            raise ValueError('Both a and b must be numbers.')
        return value

# Define what a successful response looks like
class OperationResponse(BaseModel):
    result: float = Field(..., description="The result of the operation")

# Define what an error response looks like
class ErrorResponse(BaseModel):
    error: str = Field(..., description="Error message")

# Handle HTTP exceptions and log them
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTPException on {request.url.path}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )

# Handle validation errors when request data is invalid
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Get all the error messages from the validation
    error_messages = "; ".join([f"{err['loc'][-1]}: {err['msg']}" for err in exc.errors()])
    logger.error(f"ValidationError on {request.url.path}: {error_messages}")
    return JSONResponse(
        status_code=400,
        content={"error": error_messages},
    )

@app.get("/")
async def read_root(request: Request):
    """
    Show the calculator homepage.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/add", response_model=OperationResponse, responses={400: {"model": ErrorResponse}})
async def add_route(operation: OperationRequest):
    """
    Endpoint to add two numbers.
    """
    try:
        result = add(operation.a, operation.b)
        logger.info(f"Addition: {operation.a} + {operation.b} = {result}")
        return OperationResponse(result=result)
    except Exception as e:
        logger.error(f"Add Operation Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/subtract", response_model=OperationResponse, responses={400: {"model": ErrorResponse}})
async def subtract_route(operation: OperationRequest):
    """
    Endpoint to subtract two numbers.
    """
    try:
        result = subtract(operation.a, operation.b)
        logger.info(f"Subtraction: {operation.a} - {operation.b} = {result}")
        return OperationResponse(result=result)
    except Exception as e:
        logger.error(f"Subtract Operation Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/multiply", response_model=OperationResponse, responses={400: {"model": ErrorResponse}})
async def multiply_route(operation: OperationRequest):
    """
    Endpoint to multiply two numbers.
    """
    try:
        result = multiply(operation.a, operation.b)
        logger.info(f"Multiplication: {operation.a} * {operation.b} = {result}")
        return OperationResponse(result=result)
    except Exception as e:
        logger.error(f"Multiply Operation Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/divide", response_model=OperationResponse, responses={400: {"model": ErrorResponse}})
async def divide_route(operation: OperationRequest):
    """
    Endpoint to divide two numbers.
    """
    try:
        result = divide(operation.a, operation.b)
        logger.info(f"Division: {operation.a} / {operation.b} = {result}")
        return OperationResponse(result=result)
    except ValueError as e:
        # This catches our divide by zero error specifically
        logger.error(f"Divide Operation Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Divide Operation Internal Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Health check endpoint for Docker
@app.get("/health")
async def health_check():
    """
    Simple health check to confirm the app is running.
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)