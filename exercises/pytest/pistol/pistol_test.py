from pistol import Pistol


pistol = Pistol()
BULLETS_QTY_MAX_TEST = 15
MAGAZINES_QTY_MAX_TEST = 2

def test_init():
    assert pistol.magazines == MAGAZINES_QTY_MAX_TEST
    assert pistol.BULLETS_QTY_MAX == BULLETS_QTY_MAX_TEST
    assert pistol.bullets == BULLETS_QTY_MAX_TEST
    assert pistol.pistol_is_locked is False

def test_fire_all_bullets():
    for i in range(MAGAZINES_QTY_MAX_TEST + 1):
        for j in range(1, BULLETS_QTY_MAX_TEST + 1):
            if pistol.pistol_is_locked:
                pistol.unlock()
            assert pistol.shot() is True
            assert pistol.bullets == BULLETS_QTY_MAX_TEST - j
        assert pistol.magazines == MAGAZINES_QTY_MAX_TEST - i
    assert pistol.amount()['magazines'] == 0
    assert pistol.amount()['bullets'] == 0

def test_misfire_probability():
    for _ in range(10):
        pistol.magazines = 70
        counter = 0
        shot_repeats = 1000
        for _ in range(shot_repeats):
            if pistol.pistol_is_locked:
                counter += 1
                pistol.unlock()
            pistol.shot()
        assert (shot_repeats / counter - 10) < 3

def test_reload_with_bullets():
    for i in range(1, 6):
        for j in range(1, BULLETS_QTY_MAX_TEST + 1):
            pistol.magazines = i
            pistol.bullets = j
            pistol.reload()
            assert pistol.magazines == i - 1
            assert pistol.bullets == BULLETS_QTY_MAX_TEST

def test_reload_without_bullets():
    for i in range(1, 6):
        pistol.magazines = i
        pistol.bullets = 0
        pistol.reload()
        assert pistol.magazines == i - 1
        assert pistol.bullets == BULLETS_QTY_MAX_TEST

def test_reload_latest_magazine():
    for i in range(1, BULLETS_QTY_MAX_TEST + 1):
        pistol.magazines = 0
        pistol.bullets = i
        pistol.reload()
        assert pistol.magazines == 0
        assert pistol.bullets == i

def test_unlock():
    pistol.pistol_is_locked = True
    pistol.unlock()
    assert pistol.pistol_is_locked is False

def test_amount():
    for i in range(MAGAZINES_QTY_MAX_TEST + 3):
        pistol.magazines = i
        for j in range(1, BULLETS_QTY_MAX_TEST + 1):
            pistol.bullets = j
            result = pistol.amount()
            assert result == {"magazines": i, "bullets": j}
