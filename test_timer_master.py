import unittest

from timer import time_it

from unittest.mock import patch

class TestTimer(unittest.TestCase):

    @patch('timer.time')
    def test_recommendation(self, time):
        times = [101, 125]
        time.time = lambda: times.pop(0)
        self.assertEqual(time_it(), 'this was great')
                
        
if __name__ == '__main__':
    unittest.main()