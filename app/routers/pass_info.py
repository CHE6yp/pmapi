import os
from fastapi import APIRouter, status
from fastapi.responses import Response, JSONResponse
from bson import ObjectId
from models.pass_info import PassInfo, PassInfoUpdate
from database.pass_info import *
from beanie import PydanticObjectId

router = APIRouter()

@router.get("/pass_infos")
async def get_pass_infos():
    return await find()

@router.post("/pass_infos", status_code=201)
async def post_pass_info(item: PassInfo):
    item = await add(item)
    return item

@router.get("/pass_infos/{id}")
async def get_pass_info(id: PydanticObjectId):
    item = await find_one(id)

    if item == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return item

@router.put("/pass_infos/{id}")
async def put_pass_info(id: PydanticObjectId, item: PassInfo): 
    item = await replace(id, item)

    if item == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return item

@router.patch("/pass_infos/{id}")
async def patch_pass_info(id: PydanticObjectId, item: PassInfoUpdate):
    item = await update(id, item)

    if item == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return item

@router.delete("/pass_infos/{id}")
async def delete_pass_info(id: PydanticObjectId):
    item = await delete(id)

    if item == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
