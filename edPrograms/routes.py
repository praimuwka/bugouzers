from fastapi import APIRouter

from edPrograms.schemas import EntrantSchema

router = APIRouter(prefix="/programs", tags=["Education programs"])


@router.post("/getPrograms")
async def get_programs(entrant_data: EntrantSchema):
    return entrant_data
