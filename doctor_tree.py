# doctor_tree.py

class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name, side):
        """
        Inserts a new DoctorNode as the left or right report of the specified parent node.
        """
        if self.root is None:
            print("Error: Cannot insert without a root node.")
            return

        # Helper recursive search
        parent_node = self._find_node(self.root, parent_name)
        if not parent_node:
            print(f"Error: Parent node '{parent_name}' not found.")
            return

        if side not in ["left", "right"]:
            print("Error: Side must be either 'left' or 'right'.")
            return

        new_node = DoctorNode(child_name)

        if side == "left":
            if parent_node.left is None:
                parent_node.left = new_node
            else:
                print(f"Warning: Overwriting existing left child of {parent_name}.")
                parent_node.left = new_node
        else:
            if parent_node.right is None:
                parent_node.right = new_node
            else:
                print(f"Warning: Overwriting existing right child of {parent_name}.")
                parent_node.right = new_node

    def _find_node(self, node, name):
        """Recursive search for a node by name."""
        if node is None:
            return None
        if node.name == name:
            return node
        return self._find_node(node.left, name) or self._find_node(node.right, name)

    # --- Traversals ---
    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]
