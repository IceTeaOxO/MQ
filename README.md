
### worker
```
linux
celery -A AppCelery worker --loglevel=info
```
```
windows
celery -A AppCelery worker --concurrency=4 --loglevel=info -P threads

$ celery help

$ celery multi start w1 -A proj -l info
$ celery multi stop w1 -A proj -l info
$ celery multi stopwait w1 -A proj -l info
```
### use task
```
>>> from tasks import add
>>> add.delay(4, 4)
>>> add.apply_async((2, 2), queue='lopri', countdown=10)
>>> result = add.delay(4, 4)
>>> result.get(timeout=1)
>>> result.id
>>> result.state
```
### store result
```
app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')
```
可以用redis作為後端

### celery設計工作流程
```
>>> s1 = add.s(2, 2)
>>> res = s1.delay()
>>> res.get()

```

# Resource
https://www.celerycn.io/ru-men/celery-chu-ci-shi-yong


# RabbitMQ
Docker
```
# create and start container
docker run --rm --name rabbitmq -p 5672:5672 -p 15672:15672 \
-e RABBITMQ_DEFAULT_USER=root -e RABBITMQ_DEFAULT_PASS=1234 rabbitmq:management 
```
```
# create and start container
docker-compose -f docker-compose.yml up

```