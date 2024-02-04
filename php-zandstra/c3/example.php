<?php
declare(strict_types=1);

class ShopProduct
{
    public function __construct(
        public string $title, 
        public string $producerFirstName ,
        public string $producerMainName, 
        public float $price,
        int $numPages = 0,
        float $playLength = 0
        ) {}


    public function getProducer(): string
    {
        return "{$this->producerFirstName}" . " {$this->producerMainName}";
    }

    public function getSummaryLine(): string
    {
        $base = "{$this->title} ({$this->producerMainName}, ";
        $base .= "{$this->producerFirstName})";
        return $base;
    }
    
}

class CdProduct extends ShopProduct {
    public function getPlayLength(): int {
        return $this->playLength;
    }

    public function getSummaryLine(): string {
        $base = "{$this->title} ({$this->producerMainName}, ";
        $base .= "{$this->producerFirstName})";
        $base .= ": playing time - {$this->playLength}";
        return $base;
    }
}

class BookProduct extends ShopProduct {
    public function getNumberOfPages(): int {
        return $this->numPages;
    }

    public function getSummaryLine(): string
    {
        $base = "{$this->title} ({$this->producerMainName}, ";
        $base .= "{$this->producerFirstName})";
        $base .= ": page count - {$this->numPages}";
        return $base;
    }
}

$product2 = new CdProduct(
    "Exile on Coldharbour Lane",
    "The",
    "Alabama 3",
    10.99,
    0,
    60.33
);

class ShopProductWriter {
    public function write(ShopProduct $shopProduct) {
        $str = $shopProduct->title . ": " . $shopProduct->getProducer() . " ({$shopProduct->price})\n";
        print $str;
    }

}


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

class Storage{
    public function add(string $key, string|bool $value) {

    }
}

?> 