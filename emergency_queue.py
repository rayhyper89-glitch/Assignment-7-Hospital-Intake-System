# emergency_queue.py

class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

    def __repr__(self):
        return f"{self.name} ({self.urgency})"


class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)
        while index < size:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            print("Error: No patients in queue.")
            return None
        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return root

    def print_heap(self):
        print("Current Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")
