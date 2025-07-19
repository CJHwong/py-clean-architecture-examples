# Example 5: Celery with Clean Architecture

This example demonstrates how to integrate Celery for background task processing into a project following Clean Architecture principles.

The core application (`core/`) is completely decoupled from Celery and Flask. The frameworks are treated as external entry points that use factories from Layer 4 to build and execute use cases.

## Project Structure

```plaintext
example_5_celery_tasks/
├── app.py                  # Flask web server entry point
├── celery_config.py        # Celery app instance and configuration
├── celery_tasks.py         # Celery task definitions (the @task functions)
├── requirements.txt
├── README.md
└── core/
    ├── __init__.py
    ├── l1_entities/
    ├── l2_use_cases/
    ├── l3_interface_adapters/
    └── l4_frameworks_and_drivers/
        ├── celery_dependencies.py
        └── flask_dependencies.py
```

## How to Run

1. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Start Redis:**
    Make sure you have a Redis server running on `localhost:6379`.

3. **Start the Celery Worker:**
    Open a terminal and run the worker:

    ```bash
    celery -A celery_tasks worker --loglevel=info
    ```

4. **Start the Flask Web Server:**
    Open another terminal and run the Flask app:

    ```bash
    python app.py
    ```

5. **Use the Application:**
    * **Submit a task:**

        ```bash
        curl -X POST -H "Content-Type: application/json" -d '{"data": "my important data"}' http://127.0.0.1:5000/tasks
        ```

        This will return a task ID.

    * **Check task status:**
        Use the task ID from the previous step to check the status.

        ```bash
        curl http://127.0.0.1:5000/tasks/<task_id>
        ```

        Initially, the status will be "PENDING". After a few seconds, it will change to "SUCCESS" and show the result.
