from app.config.database import database

member_collection = database["members"]


async def create_member(data: dict):

    total_members = await member_collection.count_documents({})

    member = {
        "id": f"MEM{total_members + 1:03}",
        **data
    }

    result = await member_collection.insert_one(member)

    member["_id"] = str(result.inserted_id)

    return member


async def get_member(member_id: str):

    member = await member_collection.find_one(
        {"id": member_id},
        {"_id": 0}
    )

    return member