<?php

class ShopProduct
{
    public function __construct(
        public $title, 
        public $producerFirstName,
        public $producerMainName, 
        public $price) {}


    public function getProducer()
    {
        return "{$this->producerFirstName}" . " {$this->producerMainName}";
    }
    
}

$product1 = new ShopProduct("My Antonia", "Willa", "Cather", 5.99);
// $product2 = new ShopProduct();

$product1->title = "My Antonia";
// $product2->title = "Catch 22";

print "author: {$product1->producerFirstName} " . "{$product1->producerMainName}\n";

print "author: {$product1->getProducer()}\n";

// var_dump($product1);
// var_dump($product2);

?> 