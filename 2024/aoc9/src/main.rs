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

    for i in 0..lines.len(){

        let current_line:String = lines[i].clone();
        let mut checksum:i128 = 0;

        checksum = build_string(current_line);
        println!("{}",checksum);
    }
}

fn build_string(input_line:String) -> i128{
    let line_length = input_line.len();
    let mut current_line = input_line.clone();
    let mut new_string:Vec<String> = Vec::new();
    let mut file_name:i32 = 0;
    let mut checksum:i128 = 0;
    let mut backwards_index:usize = line_length-1;
    let mut frontwards_index:usize = 0;

    //if ends on blank
    if line_length % 2 == 0{
        backwards_index -= 1;
    }


    while frontwards_index <= backwards_index{
        println!("{}",frontwards_index);
        println!("{}",backwards_index);

        let length_of_first_file:usize = current_line.chars().nth(frontwards_index).and_then(|c| c.to_digit(10)).map(|d| d as usize).unwrap();
        //represents non blanks
        if frontwards_index % 2 == 0{
            
            for _i in 0..length_of_first_file{
                new_string.push(file_name.to_string());
            }
            file_name += 1;
        }

        //else represents blanks - start sticking in those at the back
        else{


            for _k in 0..length_of_first_file{
                if frontwards_index <= backwards_index{
                    println!("{}",length_of_first_file);
                    let mut first_back_char:char = current_line.chars().nth(backwards_index.clone()).unwrap();
                    let mut char_vector: Vec<char> = current_line.chars().collect();
        
                    while first_back_char == '0'{
                        backwards_index -= 2;
                        
                        first_back_char = current_line.chars().nth(backwards_index.clone()).unwrap();
                    }

                    println!("back char: {}",first_back_char);
                    println!("back index: {}",backwards_index);

                    let mut backwards_file_name:usize = backwards_index/2;

                    println!("filename: {}",backwards_file_name);

                    new_string.push(backwards_file_name.to_string());

                    if let Some(char_to_dig_back_char) = char::to_digit(first_back_char,10){
                        let mut new_back_char = char_to_dig_back_char -  1;

                        char_vector[backwards_index] = char::from_digit(new_back_char as u32,10).unwrap();
                        let char_vector_clone = char_vector.clone();
                        current_line = char_vector_clone.into_iter().collect::<String>();
                    }
                }

                else {
                    new_string.push(file_name.to_string());
                    file_name+= 1;
                }

            }



        }      

        frontwards_index += 1;
    }

    println!("{:?}",new_string);
    return calculate_checksum(new_string);
}

fn calculate_checksum(filled_in_vec:Vec<String>) -> i128{
    let mut checksum:i128 = 0;
    let mut index:usize = 0;

    for each_value in filled_in_vec{
        let mut result:i128 = each_value.parse().unwrap();
        checksum += index as i128 * result;
        // println!("{}",checksum);

        index += 1;
    }
    
    return checksum;
}
