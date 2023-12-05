use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input)
        .expect("Invalid Input");

    let words: Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse().expect("Failed to parse number"))
        .collect();

    let sum: i32 = words.iter().map(|&x| x.pow(2)).sum();

    println!("{}", sum % 10);
}
