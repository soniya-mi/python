class Queus:
    def __init__(self):
        self.queue = []
    def enq(self,value):
        return selff.queue.insert(0,value)

    def deq(self):
        if is_empty = 0 :
            return None
        else:
            return self.queue.pop()
    def is_empty(self):
        return self.size() == 0
    def size(self):
        return len(self.queue)