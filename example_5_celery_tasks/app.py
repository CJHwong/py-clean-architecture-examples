from core.l3_interface_adapters.presenters.task_presenter import TaskPresenter
from core.l4_frameworks_and_drivers.flask_dependencies import (
    create_get_task_status_use_case,
    create_submit_task_use_case,
)
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/tasks", methods=["POST"])
def submit_task():
    payload = request.get_json()
    use_case = create_submit_task_use_case()
    task = use_case.execute(payload)
    return jsonify(TaskPresenter.to_dict(task)), 202


@app.route("/tasks/<string:task_id>", methods=["GET"])
def get_task_status(task_id: str):
    use_case = create_get_task_status_use_case()
    task = use_case.execute(task_id)
    if task:
        return jsonify(TaskPresenter.to_dict(task))
    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run()
