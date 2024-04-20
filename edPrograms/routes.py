from fastapi import APIRouter

from base_parser import PlanParser
from const import PLAN_PATH
from edPrograms.schemas import EntrantSchema

router = APIRouter(prefix="/programs", tags=["Education programs"])


@router.post("/getPrograms")
async def get_programs(entrant_data: EntrantSchema):
    object = PlanParser(entrant_data, file_path=PLAN_PATH)
    return object.get_education_programs()