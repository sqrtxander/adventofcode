fn main() {
    let commands = read_input();

    println!("{}", part_1(&commands.as_slice()));
    println!("{}", part_2(&commands.as_slice()));
}

fn part_1(commands: &[String]) -> u32 {

    let mut position = 0;
    let mut depth = 0;

    for line in commands {
        let line = line.split(' ').take(2).collect::<Vec<&str>>();

        let dir = line[0];
        let dist = line[1].parse::<u32>().unwrap();

        match dir {
            "forward" => position += dist,
            "up" => depth -= dist,
            "down" => depth += dist,
            _ => println!("Unknown command")
        }
    }

    return position * depth
}

fn part_2(commands: &[String]) -> u32 {

    let mut position = 0;
    let mut depth = 0;
    let mut aim = 0;

    for line in commands {
        let line = line.split(' ').take(2).collect::<Vec<&str>>();

        let dir = line[0];
        let dist = line[1].parse::<u32>().unwrap();

        match dir {
            "forward" => {
                position += dist;
                depth += aim * dist;    
            },
            "up" => aim -= dist,
            "down" => aim += dist,
            _ => println!("Unknown command")
        }
    }

    return position * depth
}

fn read_input() -> Vec<String> {
    let input = include_str!("../../input.txt")
        .lines()
        .map(|line| line.to_string())
        .collect();

    return input;
}