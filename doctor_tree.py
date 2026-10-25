
class DoctorNode:
    """Represents a doctor and their left and right reports."""

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    """Manages the doctor hierarchy using a binary tree."""

    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side, current_node=None):
        side = side.lower().strip()

        if side not in ("left", "right"):
            print("Error: Side must be 'left' or 'right'.")
            return False

        if self.root is None:
            print("Error: The tree is empty. Add a root doctor first.")
            return False

        # Begin searching at the root.
        if current_node is None:
            current_node = self.root

        # Insert when the correct parent is found.
        if current_node.name == parent_name:
            if side == "left":
                if current_node.left is not None:
                    print(f"Error: The LEFT side of {parent_name} is occupied.")
                    return False
                current_node.left = DoctorNode(doctor_name)
            else:
                if current_node.right is not None:
                    print(f"Error: The RIGHT side of {parent_name} is occupied.")
                    return False
                current_node.right = DoctorNode(doctor_name)

            return True

        # Search the left subtree.
        if current_node.left is not None:
            if self.insert(
                parent_name, doctor_name, side, current_node.left
            ):
                return True

        # Search the right subtree.
        if current_node.right is not None:
            if self.insert(
                parent_name, doctor_name, side, current_node.right
            ):
                return True

        # Only the initial call reports a missing parent.
        if current_node == self.root:
            print(f"Error: Parent doctor '{parent_name}' was not found.")

        return False

    def preorder(self, node):
        """Visit root, left subtree, then right subtree."""
        if node is None:
            return []

        return (
            [node.name]
            + self.preorder(node.left)
            + self.preorder(node.right)
        )

    def inorder(self, node):
        """Visit left subtree, root, then right subtree."""
        if node is None:
            return []

        return (
            self.inorder(node.left)
            + [node.name]
            + self.inorder(node.right)
        )

    def postorder(self, node):
        """Visit left subtree, right subtree, then root."""
        if node is None:
            return []

        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.name]
        )


# Test the doctor tree.
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))

    # Test invalid inputs.
    tree.insert("Dr. Nobody", "Dr. Smith", "left")
    tree.insert("Dr. Croft", "Dr. Smith", "middle")
    tree.insert("Dr. Croft", "Dr. Smith", "left")

    # Test an empty tree.
    empty_tree = DoctorTree()
    print("Empty preorder:", empty_tree.preorder(empty_tree.root))


