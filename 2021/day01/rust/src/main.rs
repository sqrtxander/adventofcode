fn main() {
    let depths = read_input();

    println!("{}", count_inc(1, &depths.as_slice()));
    println!("{}", count_inc(3, &depths.as_slice()));
}

fn count_inc(slice_size: usize, depths: &[u16]) -> i32 {
    let mut count = 0;

    for i in slice_size..depths.len() {
        if depths[i] > depths[i-slice_size] {
            count += 1;
        }
    }
    return count
}


fn read_input() -> Vec<u16> {
    let input = include_str!("../../input.txt")
        .lines()
        .map(|line| line.parse().unwrap())
        .collect::<Vec<u16>>();
    
    return input;
}