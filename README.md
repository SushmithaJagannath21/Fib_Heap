# Fibonacci Heaps in Python

## Project Overview

This project implements Fibonacci Heaps, a data structure that supports a collection of operations that are more efficient than binary heaps, particularly for algorithms involving many decrease-key operations. The project includes two primary classes:

- **FibHeap**: Implements the standard Fibonacci Heap with operations such as insert, delete minimum, find minimum, and decrease priority.
- **FibHeapLazy**: Implements a variant of the Fibonacci Heap with lazy deletion, as described in the original Fibonacci Heap paper. This version modifies the `delete_min` and `find_min` operations to handle vacant nodes.

## Files Included

- **`fib.py`**: Contains the `FibHeap` class implementation.
- **`fib_lazy.py`**: Contains the `FibHeapLazy` class implementation.
- **`project2_tests.py`**: Provides test cases to validate the functionality of both `FibHeap` and `FibHeapLazy` classes.
- **`requirements.txt`**: Specifies the required Python packages for the project (if any).

## Getting Started

### Prerequisites

- Python 3.6 or higher
- A Linux environment (recommended for testing)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/fib-heap-python.git
   cd fib-heap-python
2. Ensure you have Python 3.6 or higher installed.

3. If there are any dependencies, install them using the requirements.txt file:
   ```bash
   pip install -r requirements.txt

### Running the Code

FibHeap: You can test the FibHeap implementation using the provided test file:

```bash
python3 project2_tests.py
```

FibHeapLazy: You can test the FibHeapLazy implementation (specific to lazy deletion) using the same test file, as the FibHeapLazy class is included.

Usage
```bash
'FibHeap Class' (fib.py)
'__init__()': Initializes an empty Fibonacci Heap with no nodes.
'insert(value)': Inserts a new node with the specified value into the Fibonacci Heap.
'delete_min()': Deletes the minimum node from the Fibonacci Heap.
'find_min()': Returns the node with the minimum value.
'decrease_priority(node, new_val)': Decreases the priority of the specified node to a new value.

'FibHeapLazy Class' (fib_lazy.py)
Implements a Fibonacci Heap with lazy deletion.
'delete_min_lazy()': Deletes the minimum node, accounting for vacant nodes.
'find_min_lazy()': Finds the minimum node, accounting for vacant nodes.

