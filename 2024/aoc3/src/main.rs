use regex::Regex;
use std::fs;
use std::fmt;


fn main() {
    let contents = fs::read_to_string("input.txt")
    .expect("Should have been able to read the file");

    let str_contents = contents.as_str();

    // let mut results = mul_on_string(str_contents);

    let mut do_indices: Vec<_> = str_contents.match_indices("do").map(|(i,_)|i).collect();
    let mut dont_indices: Vec<_> = str_contents.match_indices("don't").map(|(i,_)|i).collect();

    for each_dont in dont_indices.iter(){
        do_indices.remove(do_indices.iter().position(|x| *x == *each_dont).expect("not found"));
    }


    println!("{:?}",do_indices);
    println!("{:?}",dont_indices);

    
    

}

fn mul_on_string(str_contents:&str) -> i32 {

    let re = Regex::new(r"mul\(\d+,\d+\)").unwrap();



    let mut results = vec![];

    results = re.find_iter(str_contents).map(|c| c.as_str()).collect();

    let mut total_product = 0;

    for each_phrase in results.iter(){
        let open_parenth_index = each_phrase.find("(").unwrap();
        let comma_index = each_phrase.find(",").unwrap();
        let end_parenth_index = each_phrase.find(")").unwrap();

        let first_number = &each_phrase[open_parenth_index+1..comma_index];
        let second_number = &each_phrase[comma_index+1..end_parenth_index];

        println!("{:?}",first_number);
        println!("{:?}",second_number);

        let first_num_int:i32 = first_number.parse().unwrap();
        let second_num_int:i32 = second_number.parse().unwrap();
        

        total_product += first_num_int * second_num_int;

    }

    println!("Total Product: {}",total_product);

    return total_product;


}
