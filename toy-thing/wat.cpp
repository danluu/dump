enum suits = {Club, Diamond, Heart, Spades};

class Player {};
class Game {};
class Card {};

class Deck {
public:
  Deck(){
    for (int i = 0; i < 13; ++i) {
      for (int j = 0; j < 4; ++j) {
	Card* new_card = Card(i,j);
	_cards[j*13 + i] = new_card;
      }
    }
    this.shuffle();
  };

  void shuffle() {}
  Card* get_card() {}
  void deal(int num_cards, Player& target_player) {}
  
  ~Deck();

protected:
  Card _cards[52];
};

int main() {

  return 0;
}
