<?php

class ShopProduct
{
    public function __construct(
        public $title, 
        public $producerFirstName = "",
        public $producerMainName = "", 
        public $price = 0.0) {}


    public function getProducer()
    {
        return "{$this->producerFirstName}" . " {$this->producerMainName}";
    }
    
}

$product1 = new ShopProduct("My Antonia", "Willa", "Cather", 5.99);
$product2 = new ShopProduct(
    title: "Shop Catalog",
    price: 0.7
);

$product1->title = "My Antonia";
// $product2->title = "Catch 22";


print "author: {$product1->getProducer()}\n";

// var_dump($product1);
var_dump($product2);

class AddressManager {
    private $addresses = ["209.131.36.159", "216.58.213.174"];

    public function outputAddresses($resolve) {
        foreach ($this->addresses as $address) {
            print $address;
            if ($resolve) {
                print " (" . gethostbyaddr($address) . ")";
            }
            print "\n";
        }
    }
}

$settings = simplexml_load_file("resolve.xml");
$manager = new AddressManager();
// The string false evaluates to true!
$manager->outputAddresses($settings->resolvedomains);

?> 