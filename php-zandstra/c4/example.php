<?php

declare(strict_types=1);


class StaticExample{
    public static $aNum = 0;
    public static function sayHello(){
        self::$aNum++;
        print "hello (".self::$aNum.")\n";
    }
}

print StaticExample::$aNum;
StaticExample::sayHello();
StaticExample::sayHello();

interface Chargeable {
    public function getPrice(): float;
}

class ShopProduct implements Chargeable
{
    public const AVAILABLE = 0;
    public const OUT_OF_STOCK = 1;

    private int $id = 0;
    private int|float $discount = 0;

    public function __construct(
        private string $title,
        private string $producerFirstName,
        private string $producerMainName,
        protected int|float $price
    ) {
    }

    public function setId(int $id): void
    {
        $this->id = $id;
    }

    public function getProducerFirstName(): string
    {
        return $this->producerFirstName;
    }

    public function getProducerMainName(): string
    {
        return $this->producerMainName;
    }

    public function setDiscount(int|float $num): void
    {
        $this->discount = $num;
    }

    public static function getInstance(int $id, \PDO $pdo): ShopProduct|null {
        $stmt = $pdo->prepare("select * from products where id = ?");
        $result = $stmt->execute([$id]);

        $row = $stmt->fetch();
        if (empty($row)) {
            return null;
        }

        if ($row['type'] == "book") {
            $product = new BookProduct(
                $row['title'],
                $row['firstname'],
                $row['mainname'],
                $row['price'],
                $row['numpages']
            );
        } elseif ($row['type'] == "cd") {
            $product = new CdProduct(
                $row['title'],
                $row['firstname'],
                $row['mainname'],
                $row['price'],
                $row['playlength']
            );
        } else {
            $firstname = (is_null($row['firstname'])) ? "" : $row['firstname'];
            $product = new ShopProduct(
                $row['title'],
                $firstname,
                $row['mainname'],
                $row['price']
            );
        }
        $product->setId((int)$row['id']);
        $product->setDiscount($row['discount']);
        return $product;
    }

    public function getDiscount(): int
    {
        return $this->discount;
    }

    public function getTitle(): string
    {
        return $this->title;
    }

    public function getPrice(): float
    {
        return ($this->price - $this->discount);
    }

    public function getProducer(): string
    {
        return $this->producerFirstName . " "
            . $this->producerMainName;
    }

    public function getSummaryLine(): string
    {
        $base  = "{$this->title} ( {$this->producerMainName}, ";
        $base .= "{$this->producerFirstName} )";
        return $base;
    }
}

$dsn = "sqlite:products.sqlite3";
$pdo = new \PDO($dsn, null, null);
$pdo->setAttribute(\PDO::ATTR_ERRMODE, \PDO::ERRMODE_EXCEPTION);
$obj = ShopProduct::getInstance(1, $pdo);
var_dump($pdo, $obj);
print ShopProduct::AVAILABLE;

abstract class ShopProductWriter {
    protected array $products = [];

    public function addProduct(ShopProduct $shopProduct): void {
        $this->products[] = $shopProduct;
    }

    abstract public function write(): void;
}

// class ErroredWriter extends ShopProductWriter {}
class TextProductWriter extends ShopProductWriter {
    public function write(): void {
        $str = "PRODUCTS:\n";
        foreach ($this->products as $shopProduct) {
            $str .= $shopProduct->getSummaryLine() . "\n";
        }
        print $str;
    }
}

abstract class DomainObject {
    private string $group;

    public function __construct()
    {
        $this->group = static::getGroup();
    }

    public static function create(): DomainObject {
        return new static();
    }

    public static function getGroup(): string {
        return "default";
    }
}

class User extends DomainObject {}

class Document extends DomainObject {
    public static function getGroup(): string {
        return "document";
    }
}

class SpreadSheet extends Document {}

print_r(User::create());
print_r(Document::create());
print_r(SpreadSheet::create());



?>