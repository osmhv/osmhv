import random
#اسامةـ نبيل عبده المليكي

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['♥', '♦', '♣', '♠']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.captured = []

    def play_card(self, index):
        return self.hand.pop(index)

    def draw_card(self, deck):
        card = deck.draw_card()
        if card:
            self.hand.append(card)

class BasraGame:
    def __init__(self, player1_name, player2_name):
        self.deck = Deck()
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.table = []

    def deal_initial_cards(self):
        for _ in range(4):
            self.player1.draw_card(self.deck)
            self.player2.draw_card(self.deck)
        for _ in range(4):
            self.table.append(self.deck.draw_card())

    def show_state(self):
        print(f"Table: {' '.join(str(card) for card in self.table)}")
        print(f"{self.player1.name}'s hand: {' '.join(str(card) for card in self.player1.hand)}")
        print(f"{self.player2.name}'s hand: {' '.join(str(card) for card in self.player2.hand)}")

    def play_turn(self, player):
        print(f"{player.name}'s turn")
        for i, card in enumerate(player.hand):
            print(f"{i}: {card}")
        choice = int(input(f"{player.name}, choose a card to play: "))
        chosen_card = player.play_card(choice)
        self.handle_play(player, chosen_card)

    def handle_play(self, player, card):
        self.table.append(card)
        matching_cards = [c for c in self.table[:-1] if c.rank == card.rank or c.rank == '10']

        if matching_cards:
            player.captured.extend(matching_cards + [card])
            self.table = []
            print(f"{player.name} captures {', '.join(str(c) for c in matching_cards + [card])}!")
        else:
            print(f"{player.name} places {card} on the table.")

    def play_game(self):
        self.deal_initial_cards()

        while self.player1.hand or self.player2.hand:
            self.show_state()
            self.play_turn(self.player1)
            self.play_turn(self.player2)

            if not self.player1.hand and not self.player2.hand and self.deck.cards:
                for _ in range(4):
                    self.player1.draw_card(self.deck)
                    self.player2.draw_card(self.deck)

        print(f"{self.player1.name} captured: {' '.join(str(card) for card in self.player1.captured)}")
        print(f"{self.player2.name} captured: {' '.join(str(card) for card in self.player2.captured)}")
        self.determine_winner()

    def determine_winner(self):
        p1_score = len(self.player1.captured)
        p2_score = len(self.player2.captured)

        if p1_score > p2_score:
            print(f"{self.player1.name} wins with {p1_score} cards!")
        elif p2_score > p1_score:
            print(f"{self.player2.name} wins with {p2_score} cards!")
        else:
            print("It's a tie!")


game = BasraGame("Player 1", "Player 2")
game.play_game()