use std::{
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}

fn main() {
    let file_name = String::from("input.txt");
    let lines = lines_from_file(file_name).expect("Could not load lines");

    first_part(lines);
    second_part(lines);

}

fn second_part(lines:Vec<String>){
    let mut instructions: Vec<String> = Vec::new();
    let mut updates: Vec<String> = Vec::new();


    if let Some(blank_index) = lines.iter().position(|x| x==""){
        let (first,second) = lines.split_at(blank_index);

        let first:Vec<String> = first.to_vec();
        let second:Vec<String> = second[1..].to_vec();

        instructions = first;
        updates = second;

    }

    for every_instruction in instructions.iter(){
        
        for i in 0..updates.len(){
            
            if updates[i] != "0"{
                let numbers:Vec<&str> = every_instruction.split("|").collect();

                let first_num_index = &updates[i].find(numbers[0]);
                let second_num_index = &updates[i].find(numbers[1]);

                if let (Some(first_num_index),Some(second_num_index)) =(first_num_index,second_num_index){

                    if second_num_index < first_num_index{

                        updates[i] = String::from("0"); //need to hange
                    }
                }
            }
        }
    }



}

fn first_part(lines:Vec<String>){
    let mut instructions: Vec<String> = Vec::new();
    let mut updates: Vec<String> = Vec::new();


    if let Some(blank_index) = lines.iter().position(|x| x==""){
        let (first,second) = lines.split_at(blank_index);

        let first:Vec<String> = first.to_vec();
        let second:Vec<String> = second[1..].to_vec();

        instructions = first;
        updates = second;

    }

    for every_instruction in instructions.iter(){
        
        for i in 0..updates.len(){
            
            if updates[i] != "0"{
                let numbers:Vec<&str> = every_instruction.split("|").collect();

                let first_num_index = &updates[i].find(numbers[0]);
                let second_num_index = &updates[i].find(numbers[1]);

                if let (Some(first_num_index),Some(second_num_index)) =(first_num_index,second_num_index){

                    if second_num_index < first_num_index{

                        updates[i] = String::from("0");
                    }
                }
            }
        }
    }

    let mut mids_total = 0;
    for every_entry in updates.iter(){
        let vec_entry:Vec<String> = every_entry.split(",")
                                                .map(|s| s.to_string())
                                                .collect();

        mids_total += calculate_mid_num(vec_entry);
        
    }
    println!("{}",mids_total);
}

fn calculate_mid_num(line_entry:Vec<String>) -> i32 {
    let line_length = &line_entry.len();
    let mid_point = line_length/2;

    let str_num = &line_entry[mid_point];
    
    return str_num.parse().unwrap();

}