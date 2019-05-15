class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_node = BinarySearchTree(value)
    while self.value != value:
      if value < self.value:
        if self.left is not None:
          self = self.left
        else:
          self.left = new_node
      elif value > self.value:
        if self.right is not None:
          self = self.right
        else:
          self.right = new_node

  def contains(self, target):
    while self.value != target:
      if target < self.value:
        if self.left is not None:
          self = self.left
        else:
          return False
      elif target > self.value:
        if self.right is not None:
          self = self.right
        else:
          return False
    if target == self.value:
      return True
    
  def get_max(self):
    while self.right is not None:
      self = self.right
    return self.value

  def for_each(self, cb):
    if self is not None:
      BinarySearchTree.for_each(self.left, cb)
      BinarySearchTree.for_each(self.right, cb)
      cb(self.value)