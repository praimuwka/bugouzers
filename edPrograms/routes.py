from fastapi import APIRouter

from base_parser import ProgramsParser
from const import PLAN_PATH
from edPrograms.schemas import EntrantSchema, SpecSchema
from edPrograms.service import get_disciplines, get_all_programms, get_new_subj

router = APIRouter(prefix="/programs", tags=["Education programs"])


@router.get("/get_all_programs")
def getAllProgramss():
    return get_all_programms()


@router.post("/getPrograms")
async def get_programs(entrant_data: EntrantSchema):
    object = ProgramsParser(entrant_data, file_path=PLAN_PATH)
    return object.get_education_programs()


@router.post("/getDisciplines")
async def get_disciplines_info(spec_name: SpecSchema):
    return get_disciplines(spec_name.name)


@router.post("/getDisciplinesDiff")
async def get_disciplines_info(old: SpecSchema, new: SpecSchema):
    old = get_disciplines(old.name, is_subject=True)
    new = get_disciplines(new.name, is_subject=True)
    return get_new_subj(old, new)
