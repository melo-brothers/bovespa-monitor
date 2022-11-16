from fastapi import APIRouter, FastAPI

from views import assets_router, user_router
from views_sync import sync_router

app = FastAPI()
router = APIRouter()


@router.get("/")
def first():
    return {"msg": "Hello World"}


app.include_router(prefix="/first", router=router)
app.include_router(user_router)
app.include_router(assets_router)
app.include_router(sync_router)
