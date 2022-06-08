import hazelcast
import logging


logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    client = hazelcast.HazelcastClient(cluster_name='dev',
                                       cluster_members=[
                                           '127.0.0.1:5701',
                                           '127.0.0.1:5702',
                                           '127.0.0.1:5703'
                                       ])
    dist_map = client.get_map('distributed-map').blocking()

    for idx in range(1000):
        dist_map.set(idx, f'{idx}_value')

    client.shutdown()
