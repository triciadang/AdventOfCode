use std::fs;
use std::io::{BufRead, BufReader, Error};


fn main() {
    solution();
}


fn solution() -> Result<(),Error> {
    let f = fs::File::open("input.txt")?;
    let mut reader =  BufReader::new(f);

    let mut num_safe = 0;

    for line in reader.lines() {
        let line = line?;
        let mut current_line = line.split(" ").collect::<Vec<&str>>();
        let (mut safe,mut unsafe_index) = safe_check(current_line.clone());


        if safe == false{
            let mut new_current_line = current_line.clone();
            new_current_line.drain(unsafe_index..unsafe_index+1);
            let (mut safe1, mut unsafe_index1) = safe_check(new_current_line.clone());
            safe = safe1;

            if safe1 == false{
                let mut new_current_line = current_line.clone();
                new_current_line.drain(unsafe_index+1..unsafe_index+2);
                let (mut safe2,mut unsafe_index2) = safe_check(new_current_line.clone());
                safe = safe2;

                if safe2 == false{
                    if unsafe_index != 0{
                        let mut new_current_line = current_line.clone();
                        new_current_line.drain(unsafe_index-1..unsafe_index);
                        let (mut safe3,mut unsafe_index3) = safe_check(new_current_line.clone());
                        safe = safe3;
                    }

                }

            }
            
            
            
        }

        if safe == true {
            num_safe += 1;
        }
    
    }

    println!("Number safe: {num_safe}");

    Ok(())

}


fn check_increasing_or_decreasing(current_line_vec: Vec<&str>) -> String {
    let mut first_num: i32 = current_line_vec[0].parse().unwrap();
    let mut second_num: i32 = current_line_vec[1].parse().unwrap();

    let mut increasing = false;

    if second_num > first_num {
        increasing = true;
        return String::from("increasing");
    }
    else if second_num < first_num {
        return String::from("decreasing");
    }
    else{
        return String::from("same");
    }

}

fn safe_check(current_line_vec: Vec<&str>) -> (bool,usize){

    let mut safe = true;
    let mut num_unsafe = 0;

    let mut pattern:String = check_increasing_or_decreasing(current_line_vec.clone());

    let mut index:usize = 0;

    for i in 0..current_line_vec.len()-1 {
        index = i;
        let mut next_number: i32 = current_line_vec[i+1].parse().unwrap();
        let mut below_number: i32 = current_line_vec[i].parse().unwrap();

        let mut diff = next_number - below_number;

        if pattern == "increasing"{
            if diff < 1 || diff > 3 {
                safe = false;
                break;
            }
        }

        //decreasing
        if pattern == "decreasing"{

            if diff < -3 || diff > -1 {
                safe = false;
                break;
            }
        }

        if pattern == "same"{
            safe = false;
            break;
        }

    }
    

    return (safe,index);

}