class Para:
    window_name = '我(64)'
class Variable:
    def __init__(self):
        self.pos_fishing = [1741, 712]
        self.pos_exclamation_mark = [1341, 427]
        self.left_offset = 22
        self.top_offset = 24
        self.right_offset = 14
        self.bottom_offset = 1
        self.area_exclamation_mark = lambda : [
            self.pos_exclamation_mark[0] - self.left_offset,
            self.pos_exclamation_mark[1] - self.top_offset,
            self.pos_exclamation_mark[0] + self.right_offset, 
            self.pos_exclamation_mark[1] + self.bottom_offset]
        self.pos_confirm = [1273, 579]

        self.hl = 10
        self.hh = 26
        self.sl = 96
        self.sh = 183
        self.vl = 179
        self.vh = 232
    def pos_x_call(self, val):
        self.pos_exclamation_mark[0] = val
    def pos_y_call(self, val):
        self.pos_exclamation_mark[1] = val
    def left_offset_call(self, val):
        self.left_offset = val
    def top_offset_call(self, val):
        self.top_offset = val
    def right_offset_call(self, val):
        self.right_offset = val
    def bottom_offset_call(self, val):
        self.bottom_offset = val
    def hl_call(self, val):
        self.hl = val
    def hh_call(self, val):
        self.hh = val
    def sl_call(self, val):
        self.sl = val
    def sh_call(self, val):
        self.sh = val
    def vl_call(self, val):
        self.vl = val
    def vh_call(self, val):
        self.vh = val