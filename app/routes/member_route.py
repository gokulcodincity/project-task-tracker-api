from fastapi import APIRouter, HTTPException
from app.schemas.member_schema import MemberCreate
from app.services.member_service import create_member, get_member

router = APIRouter(
    prefix="/members",
    tags=["Members"]
)


@router.post("/")
async def add_member(member: MemberCreate):

    new_member = await create_member(member.dict())

    return {
        "success": True,
        "message": "Member created successfully",
        "data": new_member
    }


@router.get("/{member_id}")
async def fetch_member(member_id: str):

    member = await get_member(member_id)

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    return {
        "success": True,
        "data": member
    }