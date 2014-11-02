use core::task::spawn;
use core::comm::{stream, Port, Chan, SharedChan};

fn spawn_and_print() {
    fn print_message() { println("I am running in a different task!"); }
    spawn(print_message);

    do spawn {
        println("I too am running in a different task!");
    }

    for int::range(0, 20) |child_task_number| {
        do spawn {
            print(fmt!("I am child number %d\n", child_task_number));
        }
    }
}

fn basic_channel() {
    let (port, chan): (Port<int>, Chan<int>) = stream();
    
    do spawn || {
        let result = 1024;
        chan.send(result);
    }

    let result = port.recv();
    println(fmt!("result %d", result));
}

fn main() {
    let (port, chan) = stream();
    let chan = SharedChan(chan);

    for uint::range(0, 4) |init_val| {
        let child_chan = chan.clone();
        do spawn {
            child_chan.send(100 * init_val);
        }
    }
    
    let result = port.recv() + port.recv() + port.recv() + port.recv();
    println(fmt!("result %u", result));
}
