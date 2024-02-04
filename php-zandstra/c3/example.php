<?php
declare(strict_types=1);

class ShopProduct
{
    public function __construct(
        public string $title, 
        public string $producerFirstName = "",
        public string $producerMainName = "", 
        public float $price = 0.0) {}


    public function getProducer()
    {
        return "{$this->producerFirstName}" . " {$this->producerMainName}";
    }
    
}

class ShopProductWriter {
    public function write(ShopProduct $shopProduct) {
        $str = $shopProduct->title . ": " . $shopProduct->getProducer() . " ({$shopProduct->price})\n";
        print $str;
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

$writer = new ShopProductWriter();
$writer->write($product1);
$writer->write($product2);

class AddressManager {
    private $addresses = ["209.131.36.159", "216.58.213.174"];

    public function outputAddresses(bool $resolve) {
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
$manager->outputAddresses(filter_var($settings->resolvedomains, FILTER_VALIDATE_BOOLEAN));

?> 