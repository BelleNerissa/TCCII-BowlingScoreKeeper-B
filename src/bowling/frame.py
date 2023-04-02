class Frame:
    def __init__(self, first_throw: int, second_throw: int) -> None:
        self.first_throw = first_throw
        self.second_throw = second_throw
        self.bonus_throw = None

    def score(self) -> int:
        """ The score of a single frame """
        if self.is_strike():
            return 10
        elif self.is_spare():
            return 10
        else:
            return self.first_throw + self.second_throw

    def is_strike(self) -> bool:
        """ Return whether the frame is a strike or not """
        return self.first_throw | self.second_throw == 10

    def is_spare(self) -> bool:
        """ Return whether the frame is a spare or not """
        return self.first_throw + self.second_throw == 10 and not self.is_strike()

    def bonus(self, pins: int) -> int:
        """ Bonus throw """
        self.bonus_throw = pins
        return self.bonus_throw
       
