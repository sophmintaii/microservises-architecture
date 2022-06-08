import hazelcast
import logging
import time

# logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    client = hazelcast.HazelcastClient(cluster_name='dev',
                                       cluster_members=[
                                           '127.0.0.1:5701',
                                           '127.0.0.1:5702',
                                           '127.0.0.1:5703'
                                       ])

    dist_map = client.get_map('distributed-map').blocking()

    key = '1'
    value = '0'
    dist_map.put_if_absent(key, value)

    start_time = time.time()
    for i in range(1000):
        dist_map.lock(key)
        try:
            value = dist_map.get(key)
            time.sleep(0.01)
            value = str(int(value) + 1)
            dist_map.set(key, value)
        finally:
            dist_map.unlock(key)

    print(f'result = {dist_map.get(key)}\ntime taken = {time.time() - start_time}')

    client.shutdown()
