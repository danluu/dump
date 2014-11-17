let (start,end) = channel();
static mut pipeline : Vec<(Sender<uint>,Receiver<uint>)> = [(start,end)];

fn make_new_pipeline(end:Receiver<uint>, prime:uint) -> Receiver<uint> {
    let (filter_start, filter_end) = channel();

    spawn(proc() {
        loop {
            let candidate_prime = end.recv();
            if (candidate_prime % prime != 0) {
                filter_start.send(candidate_prime); 
            }
        }
    });
    filter_end
}

fn get_next_prime(start:Sender<uint>, end:Receiver<uint>) -> (Sender<uint>,Receiver<uint>) {
    let next_prime = end.recv();
    let new_end = make_new_pipeline(end, next_prime);
 
    return (start,new_end);
}

fn main() {
    start.send(2u);
    get_next_prime(start,end);
}
