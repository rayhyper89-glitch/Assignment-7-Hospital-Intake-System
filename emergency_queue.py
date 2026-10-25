
class Patient:
    """Represents a patient and their urgency level."""

    def __init__(self, name, urgency):
        if not isinstance(urgency, int) or isinstance(urgency, bool):
            raise TypeError("Urgency must be an integer from 1 to 10.")

        if not 1 <= urgency <= 10:
            raise ValueError("Urgency must be between 1 and 10.")

        self.name = name
        self.urgency = urgency


class MinHeap:
    """Manages patients in priority order using a min-heap."""

    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        """Move a patient upward until the heap property is restored."""
        while index > 0:
            parent_index = (index - 1) // 2

            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = (
                    self.data[parent_index],
                    self.data[index],
                )
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        """Move a patient downward until the heap property is restored."""
        size = len(self.data)

        while True:
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            smallest = index

            if (
                left_index < size
                and self.data[left_index].urgency
                < self.data[smallest].urgency
            ):
                smallest = left_index

            if (
                right_index < size
                and self.data[right_index].urgency
                < self.data[smallest].urgency
            ):
                smallest = right_index

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (
                self.data[smallest],
                self.data[index],
            )
            index = smallest

    def insert(self, patient):
        """Add a patient and restore the heap property."""
        if not isinstance(patient, Patient):
            raise TypeError("Only Patient objects can be inserted.")

        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        """Print patients in the heap's internal list order."""
        print("Current Queue:")

        if not self.data:
            print("(empty)")
            return

        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        """Return the highest-priority patient without removing them."""
        if not self.data:
            raise IndexError("Cannot peek: the patient queue is empty.")

        return self.data[0]

    def remove_min(self):
        """Remove and return the highest-priority patient."""
        if not self.data:
            raise IndexError("Cannot remove a patient: the queue is empty.")

        if len(self.data) == 1:
            return self.data.pop()

        # Save the root, move the last patient to the root,
        # and restore the min-heap property.
        highest_priority = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)

        return highest_priority


# Test the emergency queue.
if __name__ == "__main__":
    heap = MinHeap()

    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))

    heap.print_heap()

    next_up = heap.peek()
    print("\nNext patient:", next_up.name, next_up.urgency)

    served = heap.remove_min()
    print("\nPatient being served:", served.name)

    heap.print_heap()

    # Test removing patients until the queue is empty.
    while heap.data:
        served = heap.remove_min()
        print("Now serving:", served.name)

    # Test the empty-queue error.
    try:
        heap.peek()
    except IndexError as error:
        print("Error:", error)
