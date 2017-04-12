class Card:

    
    def __init__(self, card_num, card_suit, card_rank):
        """
        Initializes class variables
        :param card_num - An int between 0 and 51, indicating which card in the deck
            it is. For this project, first 13 will represent Ace of Spades to King of
            spades, next 13 is Ace of Hearts to King of Hearts, and so forth
        :param card_suit - Represents the suit of the card, either Heart, Spade,
            Clover, and Diamond
        :param card_rank - The rank of the card, Ace, Jack, Queen, or King
        """
        self.card_num = card_num
        self.card_suit = card_suit
        self.card_rank = card_rank


    def get_suit():
        """
        :return String representing the suit of the card, Ace, Jack, Queen, or King
        """
        return
