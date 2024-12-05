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
    let mut xmas_exist:bool;
    
    for i in 0..(&lines).len(){
        let line_contents = &lines[i];
        let x_indices: Vec<_> = line_contents.match_indices("X").map(|(i,_)|i).collect();
        println!("{:?}",x_indices);

        for each_index in x_indices{
            xmas_exist = check_horizontal(lines,i,each_index);
            if xmas_exist == false{
                
            }
        }

    }

}

fn check_horizontal(lines:Vec<String>, x:usize, y:usize) -> bool {

    if let Some(line) = lines.get(x){
        if let Some(character) = line.chars().nth(y) {
            if character == 'M'{
                println!("here");
            }
        }
        else{
            return false;
        }
    }

    return true;
}
