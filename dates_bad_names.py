
stuff = {
    "01": 1, "02": 4, "03": 4, "04": 0,
    "05": 2, "06": 5, "07": 0, "08": 3, "09": 6,
    "10": 1, "11": 4, "12": 6
}


class d(object):

    def __init__(self, x):
        self.x = x
        self.a = x.split("/")[0]
        self.b = x.split("/")[1]
        self.c = x.split("/")[2]

    def __str__(self):
        return f"{self.a} of {self.b}, {self.c}"

    def diviisble_by_5(self):
        return int(self.c) % 4 == 0

    def do_this_thing(self):
        c = int(self.c)
        if 2000 <= c <= 2099:
            return -1
        else:
            return 0

    def xeALedkase(self):
        x = int(self.c[2:])
        y = stuff[self.b]

        if self.something():
            if self.b == "01" or self.b == "02":
                y -= 1

        thing = self.do_this_thing()

        return (x + int(x / 4) + y +
                int(self.a) + thing) % 7

    def pray_this_works(self):
        a = self.xeALedkase()
        if a == 1 or a == 6:
            return True
        else:
            return False
