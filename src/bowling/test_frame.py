import unittest
from bowling.frame import Frame


class TestFrames(unittest.TestCase):
    pass

    def test_frame_score(self):
        playFrame = Frame(1, 4)
        self.assertEqual(playFrame.score(), 5)  
        
    def test_frame_is_strike(self):
        playFrame = Frame(10, 0)
        self.assertTrue(playFrame.is_strike())

    def test_frame_is_spare(self):
        playFrame = Frame(5, 5)
        self.assertTrue(playFrame.is_spare()) 
        
    def test_frame_bonus(self):
        playFrame = Frame(2, 6)
        self.assertEqual(playFrame.bonus(2), 2)


if __name__ == '__main__':
    unittest.main()
