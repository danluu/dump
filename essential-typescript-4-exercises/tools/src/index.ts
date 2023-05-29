import { sum } from "./calc";

function printMessage(msg: string): void {
    console.log(`Message: ${msg}`);

}

printMessage("Hello, TypeScript");

debugger;

const total = sum(100, 200, 300);
console.log(`Total: ${total}`);