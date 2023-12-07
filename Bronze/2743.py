use std::io;

fn main() {
    let mut raw_string = String::new();

    io::stdin()
        .read_line(&mut raw_string)
        .expect("failed to read");

    println!("{}", raw_string.trim().len());
}
