class MultiQueue:
    def __init__(self, num_counters):
        self.counters = [[] for _ in range(num_counters)]
    
    def add_customer(self, customer):

        min_queue = self.counters[0]
        for queue in self.counters:
            if self.queue_size(min_queue) > self.queue_size(queue):
                min_queue = queue
        min_queue.append(customer)
        print(f"Покупець {customer} доданий до каси {self.index_of(min_queue) + 1}")
    
    def serve_customer(self, counter_index):
        if counter_index < 0 or counter_index >= self.size_counters():
            raise IndexError("Невірний номер каси")
        
        if self.queue_size(self.counters[counter_index]) > 0:
            customer = self.counters[counter_index].pop(0)
            print(f"Покупець {customer} обслугований на касі {counter_index + 1}")
            return customer
        else:
            print(f"Каса {counter_index + 1} порожня")
            return None
    
    def show_queues(self):
        i = 0
        for queue in self.counters:
            print(f"Каса {i + 1}: {queue}")
            i += 1
    
    def size_counters(self):
        count = 0
        for _ in self.counters:
            count += 1
        return count

    def queue_size(self, queue):
        count = 0
        for _ in queue:
            count += 1
        return count

    def index_of(self, queue):
        i = 0
        for j in self.counters:
            if j is queue:
                return i
            i += 1
        raise ValueError("Queue not found in counters")

multi_queue = MultiQueue(3) 

multi_queue.add_customer("Андрій")
multi_queue.add_customer("Олена")
multi_queue.add_customer("Марія")
multi_queue.add_customer("Іван")
multi_queue.add_customer("Світлана")

multi_queue.show_queues()

multi_queue.serve_customer(0) 
multi_queue.serve_customer(1)
multi_queue.serve_customer(2) 

multi_queue.show_queues()