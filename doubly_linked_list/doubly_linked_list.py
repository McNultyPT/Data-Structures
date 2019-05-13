"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    new_node = ListNode(value)
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
    self.length += 1

  def remove_from_head(self):
    head = self.head
    if not self.head and not self.tail:
      return None
    elif self.head == self.tail:
      self.head = None
      self.tail = None
      self.length -= 1
    else:
      self.head.delete()
      self.head = head.next
      self.length -= 1
    return head.value
      
  def add_to_tail(self, value):
    new_node = ListNode(value)
    if not self.tail and not self.head:
      self.tail = new_node
      self.head = new_node
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    self.length += 1

  def remove_from_tail(self):
    tail = self.tail
    if not self.tail and not self.head:
      return None
    elif self.tail == self.head:
      self.tail = None
      self.head = None
      self.length -= 1
    else:
      self.tail.delete()
      self.tail = tail.prev
      self.length -= 1
    return tail.value

  def move_to_front(self, node):
    if node == self.tail:
      self.tail = node.prev
    else:
      node.delete()
    node.next = self.head
    self.head.prev = node
    self.head = node

  def move_to_end(self, node):
    if node == self.head:
      self.head = node.next
    else:
      node.delete()
    node.prev = self.tail
    self.tail.next = node
    self.tail = node

  def delete(self, node):
    node.delete()
    if self.head == self.tail:
      self.tail = None
      self.head = None
    elif self.tail == node:
      self.tail = node.prev
    elif self.head == node:
      self.head = node.next
    self.length -= 1
    
  def get_max(self):
    pass
