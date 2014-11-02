fn f(i: int) {
    fn g(i: int) {
        println(fmt!("g %d",i));
        f(i);
    }
    println("f");
    g(i+1);
}

fn main() {
    f(0);
}
