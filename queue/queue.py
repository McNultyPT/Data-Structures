class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
  
  def dequeue(self):
    if self.len() == 0:
      return
    else:
      front_item = self.storage[0]
      del self.storage[0]
      return front_item

  def len(self):
    return len(self.storage)
