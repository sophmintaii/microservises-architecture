import hazelcast
import logging
import time


# logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    client = hazelcast.HazelcastClient(cluster_name='dev',
                                       cluster_members=[
                                           '127.0.0.1:5701'
                                       ])

    queue = client.get_queue('bounded-queue').blocking()

    value = 0
    while value < 1000:
        if queue.remaining_capacity() == 0:
            print('waiting for free space')
            time.sleep(1)
            continue
        else:
            queue.put(f'{value}_value')
            value += 1
    queue.put('pill')  # to mark the end of the queue

    client.shutdown()
