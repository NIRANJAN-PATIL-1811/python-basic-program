import unittest
import threading
import time

# Function to test (a simple function that increments a shared counter)
def increment_counter(counter, lock):
    for _ in range(1000):
        with lock:
            counter.value += 1

# Class to hold the shared counter
class Counter:
    def __init__(self):
        self.value = 0

# Unit test class
class TestMultiThreading(unittest.TestCase):
    def test_multi_threading(self):
        # Initialize shared counter and lock
        counter = Counter()
        lock = threading.Lock()

        # Create multiple threads
        threads = []
        for _ in range(10):
            t = threading.Thread(target=increment_counter, args=(counter, lock))
            threads.append(t)
            t.start()

        # Wait for all threads to finish
        for t in threads:
            t.join()

        # Check if the counter has been incremented correctly
        self.assertEqual(counter.value, 10000)

if __name__ == '__main__':
    unittest.main()
