import hazelcast
import logging
import time


# logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    client = hazelcast.HazelcastClient(cluster_name='dev',
                                       cluster_members=[
                                           '127.0.0.1:5702',
                                           '127.0.0.1:5703'
                                       ])

    queue = client.get_queue('bounded-queue').blocking()

    while 1:
        value = queue.take()
        print(value)
        time.sleep(0.1)
        if value == 'pill':  # end of the queue?
            queue.put('pill')
            break

    client.shutdown()

