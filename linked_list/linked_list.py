"""A simple implmentation of a linked list."""

from __future__ import annotations
from typing import Any, Iterator


class Node:

  def __init__(self, value: Any, next: Node | None = None) -> None:
    """"Constructor of Node.

    Parameters
    -----------
    value : Any
      The value to be stored in the Node
    next : Node | None, optional
      The next node in the LinkedList
    """
    self.value = value
    self.next = next


class LinkedList:
  """A singly linked list."""

  def __init__(self, value: Any = None) -> None:
    """Link contructor."""
    if value is None:
      self.head: Node | None = None
      self.size = 0
    else:
      self.head = Node(value)
      self.size = 1

  def prepend(self, value: any) -> None:
    """Insert at the front in O(1) time, even if list is empty"""
    new_node = Node(value, next=None)
    new_node.next = self.head
    self.head = new_node
    self.size += 1

  def __iter__(self) -> Iterator[Any]:
    """Yield values from head to tail."""
    current = self.head
    while current:
      yield current.value
      current = current.next

  def __len__(self) -> int:
    """Return the number of nodes in a list."""
    return self.size
