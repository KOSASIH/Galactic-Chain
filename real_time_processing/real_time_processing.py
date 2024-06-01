import time
from collections import deque

class RealTimeProcessor:
    def __init__(self, buffer_size=1000):
        self.buffer = deque(maxlen=buffer_size)

    def process_data(self, data):
        # Process the data in real-time
        # For example, calculate the average value of the data
        self.buffer.append(data)
        if len(self.buffer) == self.buffer.maxlen:
            average = sum(self.buffer) / len(self.buffer)
            print(f"Average value: {average}")
            self.buffer.clear()

if __name__ == "__main__":
    processor = RealTimeProcessor()
    while True:
        data = input("Enter data: ")
        processor.process_data(float(data))
        time.sleep(0.1)  # Simulate real-time processing
