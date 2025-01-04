"""

1. Pydantic Models
- Introduction to Pydantic, a data validation library.
- How to create models for request and response validation.
- Defining default values for optional fields.

2. Data Type Annotations
- Using Python type hints (`int`, `str`, `bool`, etc.) for strict data validation.
- Ensuring API inputs and outputs are type-safe.

3. Reusability
- Centralized definition of models for consistent data handling across the application.
- Models can be reused in multiple routes.

Usage in Code
- `Task` model defines the structure of a task (ID, title, description, completed).
- Optional fields like `description` are made nullable using `Optional`.


"""
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
