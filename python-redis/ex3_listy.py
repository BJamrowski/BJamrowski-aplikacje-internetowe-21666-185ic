from redis import Redis

redis_connection = Redis(decode_responses=True)

# list_key ="example-list"                      v 1.0
# redis_connection.rpush(list_key,1,2,3,4,5)
# print(redis_connection.lrange(list_key,0, -1))



# kod ponizej bedzie dzialal caly czas
# pobiera on element z listy
# w przypadku braku elementow blokuje program
# w przypadku dodania elementu do listy poinformuje nas on o tym

# whileTrue:    v 2.0
#     print(redis_connection.brpop(list_key))


redis_connection.set("key","value")

redis_connection_1 = Redis(decode_responses=True, db=1)

print(redis_connection_1.get("key"))

print(redis_connection.get("key"))
