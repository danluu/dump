extern mod std;
use std::base64::ToBase64;
use std::base64::FromBase64;

fn main () {
    let str = [52,32].to_base64();
    println(fmt!("base64: %s", str));
    let bytes = str.from_base64();
    println(fmt!("decoded: %?",bytes));
}
