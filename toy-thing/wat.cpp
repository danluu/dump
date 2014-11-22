#include <assert.h>
#include <stdlib.h>

#include <iostream>
#include <set>
#include <vector>

// This would be a lot simpler and more efficient if cards were represented as a bit mask.
// That would only require 52 of 64 bits, and passing around cards would be trivial.
// Instead, this is OO-ified just to see what this looks like.

// A card is an int from 0 to 51.
// Within a suit, cards are numbered from 0 to 12
// A, 2, 3, 4, ..., Q, K
// Suits are ordered Club, Diamond, Heart, Spades.
// Clubs    0-12
// Diamonds 13-25
// Hearts   26-38
// Spades   39-51

class Player {
public:
  Player(int id) : id_(id), num_sets_(0) {
    
  }

  int has_suit(int suit) {
    int base_card_num = suit * 13;
    int highest_card_num = base_card_num + 12;
    for (int card : hand_) {
      if (card > base_card_num && card < highest_card_num) {
	return true;
      }
    }
    return false;
  }

  void lose_suit(std::vector<int>& matching_cards, int suit) {
    assert(matching_cards.size() == 0);
    int base_card_num = suit * 13;
    int highest_card_num = base_card_num + 12;
    auto it = hand_.begin();
    while (it != hand_.end()) {
      if (*it > base_card_num && *it < highest_card_num) {
	matching_cards.push_back(*it);
	it = hand_.erase(it);
      } else {
	++it;
      }
    }
  }

  void gain_cards(std::vector<int>& new_cards) {
    for (int card : new_cards) {
      hand_.insert(card);
    }
    check_set_completion();
  }

  void gain_card(int card) {
    hand_.insert(card);
    check_set_completion();
  }
  
  void check_set_completion() {
    int total_cards = num_cards() + 4*num_sets_; // Only used for debug/assert.

    for (int i = 0; i < 13; ++i) {
      auto club = hand_.count(i);
      auto diamond = hand_.count(i+13);
      auto heart = hand_.count(i+26);
      auto spade = hand_.count(i+39);

      if (club && diamond && heart && spade) {
	++num_sets_;
	hand_.erase(i);
	hand_.erase(i+13);
	hand_.erase(i+26);
	hand_.erase(i+39);
      }

      // Should never create or destroy cards.
      assert(total_cards == num_cards() + 4*num_sets_);
    }

    if (num_cards() == 0) {
      std::cout << "Player " << id_ << " won\n";
      // TODO: handle winning somehow.
    }
  }

  int num_cards() {
    return hand_.size();
  }

private:
  std::set<int> hand_; // Contains cards in deck. Cards are removed as they're dealt.
  int num_sets_;
  int id_;
};

class Deck {
public:
  Deck(){
    reset_deck();
  };

  void reset_deck() {
    cards_.clear();
    for (int i = 0; i < 51; ++i) {
      cards_.push_back(i);
    }
    this->shuffle();
  }

  void shuffle() {
    // Maintain invariant that cards <= i are randomly shuffled.
    for (int i = 0; i < cards_.size(); ++i) {
      int target = rand() % (i + 1); // not very random, but should be ok.
      int temp = cards_[target];
      cards_[target] = cards_[i];
      cards_[i] = temp;
    }
  }

  int num_cards() {
    return cards_.size();
  }

  int get_card() {
    assert(cards_.size() > 0); // game should have already ended.
    int card = cards_.back();
    cards_.pop_back();
    return card;
  }
  
  ~Deck();

private:
  std::vector<int> cards_; // Contains cards in deck. Cards are removed as they're dealt.
};

class Game {
public: 
  Game(int num_players) : deck_(new Deck()), num_players_(num_players), game_over_(false) {
    assert(num_players <= 10); // 5 cards per player. 10 players = 50 cards.
    for (int i = 0; i < num_players; ++i) {
      players_.push_back(std::unique_ptr<Player>(new Player(i)));
    }
  }

  // Check that deck has 0 cards or any player has 0 cards.
  int game_over() {
    if (deck_->num_cards() == 0) {
      return 1;
    }
    for (int i = 0; i < players_.size(); ++i) {
      if (players_[i]->num_cards() == 0) {
	return 1;
      }
    }
    return 0;
  }

  void play_game() {
    while (!game_over_) {
      for (int current_player = 0; current_player < num_players_; current_player++) {
	int failed_action = false;
	while (!failed_action) {
	  // Take a single action. We get to go again if we don't fail.
	  int target_player, target_suit;
	  std::cout << "Player " << current_player << "target player?\n";
	  std::cin >> target_player;
	  std::cout << "Player " << current_player << "target suit?\n";
	  std::cin >> target_suit;
	  // TODO: check that current player has suit
	  if (target_player < num_players_ && target_suit < 4) {
	    if (players_[target_player]->has_suit(target_suit)) {
	      std::vector<int> cards_to_pass;
	      players_[target_player]->lose_suit(cards_to_pass, target_suit);
	      players_[current_player]->gain_cards(cards_to_pass);

	    } else {
	      failed_action = true;
	      int new_card = deck_->get_card();
	      players_[current_player]->gain_card(new_card);
	    }
	  
	    if (game_over()) {
	      // TODO: end game.
	    }
	}
	}
      }
    }
  }

private:
  std::unique_ptr<Deck> deck_;
  std::vector<std::unique_ptr<Player>> players_;
  int num_players_;
  bool game_over_;
  
};


int main() {

  return 0;
}
