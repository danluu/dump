#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

struct Person {
  char *name;
  int age;
  int height;
  int weight;
};

struct Person *new_person(char *name, int age, int height, int weight) {
  struct Person *nperson = malloc(sizeof(struct Person));
  assert(nperson != NULL);

  nperson->name = strdup(name);
  nperson->age = age;
  nperson->height = height;
  nperson->weight = weight;

  return nperson;
}

void del_person(struct Person *p) {
  assert(p != NULL);

  free(p->name);
  free(p);
}

void print_person(struct Person *p) {
  printf("Name: %s\n", p->name);
  printf("\tAge: %d\n", p->age);
  printf("\tHeight: %d\n", p->height);
  printf("\tWeight: %d\n", p->weight);
}

int main(int argc, char *argv[]) {
  // make two people structures
  struct Person *joe = new_person("Joe Alex", 32, 64, 140);

  struct Person *frank = new_person("Frank Blank", 20, 72, 180);

  // print them out and where they are in memory
  printf("Joe is at memory location %p:\n", joe);
  print_person(joe);

  printf("Frank is at memory location %p:\n", frank);
  print_person(frank);

  // make everyone age 20 years and print them again
  joe->age += 20;
  joe->height -= 2;
  joe->weight += 40;
  print_person(joe);

  frank->age += 20;
  frank->weight += 20;
  print_person(frank);

  // destroy them both so we clean up
  del_person(joe);
  del_person(frank);

  return 0;
}
