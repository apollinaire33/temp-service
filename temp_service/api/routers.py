from fastapi import APIRouter

from temp_service.api.v1.temp import temp_service_router

router = APIRouter()
router.include_router(router=temp_service_router)
