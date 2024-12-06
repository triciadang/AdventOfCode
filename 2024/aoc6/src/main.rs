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



    

}

fn find_initial_pos(lines) -> i32{
    let line_length = lines.get(0).unwrap.len();
    for i in 0..lines.iter(){
        for j in 0..lin
    }

    return (-1,-1);
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