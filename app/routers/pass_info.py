from fastapi import APIRouter
from models.pass_info import PassInfo

router = APIRouter()


@router.get("/pass_infos", tags=["pass_infos"])
async def get_collection_pass_infos():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.post("/pass_infos", tags=["pass_infos"])
async def post_pass_infos(item: PassInfo):
    return item


@router.get("/pass_infos/{id}", tags=["pass_infos"])
async def get_pass_infos(id: int):
    return {"id": id}

@router.put("/pass_infos/{id}", tags=["pass_infos"])
async def put_pass_infos(id: int, item: PassInfo):
    return item

@router.patch("/pass_infos/{id}", tags=["pass_infos"])
async def patch_pass_infos(id: int, item: PassInfo):
    return item

@router.delete("/pass_infos/{id}", tags=["pass_infos"])
async def delete_pass_infos(id: int, item: PassInfo):
    return item