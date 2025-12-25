from typing import Annotated
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ConfigDict

class Data(BaseModel):
    
    # Using Pydantic Validator
    # For numeric values, use lt or gt for less than and greater than. 
    #       For example, if one of your inputs is age, 
    #       we would expect gt=0 and lt=122 (the age of the oldest ever living person). 
    # We can also validate string objects using arguments like min_length, max_length, and regex.
    feature_1: Annotated[float, Field(gt=0, description="Must be a positive number")]
    feature_2: Annotated[str, Field(description="Text field limited to 280 characters")]
    
    model_config = ConfigDict(json_schema_extra={
        "examples": [{"feature_1": 42.0,"feature_2": "sample text"}],
        "properties": {"feature_2": {"type": "string","maxLength": 280}},
    })
    
app = FastAPI(
    title="Exercise API",
    description="An API that demonstrates checking the values of your inputs.",
    version="1.0.0",
    openapi_version="3.1.0"
)

@app.post("/data/", response_model=Data)
async def ingest_data(data: Data) -> Data:
    # Validation happens automatically through Pydantic
    # Additional business logic can be added here if needed
    return data


# Usage: `uvicorn main:app --reload`
# Run API: http://127.0.0.1:8000/data/
#           Data: {"feature_1": 8.0, "feature_2": "sample text"}
# Return: {"feature_1": 8.0, "feature_2": "sample text"}