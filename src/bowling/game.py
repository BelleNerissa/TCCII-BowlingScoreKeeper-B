from typing import List

from bowling.frame import Frame


class BowlingGame:
    def __init__(self):
        self.frames = []

    def add_frame(self, frame: Frame):
        """ Add a frame to the game """
        self.frames.append(frame)
        pass

    def set_bonus(self, first_throw: int, second_throw: int):
        """ The the bonus throw """
        self.frames[-1].bonus_throw = (first_throw, second_throw)
        pass

    def is_last_frame(self) -> bool:
        """ Return whether the frame is a last frame of the game """
        return len(self.frames) == 10 
    
    def is_next_frame_bonus(self) -> bool:
        """ Get if the next frame is bonus """
        if len(self.frames) < 10:
            return False
        if len(self.frames) == 10:
            last_frame = self.frames[-1]
            if last_frame.is_strike() or last_frame.is_spare():
                return True
            return False
        else:
            penultimate_frame = self.frames[-2]
            if penultimate_frame.is_strike() or penultimate_frame.is_spare():
                return True
            return False


    def score(self) -> int:
        """ Get the score from the game """
        total_score = 0
        for i, frame in enumerate(self.frames):
            if frame.is_strike():
                if i + 1 < len(self.frames):
                    next_frame = self.frames[i + 1]
                    if next_frame.is_strike() and i + 2 < len(self.frames):
                        total_score += 20 + self.frames[i + 2].first_throw
                    else:
                        total_score += 10 + next_frame.first_throw + next_frame.second_throw
                else:
                    total_score += 10 + frame.bonus_throw[0] + frame.bonus_throw[1]
            elif frame.is_spare():
                if i + 1 < len(self.frames):
                    total_score += 10 + self.frames[i + 1].first_throw
                else:
                    total_score += 10 + frame.bonus_throw[0]
            else:
                total_score += frame.score()

        if all(frame.is_strike() for frame in self.frames):
            return 300
        else:
            return total_score





