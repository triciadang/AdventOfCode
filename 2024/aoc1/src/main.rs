use std::fs;

fn main() {
    similarity_score();

}

fn similarity_score(){
    let contents = fs::read_to_string("input.txt")
    .expect("Should have been able to read the file");

let num_lines = contents.lines().count();


println!("{contents}");

let num_collection = contents.split_whitespace().collect::<Vec<&str>>();
let mut split_vectors_left: Vec<i32> = Vec::new();
let mut split_vectors_right: Vec<i32> = Vec::new();

for i in 0..num_collection.len() {
    let mut str_to_num: i32 = num_collection[i].parse().unwrap();
    if i%2 == 0{
        split_vectors_left.push(str_to_num);
    }
    else{
        split_vectors_right.push(str_to_num);
    }

}

split_vectors_left.sort();
split_vectors_right.sort();

let mut total_diff = 0;

for j in 0..split_vectors_left.len() {
    
    let mut num_times_appear = split_vectors_right.iter().filter(|&n| * n == split_vectors_left[j]).count();

    total_diff += split_vectors_left[j] * num_times_appear as i32;

}

println!("Total Difference: {total_diff}");


}


fn difference(){
    let contents = fs::read_to_string("input.txt")
        .expect("Should have been able to read the file");

    let num_lines = contents.lines().count();


    println!("{contents}");

    let num_collection = contents.split_whitespace().collect::<Vec<&str>>();
    let mut split_vectors_left: Vec<i32> = Vec::new();
    let mut split_vectors_right: Vec<i32> = Vec::new();

    for i in 0..num_collection.len() {
        let mut str_to_num: i32 = num_collection[i].parse().unwrap();
        if i%2 == 0{
            split_vectors_left.push(str_to_num);
        }
        else{
            split_vectors_right.push(str_to_num);
        }

    }

    split_vectors_left.sort();
    split_vectors_right.sort();

    let mut total_diff = 0;

    for j in 0..split_vectors_left.len() {
        let mut diff = (split_vectors_left[j] - split_vectors_right[j]).abs();
        total_diff += diff;

    }

    println!("Total Difference: {total_diff}");

}
