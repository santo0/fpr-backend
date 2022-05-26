try:
    from flask import Flask
    import boto3
    from celery import Celery
    import pymongo
except Exception as e:
    print("Error  :{} ".format(e))

app = Flask(__name__)

backend_uri = 'db+postgresql://localhost:5433/postgres'

simple_app = Celery('simple_worker',
                    broker='amqp://admin:mypass@rabbit:5672',
                    backend='mongodb://mongodb_container:27017/mydb')


@app.route('/simple_start_task', methods=['POST'])
def call_method():
    app.logger.info("Invoking Method ")
    r = simple_app.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
    app.logger.info(r.backend)
    return r.id


@app.route('/simple_task_status/<task_id>', methods=['GET'])
def get_status(task_id):
    status = simple_app.AsyncResult(task_id, app=simple_app)
    print("Invoking Method ")
    return "Status of the Task " + str(status.state)


@app.route('/simple_task_result/<task_id>', methods=['GET'])
def task_result(task_id):
    result = simple_app.AsyncResult(task_id).result
    return "Result of the Task " + str(result)


@app.route('/')
def index():
    return "I'm working!"
