from datetime import timedelta


MONGO_URI = "mongodb://127.0.0.1:27017/mydb"
CELERY_BROKER_URL = ("redis://localhost:6379",)
CELERY_RESULT_BACKEND = "redis://localhost:6379"
CACHE_REDIS_HOST = "127.0.0.1"
CACHE_REDIS_PORT = 6379
CACHE_REDIS_DB = 1

