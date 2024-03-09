import pytest
from pistol import Pistol, LockedException, OutOfMagazines, OutOfBullets, AmmunitionValueError
from unittest import mock


# The first number in a tuples - the quantity of bullets, the second number - the quantity of magazines
setup_positive = [(1, 0), (15, 0), (1, 1), (15, 1), (1, 10), (15, 10)]
setup_zero = [(0, 0)]
setup_negative = [(-1, -1), (-1, 0), (0, -1), (15, 11), (16, 10), (16, 11)]
setup_full = list(setup_positive + setup_zero + setup_negative)


@pytest.fixture(params=setup_positive)
def shot_setup_positive(request):
    pistol = Pistol()
    pistol.bullets = request.param[0]
    pistol.magazines = request.param[1]
    return pistol


def test_shot_setup_positive(shot_setup_positive):
    pistol = shot_setup_positive
    with mock.patch('random.randint') as randint:
        randint.return_value = 11
        initial_quantity_of_bullets = pistol.bullets
        initial_quantity_of_magazines = pistol.magazines
        pistol.shot()
        assert pistol.bullets == initial_quantity_of_bullets - 1
        assert pistol.magazines == initial_quantity_of_magazines


@pytest.fixture(params=setup_zero)
def shot_setup_zero(request):
    pistol = Pistol()
    pistol.bullets = request.param[0]
    pistol.magazines = request.param[1]
    return pistol


def test_shot_setup_zero(shot_setup_zero):
    pistol = shot_setup_zero
    with pytest.raises(OutOfBullets) as e:
        initial_quantity_of_bullets = pistol.bullets
        initial_quantity_of_magazines = pistol.magazines
        pistol.shot()
        assert str(e) == 'There are no more bullets'
        assert pistol.bullets == initial_quantity_of_bullets
        assert pistol.magazines == initial_quantity_of_magazines


@pytest.fixture(params=setup_negative)
def shot_setup_negative(request):
    pistol = Pistol()
    pistol.bullets = request.param[0]
    pistol.magazines = request.param[1]
    return pistol


def test_shot_setup_negative(shot_setup_negative):
    pistol = shot_setup_negative
    with pytest.raises(AmmunitionValueError) as e:
        initial_quantity_of_bullets = pistol.bullets
        initial_quantity_of_magazines = pistol.magazines
        pistol.shot()
        assert str(e) == 'Ammunition value error'
        assert pistol.bullets == initial_quantity_of_bullets
        assert pistol.magazines == initial_quantity_of_magazines


@pytest.fixture
def pistol_is_locked():
    pistol = Pistol()
    pistol.pistol_is_locked = True
    return pistol


@pytest.fixture(params=setup_full)
def shot_from_locked_pistol_setup_full(request, pistol_is_locked):
    pistol_is_locked.bullets = request.param[0]
    pistol_is_locked.magazines = request.param[1]
    return pistol_is_locked


def test_shot_from_locked_pistol(shot_from_locked_pistol_setup_full):
    pistol = shot_from_locked_pistol_setup_full
    with pytest.raises(LockedException) as e:
        initial_quantity_of_bullets = pistol.bullets
        initial_quantity_of_magazines = pistol.magazines
        pistol.shot()
        assert str(e) == 'The pistol is locked. Please reload it'
        assert pistol.bullets == initial_quantity_of_bullets
        assert pistol.magazines == initial_quantity_of_magazines


@pytest.fixture(params=[1, 10])
def automatic_reload(request):
    pistol = Pistol()
    pistol.bullets = 0
    pistol.magazines = request.param
    return pistol


def test_shot_with_automatic_reload(automatic_reload):
    pistol = automatic_reload
    with mock.patch('random.randint') as randint:
        randint.return_value = 11
        initial_quantity_of_magazines = pistol.magazines
        pistol.shot()
        assert pistol.bullets == pistol._MAX_BULLETS - 1
        assert pistol.magazines == initial_quantity_of_magazines - 1

