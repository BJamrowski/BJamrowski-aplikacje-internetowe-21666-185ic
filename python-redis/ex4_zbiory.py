from redis import Redis

redis_connection = Redis(decode_responses=True)

# nieposortowane
redis_connection.sadd("key","val1")
redis_connection.sadd("key","val2")
redis_connection.sadd("key","val3")

print(redis_connection.smembers("key"))

# wersja posortowana
redis_connection.zadd("sorted_set_key",{"key1": 5})
redis_connection.zadd("sorted_set_key",{"key2": 2})
redis_connection.zadd("sorted_set_key",{"key3": 6})
redis_connection.zadd("sorted_set_key",{"key4": 10})

print(redis_connection.zrange("sorted_set_key",0, -1))


# wykorzystanie hash
hash_key ='test_hash'

redis_connection.hset(hash_key,'key','value')
