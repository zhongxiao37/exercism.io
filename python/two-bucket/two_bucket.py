def measure(bucket_one, bucket_two, goal, start_bucket):
    buckets = []
    cnt = 0
    goal_bucket = None
    other_bucket = None
    buckets.append(Bucket('one', bucket_one))
    buckets.append(Bucket('two', bucket_two))
    if start_bucket == 'two':
        buckets.reverse()
    # fill the starting buckets
    buckets[0]._holding_size = buckets[0].size

    # start to transfer between buckets
    while True:
        goal_bucket = [bucket for bucket in buckets if bucket.holding_size() == goal]
        cnt += 1

        if len(goal_bucket) > 0:
            goal_bucket = goal_bucket[0]
            other_bucket = [bucket for bucket in buckets if bucket.holding_size() != goal][0]
            break
        
        # special case when other bucket's size is the goal
        if buckets[1].size == goal:
            goal_bucket = buckets[1]
            buckets[1]._holding_size = buckets[1].size
            other_bucket = buckets[0]
            cnt += 1
            break
        
        transfer_between_buckets(*buckets)
        
    return (cnt, goal_bucket.name, other_bucket.holding_size())

def transfer_between_buckets(starting_bucket, another_bucket):
    if starting_bucket.is_full() and not another_bucket.is_full():
        min_size = min([starting_bucket.holding_size(), another_bucket.remaining_size()])
        starting_bucket._holding_size -= min_size
        another_bucket._holding_size += min_size
        return None
    
    if starting_bucket.holding_size() > 0 and another_bucket.is_empty():
        min_size = min([starting_bucket.holding_size(), another_bucket.remaining_size()])
        starting_bucket._holding_size -= min_size
        another_bucket._holding_size += min_size
        return None
    
    if another_bucket.is_full():
        another_bucket._holding_size = 0
        return None
    
    if starting_bucket.is_empty():
        starting_bucket._holding_size = starting_bucket.size
        return None



class Bucket():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self._holding_size = 0
    
    def is_empty(self):
        return self._holding_size == 0

    def is_full(self):
        return self._holding_size == self.size
    
    def holding_size(self):
        return self._holding_size

    def remaining_size(self):
        return self.size - self._holding_size