import uuid

from client.redis_client import RedisClient
from helpers.logger import logger


class RedisService:
    def __init__(self):
        self.redis_client = RedisClient()

    def save_info(self, object_to_store):
        uu_id = uuid.uuid4()
        logger.info(f'Saving object to redis with Key {uu_id} and Value {object_to_store}')

        return uu_id
