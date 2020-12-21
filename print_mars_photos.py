from redis import Redis
from rq import Queue

from mars import get_mars_photo

q = Queue(connection=Redis(host='127.0.0.1', port=6379, db=0))

for i in range(100):
    print('Before')
    q.enqueue(get_mars_photo, 900 + i)
    print('After')
