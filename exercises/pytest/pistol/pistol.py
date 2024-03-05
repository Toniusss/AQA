import random


class Pistol:
    def __init__(self):
        self.BULLETS_QTY_MAX = 15
        self.MAGAZINES_QTY_MAX = 2
        self.bullets = self.BULLETS_QTY_MAX
        self.magazines = self.MAGAZINES_QTY_MAX
        self.pistol_is_locked = False

    def shot(self):
        if self.bullets > 0 or self.magazines > 0:
            if self.pistol_is_locked:
                return 'misfire'
            if self.bullets == 0 and self.magazines > 0:
                self.reload()
            if self.bullets > 0:
                if self.misfire():
                    self.pistol_is_locked = True
                self.bullets -= 1
                return True

    def reload(self):
        self.pistol_is_locked = False
        if self.bullets >= 0 and self.magazines > 0:
            self.magazines -= 1
            self.bullets = self.BULLETS_QTY_MAX
            return True
        if self.bullets > 0 and self.magazines == 0:
            return True
        return False

    def amount(self):
        amount_dict = {"magazines": self.magazines, "bullets": self.bullets}
        return amount_dict

    def unlock(self):
        self.pistol_is_locked = False
        return True

    def misfire(self):
        misfire_random = round(random.random(), 1)
        if misfire_random == 0.1:
            return True


