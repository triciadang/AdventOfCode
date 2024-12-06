use std::{
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}

fn main() {
    second_part();

}

fn second_part(){
    let file_name = String::from("input.txt");
    let lines = lines_from_file(file_name).expect("Could not load lines");
    let mut xmas_exist:bool;

    let mut xmas_count = 0;

    for i in 0..(&lines).len(){
        let line_contents = &lines[i];
        let a_indices: Vec<_> = line_contents.match_indices("A").map(|(i,_)|i).collect();

        for each_index in a_indices{
            if check_nw_se(lines.clone(),i,each_index) && check_ne_sw(lines.clone(),i,each_index){
                xmas_count += 1
            }
        }
    }
    println!("Xmas Count: {}",xmas_count);
}

fn check_ne_sw(lines:Vec<String>, x:usize, y:usize) -> bool {
    let line_length = lines.get(0).unwrap().len();
    if x+1 < lines.len() && x > 0 && y+1 < line_length && y > 0 {
        let target = ['M','S'];
        let target2 = ['S','M'];
        let result_ne = lines.get(x-1)
            .and_then(|line| {

                let char_at_y = line.chars().nth(y+1);
                char_at_y
            });

        let result_sw = lines.get(x+1)
            .and_then(|line| {
                let char_at_y = line.chars().nth(y-1);
                char_at_y
            });

            if result_ne == Some(target[0]) && result_sw == Some(target[1]){
                return true;
            }
            else if result_ne == Some(target2[0]) && result_sw == Some(target2[1]){
                return true;
            }
            else{
                return false;
            }
            
    }
    else{
        return false;
    }
}

fn check_nw_se(lines:Vec<String>, x:usize, y:usize) -> bool {
    let line_length = lines.get(0).unwrap().len();
    if x+1 < lines.len() && x > 0 && y+1 < line_length && y > 0 {
        let target = ['M','S'];
        let target2 = ['S','M'];
        let result_nw = lines.get(x-1)
            .and_then(|line| {

                let char_at_y = line.chars().nth(y-1);
                char_at_y
            });

        let result_se = lines.get(x+1)
            .and_then(|line| {
                let char_at_y = line.chars().nth(y+1);
                char_at_y
            });

            if result_nw == Some(target[0]) && result_se == Some(target[1]){
                return true;
            }
            else if result_nw == Some(target2[0]) && result_se == Some(target2[1]){
                return true;
            }
            else{
                return false;
            }
            
    }
    else{
        return false;
    }
}


fn first_part(){
    let file_name = String::from("input.txt");
    let lines = lines_from_file(file_name).expect("Could not load lines");
    let mut xmas_exist:bool;

    let mut xmas_count = 0;
    
    for i in 0..(&lines).len(){
        let line_contents = &lines[i];
        let x_indices: Vec<_> = line_contents.match_indices("X").map(|(i,_)|i).collect();

        for each_index in x_indices{
            //check horizontally
            if check_horizontal(lines.clone(),i,each_index){
                xmas_count+=1;
            }
            if check_backwards(lines.clone(),i,each_index){
                xmas_count+=1;
            }

            if check_down(lines.clone(),i,each_index){
                xmas_count+=1;
            }

            if check_up(lines.clone(),i,each_index){
                xmas_count+=1;
            }

            if check_diagonal_nw(lines.clone(),i,each_index){
                xmas_count+=1;
            }
            
            if check_diagonal_ne(lines.clone(),i,each_index){
                xmas_count+=1;
            }

            if check_diagonal_se(lines.clone(),i,each_index){
                xmas_count+=1;
            }

            if check_diagonal_sw(lines.clone(),i,each_index){
                xmas_count+=1;
            }
        }
    }
    println!("Xmas Count: {}",xmas_count);
}

fn check_horizontal(lines:Vec<String>, x:usize, y:usize) -> bool {
    lines.get(x)
        .and_then(|line| {
            if y+3 < line.len(){
                Some(&line[y+1..=y+3])
            }
            else{
                None
            }
        })
        .map_or(false,|slice| slice == "MAS")
}

fn check_backwards(lines:Vec<String>, x:usize, y:usize) -> bool {
    lines.get(x)
        .and_then(|line| {
            if y >= 3{
                Some(&line[y-3..=y-1])
            }
            else{
                None
            }
        })
        .map_or(false,|slice| slice == "SAM")
}

fn check_down(lines:Vec<String>, x:usize, y:usize) -> bool {
    if x+3 < lines.len(){
        let target = ['M','A','S'];
        for i in 1..4{
            let result = lines.get(x+i)
                .and_then(|line| {
                    let char_at_y = line.chars().nth(y);
                    char_at_y
                });

            if result != Some(target[i-1]){
                return false;
            }
        }
        return true;
    }
    else{
        return false;
    }
}


fn check_up(lines:Vec<String>, x:usize, y:usize) -> bool {
    if x >= 3 {
        let target = ['M','A','S'];
        for i in 1..4{
            let result = lines.get(x-i)
                .and_then(|line| {
                    let char_at_y = line.chars().nth(y);
                    char_at_y
                });

            if result != Some(target[i-1]){
                return false;
            }
        }
        return true;
    }
    else{
        return false;
    }
}

fn check_diagonal_nw(lines:Vec<String>, x:usize, y:usize) -> bool {
    if x >= 3 && y >= 3{
        let target = ['M','A','S'];
        for i in 1..4{
            let result = lines.get(x-i)
                .and_then(|line| {
                    let char_at_y = line.chars().nth(y-i);
                    char_at_y
                });

            if result != Some(target[i-1]){
                return false;
            }
        }
        return true;
    }
    else{
        return false;
    }
}

fn check_diagonal_sw(lines:Vec<String>, x:usize, y:usize) -> bool {
    if x+3 < lines.len() && y >= 3{
        let target = ['M','A','S'];
        for i in 1..4{
            let result = lines.get(x+i)
                .and_then(|line| {
                    let char_at_y = line.chars().nth(y-i);
                    char_at_y
                });

            if result != Some(target[i-1]){
                return false;
            }
        }
        return true;
    }
    else{
        return false;
    }
}

fn check_diagonal_se(lines:Vec<String>, x:usize, y:usize) -> bool {

    let line_length = lines.get(0).unwrap().len();
    if x+3 < lines.len() && y+3 < line_length {
        let target = ['M','A','S'];
        for i in 1..4{
            let result = lines.get(x+i)
                .and_then(|line| {
                    let char_at_y = line.chars().nth(y+i);
                    char_at_y
                });

            if result != Some(target[i-1]){
                return false;
            }
        }
        return true;
    }
    else{
        return false;
    }
}

fn check_diagonal_ne(lines:Vec<String>, x:usize, y:usize) -> bool {

    let line_length = lines.get(0).unwrap().len();

    if x >= 3 && y+3 < line_length {
        let target = ['M','A','S'];
        for i in 1..4{
            let result = lines.get(x-i)
                .and_then(|line| {
                    let char_at_y = line.chars().nth(y+i);
                    char_at_y
                });

            if result != Some(target[i-1]){
                return false;
            }
        }
        return true;
    }
    else{
        return false;
    }
}
