import random


class Barrel:
    """Класс, представляющий бочонок с номером."""

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Barrel({self.number})"

    def __eq__(self, other):
        if isinstance(other, Barrel):
            return self.number == other.number
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Bag:
    """Класс, представляющий мешок с бочонками."""

    def __init__(self):
        self.barrels = [Barrel(i) for i in range(1, 91)]
        random.shuffle(self.barrels)

    def draw(self):
        """Извлекает случайный бочонок из мешка."""
        return self.barrels.pop() if self.barrels else None

    def __str__(self):
        return f"Bag with {len(self.barrels)} barrels"

    def __len__(self):
        return len(self.barrels)


class Card:
    """Класс, представляющий карточку игрока."""

    def __init__(self):
        self.rows = [[None] * 9 for _ in range(3)]
        self.marked = set()
        self._fill_card()

    def _fill_card(self):
        """Заполняет карточку случайными числами."""
        numbers = random.sample(range(1, 91), 15)
        for i in range(3):
            row_numbers = sorted(numbers[i * 5 : (i + 1) * 5])
            positions = random.sample(range(9), 5)
            for pos, num in zip(positions, row_numbers):
                self.rows[i][pos] = num

    def mark_number(self, number):
        """Отмечает число на карточке, если оно присутствует."""
        for row in self.rows:
            if number in row:
                self.marked.add(number)
                return True
        return False

    def is_winner(self):
        """Проверяет, закрыты ли все числа на карточке."""
        return all(num in self.marked for row in self.rows for num in row if num is not None)

    def __str__(self):
        return "\n".join(
            " ".join(f"{num:2}" if num else "  " for num in row) for row in self.rows
        )

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rows == other.rows
        return False


class Player:
    """Класс, представляющий игрока."""

    def __init__(self, name, is_human=True):
        self.name = name
        self.card = Card()
        self.is_human = is_human

    def take_turn(self, number):
        """Выполняет ход игрока."""
        if self.is_human:
            should_mark = self.card.mark_number(number)
            if should_mark:
                print(f"{self.name} зачеркнул число {number}.")
            else:
                print(f"{self.name} пропустил ход, числа {number} нет на карточке.")
        else:
            if self.card.mark_number(number):
                print(f"Компьютер {self.name} зачеркнул число {number}.")

    def __str__(self):
        return f"Player(name={self.name}, is_human={self.is_human})"

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.name == other.name and self.card == other.card
        return False


class Game:
    """Класс, управляющий процессом игры."""

    def __init__(self, players):
        self.players = players
        self.bag = Bag()

    def play(self):
        """Запускает игровой процесс."""
        try:
            while True:
                barrel = self.bag.draw()
                if not barrel:
                    print("Бочонки закончились. Игра окончена.")
                    break
                print(f"\nВыпал бочонок с номером: {barrel.number}")
                for player in self.players:
                    print(f"\nКарточка игрока: {player.name}")
                    print(player.card)
                    player.take_turn(barrel.number)
                    if player.card.is_winner():
                        print(f"\n{player.name} победил!")
                        return
        except KeyboardInterrupt:
            print("\nИгра была прервана вручную. До свидания!")
            exit(0)

    def __str__(self):
        return f"Game with {len(self.players)} players and a bag of {len(self.bag)} barrels."


def setup_game():
    """Настраивает игру с выбором количества и типов игроков."""
    print("Добро пожаловать в игру Лото!")
    num_players = int(input("Введите количество игроков (минимум 2): "))
    players = []

    for i in range(1, num_players + 1):
        player_type = input(f"Игрок {i} - человек или компьютер? (h/c): ").strip().lower()
        if player_type == "h":
            name = input(f"Введите имя для игрока {i}: ")
            players.append(Player(name, is_human=True))
        elif player_type == "c":
            name = f"Компьютер {i}"
            players.append(Player(name, is_human=False))
        else:
            print("Неверный ввод, создаем игрока как компьютер.")
            name = f"Компьютер {i}"
            players.append(Player(name, is_human=False))

    return players


# Запуск игры
if __name__ == "__main__":
    players = setup_game()
    game = Game(players)
    game.play()
