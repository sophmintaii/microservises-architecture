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
    for _ in range(1000):
        while True:
            old_value = dist_map.get(key)
            new_value = int(old_value)
            time.sleep(0.01)
            new_value += 1
            if dist_map.replace_if_same(key, old_value, str(new_value)):
                break

    print(f'result = {dist_map.get(key)}\ntime taken = {time.time() - start_time}')

    client.shutdown()
