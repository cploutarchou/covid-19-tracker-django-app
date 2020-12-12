import json
import redis
from datetime import timedelta, datetime

from app.config import config

start_time = datetime.now()


class RedisClient:
    def __init__(self, redis_database: int = None):
        self.connection = None
        if redis_database:
            self.client = self.init_client(redis_db=redis_database)
            print(f"Init connection with redis database {redis_database}")
        else:
            self.client = self.init_client(redis_db=redis_database)
            print(f"Init connection with redis database 0")

    def init_client(self, redis_db: int = None):
        self.connection = redis.ConnectionPool(host=config.redis_db_host, port=config.redis_db_port, db=redis_db)
        return redis.Redis(connection_pool=self.connection)

    def set_key(self, key: str = None, data: dict = None, ttl: int = None):
        try:
            if self.get(redis_key=key) is None:
                self.client.set(name=key, value=data, ex=int(ttl))
                res = self.client.save()
                return res
            else:
                print(f"Redis key {key} already exists")
        except Exception as exp:
            print(exp)
            pass

    def get(self, redis_key: str = None):
        redis_cache_data = self.client.get(name=redis_key)
        try:
            if redis_cache_data:
                cache_data = redis_cache_data.decode("utf-8")
                cache_data = json.loads(cache_data)
                return cache_data
        except Exception as exp:
            print(exp)
            pass

    def destroy(self, redis_key: str = None):
        return self.client.expire(name=redis_key, time=0)

    def get_ttl_in_seconds(self, redis_key: str = None) -> float:
        ttl_value = self.client.pttl(name=redis_key)
        delta = timedelta(milliseconds=ttl_value)
        seconds = delta.total_seconds()
        return seconds

    def disconnect(self, redis_db):
        print(f"Redis Client Successfully Disconnected from Redis db {redis_db}")
        self.connection.disconnect(inuse_connections=True)

    def remove_key(self, redis_key: str = None):
        self.client.delete(redis_key)
