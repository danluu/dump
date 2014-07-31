#include <linux/module.h>
#include <linux/kernel.h>

int init_module(void) {
  printk(KERN_INFO "Hello World!\n");

  return 0;
}

void cleanup_module(void) {
  printk(KERN_INFO "Cleaning up!\n");
}
