from threading import Thread, Condition
import time
import random
condition = Condition()
queue = []
max_num=4

class ProducerThread(Thread):
    def run(self):
        nums = range(5) 
        global queue
        while True:
            condition.acquire()
            if len(queue) == max_num:
                print "Queue full, producer is waiting"
                condition.wait()
                print "Space in queue, Consumer notified the producer"
            num = random.choice(nums)
            queue.append(num)
            print "Produced", num
            condition.notify()
            condition.release()
            time.sleep(random.random())

class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print "Nothing in queue, consumer is waiting"
                condition.wait()
                print "Producer added something to queue and notified the consumer"
            num = queue.pop(0)
            print "Consumed", num
            condition.release()
            time.sleep(random.random())
ProducerThread().start()
ConsumerThread().start()
