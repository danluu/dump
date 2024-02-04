<?php

class ShopProduct
{
    public $title = "default product";
    public $producerMainName = "main name";
    public $producerFirstName = "first name";
    public $price = 0;

    public function getProducer()
    {
        return "{$this->producerFirstName}" . " {$this->producerMainName}";
    }
    
}

$product1 = new ShopProduct();
$product2 = new ShopProduct();

$product1->title = "My Antonia";
$product2->title = "Catch 22";

print "author: {$product1->producerFirstName} " . "{$product1->producerMainName}\n";

print "author: {$product1->getProducer()}\n";

// var_dump($product1);
// var_dump($product2);

?> 