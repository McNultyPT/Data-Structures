class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass
    # return len(self.storage)

  def _bubble_up(self, index):
    if index == 0:
      return
    parent = (index - 1) // 2
    if self.storage[index] > self.storage[parent]:
      self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
    return self._bubble_up(parent)

  def _sift_down(self, index):
    left = index * 2 + 1
    right = index * 2 + 2
    length = len(self.storage) - 1
    if left <= length and self.storage[left] > self.storage[index]:
      largest = left
    else:
      largest = index
    if right <= length and self.storage[right] > self.storage[largest]:
      largest = right
    if largest != index:
      self.storage[largest], self.storage[index] = self.storage[index], self.storage[largest]
      self._sift_down(largest)