class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    self.storage[0], self.storage[len(self.storage)-1] = self.storage[len(self.storage)-1], self.storage[0]
    top_most_value = self.storage.pop()
    self._sift_down(0)
    return top_most_value

  def get_max(self):
    pass

  def get_size(self):
    return len(self.storage)

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