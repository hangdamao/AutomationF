# author = "hang"
# created 12.10.2019

import redis
from base import log_base

logger = log_base.MyLog("redis_base")


class RedisBase:

    def __init__(self):
        self.__host = 'localhost'   # redis数据库地址
        self.__port = 6379          # redis数据库端口号
        self.__db = 1               # redis数据库名称
        self.__red = self.__redis_ini()

    def __enter__(self):
        return self

    def __redis_ini(self):
        pool = redis.ConnectionPool(host=self.__host,
                                    port=self.__port,
                                    db=self.__db)
        red = redis.Redis(connection_pool=pool)
        # logger.debug("redis数据库初始化成功。")
        logger.info("redis数据库初始化成功。")
        return red

    def redis_set(self, key, value, timeout=500):
        # 设置存储在redis数据库的失效时间
        res = self.__red.set(name=key, value=value, ex=timeout)
        if res is True:
            logger.info(f"向redis数据库存储数据：{key, value}成功。")
            return True
        return False

    def redis_get(self, key):
        # 从redis数据库中读取数据
        res = self.__red.get(name=key)
        if res is not None:
            logger.info(f"从redis数据库读取数据：{key, res}成功。")
            return str(res, encoding="utf-8")
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logger.error("redis数据库初始化失败或操作数据异常！")
        return False  # True表示不会抛出异常信息， False会抛出异常


if __name__ == '__main__':
    with RedisBase() as R:
        res_1 = R.redis_set(key="aaaa", value="11123321")
        res_2 = R.redis_get(key="aaaa")
        logger.info(res_1)
        logger.info(res_2)
        logger.info(type(res_2))
        print(R.redis_get('aaaa'))