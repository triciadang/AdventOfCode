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

        if safe == true {
            num_safe += 1;
        }

        println!("{line}: {safe}");
    

    }

    println!("Number safe: {num_safe}");

    Ok(())

}

fn safe_check(current_line_vec: Vec<&str>, increasing:bool) -> bool{
    let mut safe = true;
    let mut num_unsafe = 0;

    for i in 0..current_line_vec.len()-1 {
        let mut higher_number: i32 = current_line_vec[i+1].parse().unwrap();
        let mut below_number: i32 = current_line_vec[i].parse().unwrap();

        let mut diff = higher_number - below_number;

        if increasing == true{
            if diff < 1 || diff > 3 {
                safe = false;
                num_unsafe += 1;

            }
        }

        //decreasing
        if increasing == false{

            if diff < -3 || diff > -1 {
                safe = false;
                num_unsafe += 1;;
            }
        }

        if num_unsafe > 1{
            break;
        }
        
    }

    if num_unsafe <= 1{
        safe = true;
    }

    return safe;

}