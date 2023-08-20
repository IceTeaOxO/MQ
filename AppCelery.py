from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('tasks',
             broker='amqp://root:1234@127.0.0.1:5672',
             backend='rpc://',
             include=['tasks'])
# backend='file:///tmp/celery_results'
# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)



if __name__ == '__main__':
    app.start()