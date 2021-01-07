from redis import Redis

# redis_connection = Redis()                      v 1.0
redis_connection = Redis(decode_responses=True) # v 2.0

# key ="some-key"
# value ="some-val"

key ="some-key"
value =55

redis_connection.set(key, value)
print(redis_connection.get(key))

# redis_connection.append(key,"-append")          # v 3.0
# print(redis_connection.get(key))

# redis_connection.delete(key)                    # v 3.1
# print(redis_connection.get(key))

print(redis_connection.incr(key,5))

print(redis_connection.decr(key,20))
