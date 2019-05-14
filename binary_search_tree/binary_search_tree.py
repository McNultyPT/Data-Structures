class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    current = self
    new_node = BinarySearchTree(value)
    while current.value != value:
      if value < current.value:
        if current.left is not None:
          current = current.left
        else:
          current.left = new_node
      elif value > current.value:
        if current.right is not None:
          current = current.right
        else:
          current.right = new_node


  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass