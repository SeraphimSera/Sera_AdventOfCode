use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn day1() -> io::Result<i32> {
    let file = File::open("day1_data.txt")?;
    let reader = BufReader::new(file);
    let mut total = 0;

    for line in reader.lines() {
        for s in line.unwrap().split(' ') {
            println!("{}", s);
        }
    }

    /*
    TODO: 
    - split string in each line (with map, maybe?)
    - convert each split entry into numbers 
    - turn it into two separate lists (somehow)
    - sort then iterate through both at once
    - subtract between both numbers and get abs value
    - add all abs values together
    */

    Ok(1)
}

fn main() {
    let _ = day1();
}