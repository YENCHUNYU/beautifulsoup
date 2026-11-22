# Milestone 4: Iterable BeautifulSoup

## Overview

This milestone makes BeautifulSoup objects iterable, allowing users to traverse all nodes in an HTML document using a standard Python `for` loop.

The iteration follows document order and includes HTML tags, text nodes, comments, and other node types such as doctypes.

## Implementation

The `__iter__()` method was implemented in the `BeautifulSoup` class:

```python
def __iter__(self) -> Iterator[PageElement]:
    """Iterate over all nodes in the document in tree order."""
    return self.descendants
```

Instead of implementing a separate tree traversal algorithm, this method reuses BeautifulSoup's existing `descendants` iterator.

The iterator visits nodes in depth-first document order, including nested elements and text nodes.

## Lazy Iteration

The implementation uses lazy iteration, meaning nodes are produced one at a time as they are requested.

It does not collect all nodes into a list before iteration. This avoids allocating an additional list containing every node and allows iteration to stop early without visiting the entire tree.

Each call to `iter(soup)` creates a new iterator, so the same BeautifulSoup object can be traversed multiple times.

## Usage Example

```python
from bs4 import BeautifulSoup

html = "<div>Hello<p>World</p></div>"
soup = BeautifulSoup(html, "html.parser")

for node in soup:
    print(node)
```

The loop visits the `div` element, its text node, the nested `p` element, and its text node.

## Unit Tests

Five unit tests were added to verify the implementation:

1. **Tree Order:** Verifies that all nodes are visited in depth-first document order.
2. **Text and Comments:** Verifies that text nodes and HTML comments are included.
3. **Doctype:** Verifies that document type declarations are included.
4. **Empty Soup:** Verifies that iterating over an empty document produces no nodes.
5. **Iterator Behavior:** Verifies that the iterator follows Python's iterator protocol, raises `StopIteration` when exhausted, and supports repeated traversal of the same soup object.

## Design Decisions

The implementation reuses the existing `descendants` iterator to avoid duplicating tree traversal logic.

This approach keeps the implementation simple, supports lazy iteration, and preserves the regular BeautifulSoup constructor and object interface.