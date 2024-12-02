use std::fs;
use std::io::{BufRead, BufReader, Error};


fn main() {
    first_part();
}


fn first_part() -> Result<(),Error> {
    let f = fs::File::open("input.txt")?;
    let mut reader =  BufReader::new(f);

    let mut num_safe = 0;

    for line in reader.lines() {
        let line = line?;
        let mut current_line = line.split(" ").collect::<Vec<&str>>();

        let mut first_num: i32 = current_line[0].parse().unwrap();
        let mut second_num: i32 = current_line[1].parse().unwrap();

        let mut increasing = false;
        let mut safe = false;

        if second_num > first_num {
            increasing = true;
            safe = safe_check(current_line,increasing)
        }
        else if second_num < first_num {
            safe = safe_check(current_line,increasing)
        }

        //else if equal, safe is already false

        if safe == true{
            num_safe += 1;
        }

    }

    Ok(())

}

fn safe_check(current_line_vec: <Vec<&str>>, increasing:bool){

}