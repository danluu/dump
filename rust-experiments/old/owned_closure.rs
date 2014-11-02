fn main() {

    let x = 50;
    let a: ~fn() = || { println(fmt!("%?",x)) };
    fn f() {
        100;
    }
//    println(fmt!("%?",a()));
    spawn(a);
//    spawn(f);
}
