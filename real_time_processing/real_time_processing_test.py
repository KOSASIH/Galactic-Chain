import unittest
from real_time_processing import RealTimeProcessor

class TestRealTimeProcessor(unittest.TestCase):
    def test_process_data(self):
        processor = RealTimeProcessor()
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        for d in data:
            processor.process_data(d)
        self.assertEqual(len(processor.buffer), 5)

    def test_average_value(self):
        processor = RealTimeProcessor()
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        for d in data:
            processor.process_data(d)
        self.assertEqual(processor.buffer[0], 3.0)

if __name__ == "__main__":
    unittest.main()
