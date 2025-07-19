from celery import Celery

# In a real app, this would come from a config file
REDIS_URL = "redis://localhost:6379/0"

app = Celery(
    "tasks",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["tasks"],
)

if __name__ == "__main__":
    app.start()
