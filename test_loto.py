import pytest
from loto import Barrel, Bag, Card, Player, Game


def test_barrel_str():
    barrel = Barrel(10)
    assert str(barrel) == "Barrel(10)"


def test_barrel_comparison():
    barrel1 = Barrel(10)
    barrel2 = Barrel(10)
    barrel3 = Barrel(11)
    assert barrel1 == barrel2
    assert barrel1 != barrel3


def test_bag_str():
    bag = Bag()
    assert "Bag with" in str(bag)


def test_card_str():
    card = Card()
    assert isinstance(str(card), str)


def test_card_comparison():
    card1 = Card()
    card2 = Card()
    assert card1 != card2  # Маловероятно, что карточки идентичны


def test_player_str():
    player = Player("Test Player")
    assert str(player) == "Player(name=Test Player, is_human=True)"


def test_player_comparison():
    player1 = Player("Player1")
    player2 = Player("Player1")
    assert player1 != player2  # Разные карточки
