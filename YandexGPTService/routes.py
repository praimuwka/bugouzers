from fastapi import APIRouter

from YandexGPTService.client import GPTClient
from edPrograms.schemas import SpecSchema

router = APIRouter(prefix="/gpt")

gpt_client = GPTClient()



@router.post("/get_job")
async def get_job(spec: SpecSchema):
    return await gpt_client.get_appropriate_jobs(spec.name)


@router.post("/compare_specs")
async def compare_specs(spec1: SpecSchema, spec2: SpecSchema):
    return await gpt_client.compare_specs(spec1, spec2)

