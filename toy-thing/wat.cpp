#include <vector>
#include <stdlib.h>
#include <assert.h>

enum Suits {Club, Diamond, Heart, Spades};

class Player {};

// A card is an int from 0 to 51.
// Within a suit, cards are numbered from 0 to 12
// A, 2, 3, 4, ..., Q, K
// Suits are ordered Club, Diamond, Heart, Spades.
// Clubs    0-12
// Diamonds 13-25
// Hearts   26-38
// Spades   39-51

class Deck {
public:
  Deck(){
    for (int i = 0; i < 51; ++i) {
      _cards.push_back(i);
    }
    this->shuffle();
  };

  void shuffle() {
    // Maintain invariant that cards <= i are randomly shuffled.
    for (int i = 0; i < _cards.size(); ++i) {
      int target = rand() % (i + 1); // not very random, but should be ok.
      int temp = _cards[target];
      _cards[target] = _cards[i];
      _cards[i] = temp;
    }
  }

  int get_card() {
    assert(_cards.size() > 0);
    int card = _cards.back();
    _cards.pop_back();
    return card;
  }
  
  ~Deck();

private:
  std::vector<int> _cards; // Contains cards in deck. Cards are removed as they're dealt.
};

class Game {
public: 
  Game(int num_players) {
    assert(num_players < 10);
    
    
  }
private:
  std::unique_ptr<Deck> _deck;
  
};


int main() {

  return 0;
}
