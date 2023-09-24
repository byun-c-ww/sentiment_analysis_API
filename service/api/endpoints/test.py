from fastapi import APIRouter

test_router = APIRouter()

@test_router.get('/test')
async def testing(text:str):
    return {"testing":"testing"}