use regex::Regex;
use std::fs;
use std::fmt;

fn main() {
    let contents = fs::read_to_string("input.txt")
    .expect("Should have been able to read the file");

    let str_contents = contents.as_str().trim();

    let mut results = mul_on_string(str_contents);
    println!("Result: {}",results);

    let mut do_indices: Vec<_> = str_contents.match_indices("do()").map(|(i,_)|i).collect();
    let mut dont_indices: Vec<_> = str_contents.match_indices("don't()").map(|(i,_)|i).collect();

    let mut first_index = 0;
    let mut new_total = 0;

    for each_dont in dont_indices.iter(){

        if each_dont > &first_index{

            let new_string = &str_contents[first_index..*each_dont];

            new_total += mul_on_string(new_string);
            println!("New Product: {}",new_total);

            for each_do in do_indices.iter(){
                if each_do > each_dont {
                    first_index = *each_do;
                    break;
                }
            }
        }

    }

    let last_index_dont = dont_indices.len() - 1;
    let mut last_index_do = do_indices.len() - 1;

    for each_do in do_indices.iter(){
        if *each_do > dont_indices[last_index_dont]{
            let new_string = &str_contents[*each_do..];
            new_total += mul_on_string(new_string);
            break;
        }

    }




    println!("New Product: {}",new_total);

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

        let first_num_int:i32 = first_number.parse().unwrap();
        let second_num_int:i32 = second_number.parse().unwrap();
        

        total_product += first_num_int * second_num_int;

    }

    return total_product;


}
