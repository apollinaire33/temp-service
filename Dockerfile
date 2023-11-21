FROM python:3.10-alpine AS base

WORKDIR usr/src/temp_service
COPY ./requirements ./requirements

RUN pip install --no-cache-dir --upgrade -r requirements/base.txt -r requirements/prod.txt

COPY . .
CMD alembic upgrade head

FROM base as prod

CMD uvicorn temp_service.main:app --reload  --host 0.0.0.0
EXPOSE 8000