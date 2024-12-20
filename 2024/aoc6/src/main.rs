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

    // part1(lines);

    let copied_lines = lines.clone();
    let line_length = copied_lines.get(0).unwrap().len();

    let mut check_loops_count = 0;

    for i in 0..lines.len(){
        println!("i: {}", i);
        for j in 0..line_length{
            let temp_lines = lines.clone();
            if check_loops(i,j,temp_lines){
                println!("i: {}, j: {}", i, j);
                check_loops_count+=1;
            }
        }
    }

    println!("Loop Count: {}",check_loops_count);

}

struct VectorDir(usize,usize,String);

fn check_loops(i:usize,j:usize,other_lines: Vec<String>)->bool{
    let mut lines = other_lines;
    let (mut current_line,mut current_index) = find_initial_pos(lines.clone());
    let mut all_movements:Vec<VectorDir>;

    let mut direction = String::from("N");
    let mut out_of_bounds = false;
    
    // change lines
    if let Some(line) = lines.get_mut(i) {
        let mut chars: Vec<char> = line.chars().collect();
        chars[j] = '#';
        *line = chars.iter().collect();
    }

    let mut hit_same_vector_dir = false;

    while out_of_bounds == false && hit_same_vector_dir == false{
        
        let temp_lines = lines.clone();
        let mut temp_dir = direction.clone();
        let mut hit_loop:bool = false;
        let (new_line,new_index,out_of_bounds_flag,new_lines,hit_loop) = 
                            move_us2(current_line,current_index,temp_lines,temp_dir);

        if hit_loop == true{
            return true;
        }

        current_line = new_line;
        current_index = new_index;
        out_of_bounds = out_of_bounds_flag;
        lines = new_lines;

        if direction == "N"{
            direction = String::from("E");
        }
        else if direction == "E"{
            direction = String::from("S");
        }
        else if direction == "S"{
            
            direction = String::from("W");
        }
        else if direction == "W"{
            direction = String::from("N");
        }

    }

    return false;
}

fn move_us2(
    mut current_line:usize,
    mut current_index:usize,
    lines: Vec<String>,
    mut direction:String)
-> (usize,usize,bool,Vec<String>,bool) {

    let all_lines_counts = &lines.len();
    let line_length = &lines.get(0).unwrap().len();
    let mut new_line:Vec<String> = lines;
    

    while current_line < *all_lines_counts
    && current_index < *line_length
    {
        if current_index != 0 && current_line != 0 {
            let mut temp_current_index = current_index;
            let mut temp_current_line = current_line;
            let mut temp_direction = direction.clone();

            if temp_direction == "W"{
                temp_current_index = current_index - 1;
            }
            if temp_direction == "S"{
                temp_current_line = current_line + 1;
            }
            if temp_direction == "E"{
                temp_current_index = current_index + 1;
            }
            if temp_direction == "N"{
                temp_current_line = current_line - 1;
            }

            if let Some(result_n) = new_line.get(temp_current_line)
                    .and_then(|line| line.chars().nth(temp_current_index.clone())) {

                if result_n == '#' {
                    return (current_line,current_index,false,new_line,false);
                }
                else if result_n != direction.chars().next().expect("string is empty"){

                    if let Some(line) = new_line.get_mut(temp_current_line) {
                        let mut chars: Vec<char> = line.chars().collect();
                        if current_index < chars.len() {
                            chars[temp_current_index] = '^';
                            *line = chars.iter().collect();
                        }
                    }
                    if let Some(line) = new_line.get_mut(current_line) {
                        let mut chars: Vec<char> = line.chars().collect();
                        if current_index < chars.len() {
                            chars[current_index] = direction.chars().next().expect("string is empty");
                            *line = chars.iter().collect();
                        }
                    }
                    if direction == "W"{
                        current_index -= 1;
                    }
                    if direction == "S"{
                        current_line += 1;

                    }
                    if direction == "E"{
                        current_index += 1;
                    }
                    if direction == "N"{
                        current_line -= 1;
                    }

                }
                else{
                    return (current_line,current_index,true,new_line,true); 
                }
            }
            else{
                break;
            }
        }
        else{
            break;
        }
    }
    return (current_line,current_index,true,new_line,false);
}

fn part1(other_lines: Vec<String>){
    let mut lines = other_lines;
    let (mut current_line,mut current_index) = find_initial_pos(lines.clone());
    

    let mut direction = String::from("N");
    let mut out_of_bounds = false;

    while out_of_bounds == false{
        
        let temp_lines = lines.clone();
        let mut temp_dir = &direction;
        let (new_line,new_index,out_of_bounds_flag,new_lines) = move_us(current_line,current_index,temp_lines,temp_dir);
        current_line = new_line;
        current_index = new_index;
        out_of_bounds = out_of_bounds_flag;
        lines = new_lines;

        if direction == "N"{
            direction = String::from("E");
        }
        else if direction == "E"{
            direction = String::from("S");
        }
        else if direction == "S"{
            
            direction = String::from("W");
        }
        else if direction == "W"{
            direction = String::from("N");
        }

        for each in lines.iter(){
        println!("{:?}",each);
        }
        println!("{}",out_of_bounds);
    }

    let temp_lines = lines.clone();
    let mut num_of_symbols = 0;

    for each_line in temp_lines{
        num_of_symbols += each_line.chars().filter(|x| *x=='X').count();
        num_of_symbols += each_line.chars().filter(|x| *x=='^').count();
    }
    println!("Number of Marks: {}",num_of_symbols);
    return
}


fn move_us(
    mut current_line:usize,
    mut current_index:usize,
    lines: Vec<String>,
    mut direction:&String)
-> (usize,usize,bool,Vec<String>) {

    let all_lines_counts = &lines.len();
    let line_length = &lines.get(0).unwrap().len();
    let mut new_line:Vec<String> = lines;
    

    while current_line < *all_lines_counts
    && current_index < *line_length
    {
        if current_index != 0 && current_line != 0 {
            let mut temp_current_index = current_index;
            let mut temp_current_line = current_line;



            if direction == "W"{
                temp_current_index = current_index - 1;
            }
            if direction == "S"{
                temp_current_line = current_line + 1;
            }
            if direction == "E"{
                temp_current_index = current_index + 1;
            }
            if direction == "N"{
                temp_current_line = current_line - 1;
            }

            // println!("{}",temp_current_line);

            if let Some(result_n) = new_line.get(temp_current_line)
                    .and_then(|line| line.chars().nth(temp_current_index.clone())) {

                if result_n == '#' {
                    return (current_line,current_index,false,new_line);
                }
                else{

                    if let Some(line) = new_line.get_mut(temp_current_line) {
                        let mut chars: Vec<char> = line.chars().collect();
                        if current_index < chars.len() {
                            chars[temp_current_index] = '^';
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
                    if direction == "W"{
                        current_index -= 1;
                    }
                    if direction == "S"{
                        current_line += 1;

                    }
                    if direction == "E"{
                        current_index += 1;
                    }
                    if direction == "N"{
                        current_line -= 1;
                    }
                }
            }
            else{
                break;
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