from characters import Pig
from polygon import Polygon


class Level():
    def __init__(self, pigs, columns, beams, space):
        self.pigs = pigs
        self.columns = columns
        self.beams = beams
        self.space = space
        self.number = 0
        self.number_of_birds = 4
        # lower limit
        self.one_star = 30000
        self.two_star = 40000
        self.three_star = 60000
        self.bool_space = False

    def open_flat(self, x, y, n):
        """Create a open flat struture"""
        y0 = y
        for i in range(n):
            y = y0+100+i*100
            p = (x, y)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+60, y)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+30, y+50)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def closed_flat(self, x, y, n):
        """Create a closed flat struture"""
        y0 = y
        for i in range(n):
            y = y0+100+i*125
            p = (x+1, y+22)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+60, y+22)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+30, y+70)
            self.beams.append(Polygon(p, 85, 20, self.space))
            p = (x+30, y-30)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def horizontal_pile(self, x, y, n):
        """Create a horizontal pile"""
        y += 70
        for i in range(n):
            p = (x, y+i*20)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def vertical_pile(self, x, y, n):
        """Create a vertical pile"""
        y += 10
        for i in range(n):
            p = (x, y+85+i*85)
            self.columns.append(Polygon(p, 20, 85, self.space))

    def build_0(self):
        """level 0"""
        pig1 = Pig(980, 100, self.space)
        pig2 = Pig(985, 182, self.space)
        self.pigs.append(pig1)
        self.pigs.append(pig2)
        p = (950, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1010, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 150)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (950, 200)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1010, 200)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 240)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8
        self.one_star = 30000
        self.two_star = 40000
        self.three_star = 60000

    def build_1(self):
        """level 1"""
        pig = Pig(1000, 100, self.space)
        self.pigs.append(pig)
        p = (900, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (850, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (850, 150)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1050, 150)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1105, 210)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def build_2(self):
        """level 2"""
        pig1 = Pig(880, 180, self.space)
        self.pigs.append(pig1)
        pig2 = Pig(1000, 230, self.space)
        self.pigs.append(pig2)
        p = (880, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (880, 150)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (1000, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1000, 180)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1000, 210)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def build_3(self):
        """level 3"""
        pig = Pig(950, 320, self.space)
        pig.life = 25
        self.pigs.append(pig)
        pig = Pig(885, 225, self.space)
        pig.life = 25
        self.pigs.append(pig)
        pig = Pig(1005, 225, self.space)
        pig.life = 25
        self.pigs.append(pig)
        p = (1100, 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1070, 152)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (1040, 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (920, 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (950, 152)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (1010, 180)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (860, 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (800, 100)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (830, 152)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (890, 180)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (860, 223)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (920, 223)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 223)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1040, 223)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (890, 280)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (1010, 280)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (950, 300)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (920, 350)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 350)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (950, 400)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def build_4(self):
        """level 4"""
        pig = Pig(900, 300, self.space)
        self.pigs.append(pig)
        pig = Pig(1000, 500, self.space)
        self.pigs.append(pig)
        pig = Pig(1100, 400, self.space)
        self.pigs.append(pig)
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def build_5(self):
        """level 5"""
        pig = Pig(900, 70, self.space)
        self.pigs.append(pig)
        pig = Pig(1000, 152, self.space)
        self.pigs.append(pig)
        for i in range(9):
            p = (800, 70+i*21)
            self.beams.append(Polygon(p, 85, 20, self.space))
        for i in range(4):
            p = (1000, 70+i*21)
            self.beams.append(Polygon(p, 85, 20, self.space))
        p = (970, 176)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1026, 176)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1000, 230)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8



    def load_level(self):
        try:
            build_name = "build_"+str(self.number)
            getattr(self, build_name)()
        except AttributeError:
            self.number = 0
            build_name = "build_"+str(self.number)
            getattr(self, build_name)()
