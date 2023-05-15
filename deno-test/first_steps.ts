const res = await fetch("https://deno.land");
const body = await res.text();
console.log(body);