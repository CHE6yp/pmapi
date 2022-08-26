import os
from fastapi import APIRouter, status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from models.pass_info import PassInfo, PassInfoUpdate
from pymongo.collection import ReturnDocument
from helpers.base64_validator import isBase64
from bson import ObjectId
from config.config import db

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
async def get_collection_pass_infos():
    items = await db["pass_infos"].find({}, config).to_list(100)
    return items

@router.post("/pass_infos")
async def post_pass_infos(item: PassInfo):
    item = jsonable_encoder(item)
    new_item = await db["pass_infos"].insert_one(item)
    created_item = await db["pass_infos"].find_one({"_id": new_item.inserted_id}, config)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_item)

@router.get("/pass_infos/{id}")
async def get_pass_infos(id: str):
    if isBase64(id) == False:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    item = await db["pass_infos"].find_one({"_id": ObjectId(id)}, config)

    if item == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return item

@router.put("/pass_infos/{id}")
async def put_pass_infos(id: str, item: PassInfo):
    if isBase64(id) == False:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    item = jsonable_encoder(item)
    item = await db["pass_infos"].find_one_and_replace(
        {"_id": ObjectId(id)}, 
        item, 
        config, 
        return_document=ReturnDocument.AFTER
    )

    if item == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return item

@router.patch("/pass_infos/{id}")
async def patch_pass_infos(id: str, item: PassInfoUpdate):
    if isBase64(id) == False:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    item = jsonable_encoder(item.dict(exclude_unset=True))
    item = await db["pass_infos"].find_one_and_update(
        {"_id": ObjectId(id)}, 
        {'$set': item}, 
        config, 
        return_document=ReturnDocument.AFTER
    )

    if item == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return item

@router.delete("/pass_infos/{id}")
async def delete_pass_infos(id: str):
    if isBase64(id) == False:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    item = await db["pass_infos"].find_one_and_delete(
        {"_id": ObjectId(id)}
    )
    if item == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
