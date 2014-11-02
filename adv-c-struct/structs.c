// Example from pp. 389

typedef struct foo_faster {
  struct foo_faster *next;
  int data;
} foo_faster;

typedef struct foo {
  int data;
  struct foo *next;
} foo;

int main() {

  
}
