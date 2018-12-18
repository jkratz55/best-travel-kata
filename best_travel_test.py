import unittest
import best_travel as b

class BestTravelTest(unittest.TestCase):

    def test_best_sum(self):

        self.assertEqual(b.choose_best_sum([50, 55, 57, 58, 60], 3, 174), [55,58,60])

