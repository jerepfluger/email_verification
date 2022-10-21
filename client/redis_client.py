from os import environ as env

import redis

from config.config import settings as config_file


class RedisClient(object):
    def __init__(self):
        self.instance = redis.Redis(
            host=config_file.redis.host,
            port=config_file.redis.port,
            password=env['REDIS_PASSWORD']
        )

    def save_key_value(self, key, value, expiry):
        self.instance.set(key, value, expiry)

    def get_value(self, key):
        return self.instance.get(key)
