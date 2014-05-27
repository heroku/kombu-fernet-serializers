from celery import Celery
from kombu_fernet.serializers.json import MIMETYPE

app = Celery('tasks', broker='redis://', backend='redis://')
app.conf.update(
    CELERY_TASK_SERIALIZER='fernet_json',
    CELERY_RESULT_SERIALIZER='fernet_json',
    CELERY_ACCEPT_CONTENT=[MIMETYPE],
)

@app.task
def add(x, y):
    return x + y
