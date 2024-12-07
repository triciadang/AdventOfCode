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
    let mut lines = lines_from_file(file_name).expect("Could not load lines");

    let (mut current_line,mut current_index) = find_initial_pos(lines.clone());

    let mut direction = String::from("N");
    let mut out_of_bounds = false;


    while out_of_bounds == false{
        if direction == String::from("N"){
            let temp_lines = lines.clone();
            let (new_line,new_index,out_of_bounds_flag,new_lines) = move_north(current_line,current_index,temp_lines);
            current_line = new_line;
            current_index = new_index;
            out_of_bounds = out_of_bounds_flag;
            lines = new_lines;
            direction = String::from("E");
        }
        else if direction == "E"{
            let temp_lines = lines.clone();
            let (new_line,new_index,out_of_bounds_flag,new_lines) = move_east(current_line,current_index,temp_lines);
            current_line = new_line;
            current_index = new_index;
            out_of_bounds = out_of_bounds_flag;
            lines = new_lines;
            direction = String::from("S");
        }
        else if direction == "S"{
            let temp_lines = lines.clone();
            let (new_line,new_index,out_of_bounds_flag,new_lines) = move_south(current_line,current_index,temp_lines);
            current_line = new_line;
            current_index = new_index;
            out_of_bounds = out_of_bounds_flag;
            lines = new_lines;
            direction = String::from("W");
        }
        else if direction == "W"{
            let temp_lines = lines.clone();
            let (new_line,new_index,out_of_bounds_flag,new_lines) = move_west(current_line,current_index,temp_lines);
            current_line = new_line;
            current_index = new_index;
            out_of_bounds = out_of_bounds_flag;
            lines = new_lines;
            direction = String::from("N");
        }
    }
    let temp_lines = lines.clone();
    let mut num_of_symbols = 0;

    for each_line in temp_lines{
        num_of_symbols += each_line.chars().filter(|x| *x=='X').count();
        num_of_symbols += each_line.chars().filter(|x| *x=='^').count();
    }
    println!("Number of Marks: {}",num_of_symbols);

}

fn move_west(
    mut current_line:usize,
    mut current_index:usize,
    lines: Vec<String>) 
-> (usize,usize,bool,Vec<String>) {

    let all_lines_counts = &lines.len();
    let line_length = &lines.get(0).unwrap().len();
    let mut new_line:Vec<String> = lines;
    

    while current_line < *all_lines_counts
    && current_index < *line_length
    {
        if current_index != 0{
            if let Some(result_n) = new_line.get(current_line)
                    .and_then(|line| line.chars().nth(current_index-1)) {

                if result_n == '#' {
                    return (current_line,current_index,false,new_line);
                }
                else{

                    if let Some(line) = new_line.get_mut(current_line) {
                        let mut chars: Vec<char> = line.chars().collect();
                        if current_index < chars.len() {
                            chars[current_index-1] = '^';
                            *line = chars.iter().collect();
                        }
                    }
                    if let Some(line) = new_line.get_mut(current_line) {
                        let mut chars: Vec<char> = line.chars().collect();
                        if current_index < chars.len() {
                            chars[current_index] = 'X';
                            *line = chars.iter().collect();
                        }
                    }
                        current_index -= 1;
                }
            }
        }
        else{
            break;
        }
    }
    return (current_line,current_index,true,new_line);
}

fn move_east(
    mut current_line:usize,
    mut current_index:usize,
    lines: Vec<String>) 
-> (usize,usize,bool,Vec<String>) {

    let all_lines_counts = &lines.len();
    let line_length = &lines.get(0).unwrap().len();
    let mut new_line:Vec<String> = lines;
    

    while current_line < *all_lines_counts
    && current_index < *line_length
    {
        if let Some(result_n) = new_line.get(current_line)
                .and_then(|line| line.chars().nth(current_index+1)) {

            if result_n == '#' {
                return (current_line,current_index,false,new_line);
            }
            else{

                if let Some(line) = new_line.get_mut(current_line) {
                    let mut chars: Vec<char> = line.chars().collect();
                    if current_index < chars.len() {
                        chars[current_index+1] = '^';
                        *line = chars.iter().collect();
                    }
                }
                if let Some(line) = new_line.get_mut(current_line) {
                    let mut chars: Vec<char> = line.chars().collect();
                    if current_index < chars.len() {
                        chars[current_index] = 'X';
                        *line = chars.iter().collect();
                    }
                }
                current_index += 1;            
            }  
        }
        else{
            break;
        }
    }
    return (current_line,current_index,true,new_line);
}


fn move_south(
    mut current_line:usize,
    mut current_index:usize,
    lines: Vec<String>) 
-> (usize,usize,bool,Vec<String>) {

    let all_lines_counts = &lines.len();
    let line_length = &lines.get(0).unwrap().len();
    let mut new_line:Vec<String> = lines;
    

    while current_line < *all_lines_counts
    && current_index < *line_length
    {
        if let Some(result_n) = new_line.get(current_line+1)
                .and_then(|line| line.chars().nth(current_index)) {

            if result_n == '#' {
                return (current_line,current_index,false,new_line);
            }
            else{

                if let Some(line) = new_line.get_mut(current_line+1) {
                    let mut chars: Vec<char> = line.chars().collect();
                    if current_index < chars.len() {
                        chars[current_index] = '^';
                        *line = chars.iter().collect();
                    }
                }
                if let Some(line) = new_line.get_mut(current_line) {
                    let mut chars: Vec<char> = line.chars().collect();
                    if current_index < chars.len() {
                        chars[current_index] = 'X';
                        *line = chars.iter().collect();
                    }
                }
                current_line += 1;        
            }  
        }
        else{
            break;
        }
    }
    return (current_line,current_index,true,new_line);
}

fn move_north(
    mut current_line:usize,
    mut current_index:usize,
    lines: Vec<String>) 
-> (usize,usize,bool,Vec<String>) {

    let all_lines_counts = &lines.len();
    let line_length = &lines.get(0).unwrap().len();
    let mut new_line:Vec<String> = lines;
    

    while current_line < *all_lines_counts
    && current_line >= 0
    && current_index < *line_length
    && current_index >= 0 
    {
        if current_line != 0{
            if let Some(result_n) = new_line.get(current_line - 1)
                    .and_then(|line| line.chars().nth(current_index)) {

                if result_n == '#' {
                    return (current_line,current_index,false,new_line);
                }
                else{

                    if let Some(line) = new_line.get_mut(current_line-1) {
                        let mut chars: Vec<char> = line.chars().collect();
                        if current_index < chars.len() {
                            chars[current_index] = '^';
                            *line = chars.iter().collect();
                        }
                    }
                    if let Some(line) = new_line.get_mut(current_line) {
                        let mut chars: Vec<char> = line.chars().collect();
                        if current_index < chars.len() {
                            chars[current_index] = 'X';
                            *line = chars.iter().collect();
                        }
                    }
                        current_line -= 1;

                }
            }
        }
        else{
            break;
        }
    }
    return (current_line,current_index,true,new_line);
}


fn find_initial_pos(lines:Vec<String>) -> (usize,usize){
    for i in 0..lines.len(){

        if let Some(position) = lines[i].find("^"){
            return (i,position);
        }
        
    }
    return (0,0);
}