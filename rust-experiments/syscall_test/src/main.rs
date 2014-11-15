#![feature(phase)]

#[phase(plugin, link)]
extern crate syscall;

fn write(fd: uint, buf: &[u8]) {
    unsafe {
        syscall!(WRITE, fd, buf.as_ptr(), buf.len());
    }
}

fn main() {
    println!("Hello, world!");
    write(1, "Hello, world via syscall!\n".as_bytes());
}
