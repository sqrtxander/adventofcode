fn main() {
    let crabs = read_input();

    println!("{:?}", crabs);

    println!("{}", part_1(&crabs.as_slice()));
    println!("{}", part_2(&crabs.as_slice()));
}

fn mean(vec: &[i32]) -> f32 {
    let sum: i32 = Iterator::sum(vec.iter());
    return (sum / vec.len() as i32) as f32;
} 


fn sum_fuel_1(pos: i32, crabs: &[i32]) -> i32 {
    let mut count = 0;
    for num in crabs {
        count += (num - pos).abs();
    }
    return count;
}

fn part_1(crabs: &[i32]) -> i32 {
    let mut curr_pos = mean(crabs) as i32;

    let delta = if sum_fuel_1(curr_pos, crabs) > sum_fuel_1(curr_pos - 1, crabs) { -1 } else { 1 };

    let mut prev_pos = curr_pos - delta;
    while sum_fuel_1(curr_pos, crabs) < sum_fuel_1(prev_pos, crabs) {
        prev_pos = curr_pos;
        curr_pos += delta;
        
    };
    
    return sum_fuel_1(prev_pos, crabs) ;
}

fn sum_fuel_2(pos: i32, crabs: &[i32]) -> i32 {
    let mut count = 0;
    for num in crabs {
        let distance = (num - pos).abs();
        count += distance * (distance + 1) / 2;
    }
    return count;
}

fn part_2(crabs: &[i32]) -> i32 {
    let mut curr_pos = mean(crabs) as i32;

    let delta = if sum_fuel_2(curr_pos, crabs) > sum_fuel_2(curr_pos - 1, crabs) { -1 } else { 1 };

    let mut prev_pos = curr_pos - delta;
    while sum_fuel_2(curr_pos, crabs) < sum_fuel_2(prev_pos, crabs) {
        prev_pos = curr_pos;
        curr_pos += delta;
        
    };
    
    return sum_fuel_2(prev_pos, crabs) ;
}

fn read_input() -> Vec<i32> {
    let input = include_str!("../../input.txt")
        .split(",")
        .map(|line| line.parse().unwrap())
        .collect::<Vec<i32>>();

    return input;
}
