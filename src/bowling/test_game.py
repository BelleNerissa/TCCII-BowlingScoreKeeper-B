import unittest
from bowling.frame import Frame
from bowling.game import BowlingGame


class TestGames(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def test_add_frame(self):
        frame = Frame(4, 2)
        self.game.add_frame(frame)
        self.assertEqual(len(self.game.frames), 1)

    def test_score_all_zeros(self):
        for i in range(10):
            frame = Frame(0, 0)
            self.game.add_frame(frame)
        self.assertEqual(self.game.score(), 0)

    def test_score_all_strikes(self):
        for i in range(10):
            frame = Frame(10, 0)
            self.game.add_frame(frame)
        self.game.set_bonus(10, 10)
        self.assertEqual(self.game.score(), 300)

    # def test_set_bonus(self):
    #     self.game.set_bonus(5, 2)
    #     self.assertEqual(self.game.bonus_throw, (5, 2))

    def test_is_next_frame_bonus(self):
        self.assertFalse(self.game.is_next_frame_bonus())
        self.game.add_frame(Frame(1, 2))
        self.game.add_frame(Frame(2, 0))
        self.game.add_frame(Frame(5, 3))
        self.game.add_frame(Frame(10, 0))
        self.game.add_frame(Frame(6, 0))
        self.game.add_frame(Frame(10, 3))
        self.game.add_frame(Frame(10, 0))
        self.game.add_frame(Frame(10, 0))
        self.game.add_frame(Frame(10, 0))
        self.game.add_frame(Frame(10, 0))
        self.game.add_frame(Frame(10, 0))
        self.assertTrue(self.game.is_next_frame_bonus())


    def test_is_last_frame(self):
        for i in range(10):
            self.assertFalse(self.game.is_last_frame())
            self.game.add_frame(Frame(1, 2))
        self.assertTrue(self.game.is_last_frame())

if __name__ == '__main__':
    unittest.main()
