from typing import List
from bson import ObjectId
from models.pass_info import PassInfo, PassInfoUpdate
from pymongo.collection import ReturnDocument
from fastapi.encoders import jsonable_encoder
from config.config import db

config = {
            "id": {'$toString': "$_id"},
            "_id": 0,
            "datetime": 1,
            "number": 1,
            "entry": 1,
            "car_type": 1,
            "photo": 1,
        }

async def find() -> List[PassInfo]:
    items = await db["pass_infos"].find({}, config).to_list(None)
    return items

async def add(item: PassInfo) -> PassInfo:
    item = jsonable_encoder(item)
    item = await db["pass_infos"].insert_one(item)
    item = await db["pass_infos"].find_one({"_id": item.inserted_id}, config)
    return item

async def find_one(id: ObjectId) -> PassInfo:
    item = await db["pass_infos"].find_one({"_id": id}, config)
    return item

async def replace(id: ObjectId, item: PassInfo) -> PassInfo:
    item = jsonable_encoder(item)
    item = await db["pass_infos"].find_one_and_replace(
        {"_id": ObjectId(id)},
        item,
        config,
        return_document=ReturnDocument.AFTER
    )
    return item

async def update(id: ObjectId, item: PassInfoUpdate) -> PassInfo:
    item = jsonable_encoder(item.dict(exclude_unset=True))
    item = await db["pass_infos"].find_one_and_update(
        {"_id": ObjectId(id)}, 
        {'$set': item}, 
        config, 
        return_document=ReturnDocument.AFTER
    )
    return item


async def delete(id: ObjectId) -> PassInfo:
    item = await db["pass_infos"].find_one_and_delete(
        {"_id": ObjectId(id)}
    )
    return item

