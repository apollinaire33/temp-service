from celery import Celery

from temp_service.core.config import settings

app = Celery('temp_service_beat')
app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = settings.CELERY_BEAT_SCHEDULE
