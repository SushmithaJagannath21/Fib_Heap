# explanations for member functions are provided in requirements.py
from __future__ import annotations

class FibNode:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNode):
        return self.val == other.val

class FibHeapLazy:
    def __init__(self):
        # you may define any additional member variables you need
        self.roots = []
        self.min_node = None
        self.min_index = None
        self.nodes = 0

    def get_roots(self) -> list:
        return self.roots

    def insert(self, value: int) -> FibNode:
        new_node = FibNode(value)
        self.roots.append(new_node)
        self.nodes += 1
        if self.min_node is None or value < self.min_node.get_value_in_node():
            self.min_node = new_node
            self.min_index = len(self.roots) - 1
        return new_node

    def find_best_root(self) -> FibNode:
        min_value = float("inf")
        best_root = None
        for index, root in enumerate(self.roots):
            if root.get_value_in_node() < min_value:
                min_value = root.get_value_in_node()
                best_root = root
                self.min_index = index
        return best_root

    def delete_root_by_index(self, index: int) -> None:
        self.roots[index], self.roots[-1] = self.roots[-1], self.roots[index]
        self.nodes -= 1
        self.roots.pop()

    def delete_min_lazy(self) -> None:
        if self.min_node is None:
            return  # No minimum node to delete

        if self.min_node.get_value_in_node() is None:  # Check if minimum node is vacant
            # Deleting vacant nodes and their vacant children
            vacant_nodes = [self.min_node]
            while vacant_nodes:
                current_node = vacant_nodes.pop()
                for child in current_node.get_children():
                    if child.get_value_in_node() is None:
                        vacant_nodes.append(child)
                self.roots.remove(current_node)
                self.nodes -= 1

            # Rebuilding heap structure to maintain Fibonacci heap property
            self.restructure_forest()

        else:
            # Minimum node is not vacant, proceed with normal delete operation
            # Merging children of deleted note to list of roots
            if self.min_node.get_children():
                for child in self.min_node.get_children():
                    if child.get_value_in_node() is not None:
                        child.parent = None
                        child.flag = False
                        self.roots.append(child)

            # Removing deleted node from list of roots
            self.delete_root_by_index(self.min_index)
            self.min_node, self.min_index = None, float('inf')

            # Improving Forest Structure and finding the new best root
            self.restructure_forest()

    def restructure_forest(self) -> None:
        roots_copy = self.roots.copy()
        degree = [None] * (self.nodes + 1)

        while roots_copy:
            current_node = roots_copy.pop()
            num_children = len(current_node.get_children())
            if degree[num_children] is None:
                degree[num_children] = current_node
            else:
                temp = degree[num_children]
                degree[num_children] = None
                if current_node.val >= temp.val:
                    temp.children.append(current_node)
                    current_node.parent = temp
                    roots_copy.append(temp)
                else:
                    current_node.children.append(temp)
                    temp.parent = current_node
                    roots_copy.append(current_node)
        
        self.roots = [root for root in degree if root is not None]

        # Finding the new best root
        self.min_node = self.find_best_root()

    def find_min_lazy(self) -> FibNode:
        if self.min_node is None:
            return None
        elif self.min_node.get_value_in_node() is None:  # If minimum node is vacant
            min_value = float("inf")
            min_node = None
            for root in self.roots:
                if root.get_value_in_node() is not None and root.get_value_in_node() < min_value:
                    min_value = root.get_value_in_node()
                    min_node = root
            return min_node
        else:
            return self.min_node

    def make_root(self, node: FibNode) -> None:
        node.parent = None
        node.flag = False
        self.roots.append(node)

    def promote(self, node: FibNode) -> None:
        if node.parent is not None:
            parent_node = node.parent
            parent_node.children.remove(node)
            self.make_root(node)
            self.min_node = self.find_best_root()
            if parent_node.parent is not None:
                if parent_node.flag:
                    self.promote(parent_node)
                else:
                    parent_node.flag = True

    def decrease_priority(self, node: FibNode, new_value: int) -> None:
        node.val = new_value
        if node.parent is None:
            if new_value < self.min_node.get_value_in_node():
                self.min_node = node
                for index, root in enumerate(self.roots):
                    if root == node:
                        self.min_index = index
        else:
            self.promote(node)



    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define