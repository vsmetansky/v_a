import os

ES_HOST = os.getenv('ES_HOST', 'localhost')
ES_USER = os.getenv('ES_USER', 'elastic')
ES_PASS = os.getenv('ES_PASS')
ES_CONNECTIONS_MAX_NUM = os.getenv('ES_CONNECTIONS_MAX_NUM', 100)
ES_STATS_ONLY = os.getenv('ES_STATS_ONLY', True)

PROJECT_NAME = 'v_a'
