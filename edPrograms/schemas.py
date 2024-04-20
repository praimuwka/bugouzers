from enum import Enum
from typing import List, Annotated, Optional

from annotated_types import Le, Gt
from pydantic import BaseModel, field_validator


class ExamNameEnum(str, Enum):
    math = "math"
    rus_lang = "rus"
    physic = "phys"
    informatics = "informatics"

class ExamInfo(BaseModel):
    name: ExamNameEnum
    mark: Annotated[int, Le(100), Gt(0)]

class EntrantSchema(BaseModel):
    is_budget:bool
    jobs: Optional[List[str]] = None
    exams: List[ExamInfo]
    @field_validator("exams")
    @classmethod
    def no_duplicate_exams(cls, exams):
        entrant_exams = []
        for i in exams:
            if i.name in entrant_exams:
                raise ValueError("Duplicate in exams !")
            entrant_exams.append(i.name)
        return exams


