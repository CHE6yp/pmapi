import os
from fastapi import APIRouter, status
from fastapi.responses import Response, JSONResponse
from bson import ObjectId
from models.pass_info import PassInfo, PassInfoUpdate
from database.pass_info import *

router = APIRouter()

config = {
            "id": {'$toString': "$_id"},
            "_id": 0,
            "datetime": 1,
            "number": 1,
            "entry": 1,
            "car_type": 1,
            "photo": 1,
        }

@router.get("/pass_infos")
async def get_pass_infos():
    return await find()

@router.post("/pass_infos")
async def post_pass_info(item: PassInfo):
    item = await add(item)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)

@router.get("/pass_infos/{id}")
async def get_pass_info(id: str):
    if ObjectId.is_valid(id) == False:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    item = await find_one(ObjectId(id))

    if item == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return item

@router.put("/pass_infos/{id}")
async def put_pass_info(id: str, item: PassInfo): 
    if ObjectId.is_valid(id) == False:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    item = await replace(ObjectId(id), item)

    if item == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return item

@router.patch("/pass_infos/{id}")
async def patch_pass_info(id: str, item: PassInfoUpdate):
    if ObjectId.is_valid(id) == False:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    item = await update(ObjectId(id), item)

    if item == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return item

@router.delete("/pass_infos/{id}")
async def delete_pass_info(id: str):
    if ObjectId.is_valid(id) == False:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    item = await delete(ObjectId(id))

    if item == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
