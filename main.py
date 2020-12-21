# from redis import Redis
# from rq import Queue

# from my_module import count_words_at_url

# q = Queue(connection=Redis())
# result = q.enqueue(count_words_at_url, 'http://nvie.com')

# from mars import get_mars_photo
# get_mars_photo(1000)


from test1 import count_words_at_url
from rqtester import q
result = q.enqueue(count_words_at_url, 'http://nvie.com')