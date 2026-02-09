from pydantic import BaseModel
from typing import List, Dict

class Step(BaseModel):
    type: str
    entity: str
    update: Dict

class Workflow(BaseModel):
    name: str
    trigger: str
    steps: List[Step]

class WorkflowOutput(BaseModel):
    workflow: Workflow
