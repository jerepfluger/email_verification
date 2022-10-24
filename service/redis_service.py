import json
import uuid

from client.redis_client import RedisClient
from helpers.logger import logger


class RedisService:
    def __init__(self):
        self.redis_client = RedisClient()

    def save_info(self, object_to_store, expiry=None):
        uu_id = uuid.uuid4()
        logger.info(f'Saving object to redis with Key {uu_id}')
        self.redis_client.save_key_value(str(uu_id), json.dumps(object_to_store), expiry)

        return uu_id

    def get_info(self, key):
        logger.info(f'Retrieving redis info for Key {key}')
        return self.redis_client.get_value(key)
