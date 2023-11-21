from fastapi import FastAPI

from temp_service.api.routers import router
from temp_service.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(router)