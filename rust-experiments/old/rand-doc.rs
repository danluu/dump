use core::rand::RngUtil; 

fn main() {
    let rng = rand::Rng(); 
    println(fmt!("%f",rng.gen_float())); 
    println(fmt!("%d",rng.gen_int())); 
    println(fmt!("%b",rng.gen_bool())); 
    println(fmt!("%b",rng.gen_weighted_bool(3))); 
    println(rng.gen_str(8)); 
    println(fmt!("%?",rng.gen_bytes(8))); 
    println(fmt!("%d",rng.choose([1,2,4,8,16,32]))); 

    let x = [rand::Weighted {weight: 4, item: 'a'}, 
             rand::Weighted {weight: 2, item: 'b'}, 
             rand::Weighted {weight: 2, item: 'c'}];
    println(fmt!("%c",rng.choose_weighted(x)));

    println(fmt!("%?",rng.choose_weighted_option(x)));
    println(fmt!("%?",rng.weighted_vec(x)));  //~['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c']
    println(fmt!("%?",rng.shuffle([1,2,3])));

    let mut y = [1,2,3];
    rng.shuffle_mut(y);
    println(fmt!("%?",y));
    rng.shuffle_mut(y);
    println(fmt!("%?",y));

}
