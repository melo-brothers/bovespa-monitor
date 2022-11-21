from fastapi import APIRouter, FastAPI

from database.connection import sessionmaker
from views import assets_router, user_router
from views_sync import sync_router

app = FastAPI()
router = APIRouter()


async def get_db():
    db = sessionmaker()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def first():
    return {"msg": "Hello World"}


app.include_router(prefix="/first", router=router)
app.include_router(user_router)
app.include_router(assets_router)
app.include_router(sync_router)
