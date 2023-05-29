let hatPrice = 100;
console.log(`Hat price: ${hatPrice}`);

let bootsPrice = "100";
console.log(`Boots price: ${bootsPrice}`);

if (hatPrice == bootsPrice) {
    console.log("Prices are the same");
} else {
    console.log("Prices are different");
}

let totalPrice = Number(hatPrice) + Number(bootsPrice);
console.log(`Total Price: ${totalPrice}`);