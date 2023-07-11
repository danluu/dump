#include <cstdio>
#include <iostream>

// 3-2. Add a read_from and a write_to function to Listing 3-6.
// These functions should read or write to upper or lower as appropriate.
// Perform bounds checking to prevent buffer overflows.
void write_with_check(char* ptr, size_t idx, size_t max_idx, char val) {
    if (ptr != nullptr && idx <= max_idx) {
        ptr[idx] = val;
    }
}

void three_six() {
    char lower[] = "abc?e";
    char upper[] = "ABC?E";

    size_t lower_max_idx = sizeof(lower) / sizeof(lower[0]) - 2;
    size_t upper_max_idx = sizeof(upper) / sizeof(upper[0]) - 2;

    std::cout << "lower_max_idx: " << lower_max_idx << std::endl;
    std::cout << sizeof(lower) << " " << sizeof(lower[0]) << std::endl;

    char* upper_ptr = upper; // Equivalent: &upper[0]

    lower[3] = 'd'; // lower now contains a b c d e \0 upper_ptr[3] = 'D'; // upper now contains A B C D E \0
    char letter_d = lower[3]; // letter_d equals 'd' char letter_D = upper_ptr[3]; // letter_D equals 'D'

    for (int i = 0; i <= lower_max_idx; ++i) {
        printf("%c\n", lower[i]);
    }
    printf("lower: %s\nupper: %s", lower, upper);    

    upper[3] = 'D';
    for (int i = 0; i < 10; ++i) {
        write_with_check(lower, i, lower_max_idx, 'x');
    }

    for (int i = 0; i <= lower_max_idx; ++i) {
        printf("%c\n", lower[i]);
    }

    printf("lower: %s\nupper: %s\n", lower, upper);
}

// 3-3. Add an Element* previous to Listing 3-9 to make a doubly linked list.
// Add an insert_before method to Element.
// Traverse the list from front to back, then from back to front, using two separate for loops.
// Print the operating_number inside each loop.
struct Element {
    Element* prev{};
    Element* next{};
    void insert_after(Element* new_element) {
        new_element->prev = this;

        new_element->next = this->next;
        this->next = new_element;
        if (new_element->next != nullptr) {
            new_element->next->prev = new_element;
        }
    }
    void insert_before(Element* new_element) {
        new_element->next = this;
        
        new_element->prev = this->prev;
        this->prev = new_element;
        if (new_element->prev != nullptr) {
            new_element->prev->next = new_element;
        }
    }
    char prefix[2];
    short operating_number;
};

void traverse_three_nine() {
    Element t0, t1, t2, t3;
    t1.prefix[0] = 'T';
    t1.prefix[1] = 'K';
    t1.operating_number = 421;
    t1.insert_after(&t2);
    t2.prefix[0] = 'F';
    t2.prefix[1] = 'N';
    t2.operating_number = 2187;
    t2.insert_after(&t3);
    t3.prefix[0] = 'L';
    t3.prefix[1] = 'S';
    t3.operating_number = 5;

    for (Element* ptr = &t1; ptr != nullptr; ptr = ptr->next) {
        std::cout << ptr->operating_number << std::endl;
    }

    for (Element* ptr = &t3; ptr != nullptr; ptr = ptr->prev) {
        std::cout << ptr->operating_number << std::endl;
    }

    t0.operating_number = 20;
    t1.insert_before(&t0);

    for (Element* ptr = &t0; ptr != nullptr; ptr = ptr->next) {
        std::cout << ptr->operating_number << std::endl;
    }

    for (Element* ptr = &t3; ptr != nullptr; ptr = ptr->prev) {
        std::cout << ptr->operating_number << std::endl;
    }
}

int main() {
    three_six();
    traverse_three_nine();

    return 0;
}