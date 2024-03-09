import random


class Pistol:
    _MAX_BULLETS = 15
    _MAX_MAGAZINES = 10
    _PERCENTAGE_MISFIRES = 10

    def __init__(self):
        self.bullets = self._MAX_BULLETS
        self.magazines = self._MAX_MAGAZINES
        self.pistol_is_locked = False

    def shot(self):
        if self.pistol_is_locked:
            raise LockedException
        # Ordinary shot
        if 0 < self.bullets <= self._MAX_BULLETS:
            if 0 <= self.magazines <= self._MAX_MAGAZINES:
                # Random misfires
                if random.randint(1, 100) <= self._PERCENTAGE_MISFIRES:
                    self.pistol_is_locked = True
                    raise LockedException
                # Shot
                self.bullets -= 1
            else:
                raise AmmunitionValueError
        elif self.bullets == 0:
            # Automatic reloading with 0 bullets
            if 0 < self.magazines <= self._MAX_MAGAZINES:
                self.reload()
                self.shot()
            # Out of bullets and magazines
            elif self.magazines == 0:
                raise OutOfBullets
            else:
                raise AmmunitionValueError
        else:
            raise AmmunitionValueError

    def reload(self):
        self.pistol_is_locked = False
        # Automatic reload
        if self.magazines > 0:
            self.magazines -= 1
            self.bullets = self._MAX_BULLETS
        else:
            # The last magazine with bullets
            if self.bullets > 0:
                raise OutOfMagazines

    def amount(self):
        return {"magazines": self.magazines, "bullets": self.bullets}


class LockedException(Exception):
    def __str__(self):
        return 'The pistol is locked. Please reload it'


class OutOfMagazines(Exception):
    def __str__(self):
        return 'There are no more magazines'


class OutOfBullets(Exception):
    def __str__(self):
        return 'There are no more bullets'


class AmmunitionValueError(Exception):
    def __str__(self):
        return 'Ammunition value error'
