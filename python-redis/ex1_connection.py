from redis import Redis
redis_connection = Redis()
print("Connection to Redis server: ", redis_connection.ping())
