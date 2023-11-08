from pydantic import BaseModel, validator, ValidationError
from datetime import datetime

class EmployeeModel(BaseModel):
    id: int
    name: str
    datetime: str
    department_id: int
    job_id: int

    @validator('datetime')
    def validate_datetime(cls, v):
        try:
            # This will raise an error if the datetime is not in ISO format
            return datetime.fromisoformat(v)
        except ValueError:
            raise ValueError('datetime must be in ISO 8601 format')

class DepartmentModel(BaseModel):
    id: int
    department: str 

class JobModel(BaseModel):
    id: int
    job: str
