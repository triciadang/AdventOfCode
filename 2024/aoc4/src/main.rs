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
            xmas_exist = check_horizontal(lines.clone(),i,each_index);
            if xmas_exist == false{
                
            }
            else{
                println!("{}",xmas_exist)

            }
        }

    }

}

fn check_horizontal(lines:Vec<String>, x:usize, y:usize) -> bool {
    lines.get(x)
        .and_then(|line| {
            // let chars: Vec<char> = line.chars().collect();
            if y+3 < line.len(){
                Some(&line[y..=y+3])
            }
            else{
                None
            }
        })
        .map_or(false,|slice| slice == "MAS")
}