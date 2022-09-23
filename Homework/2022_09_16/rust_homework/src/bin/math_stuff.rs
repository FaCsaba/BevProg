fn masodfoku(a: f64, b: f64, c: f64) -> (f64, f64) {
    return (
        -b + (b.powi(2) - 4.0 * a * c).sqrt(),
        -b - (b.powi(2) - 4.0 * a * c).sqrt(),
    );
}

struct WeightAve {
    weight: i64,
    value: i64,
}

fn weighted_average(l: &Vec<WeightAve>) -> f64 {
    let weighted_value = l.iter().fold(0, |acc: i64, x| acc + x.weight * x.value);
    let weight_sum = l.iter().fold(0, |acc, x| acc + x.weight);

    return weighted_value as f64 / weight_sum as f64;
}

fn standard_deviation(l: &Vec<i32>) -> f64 {
    let average = l.iter().fold(0, |acc, x| acc + x) as f64 / l.len() as f64;
    let mut s = 0.0;
    for x in l {
        s += ((*x as f64 - average) as f64).powi(2)
    }
    (s / l.len() as f64).sqrt()
}

fn main() {
    println!("{:?}", masodfoku(2.0, 10.0, 3.0));
    println!(
        "{}",
        weighted_average(&vec![
            WeightAve {
                weight: 25,
                value: 75
            },
            WeightAve {
                weight: 30,
                value: 60
            }
        ])
    );
    println!(
        "{}",
        standard_deviation(&vec![
            9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4
        ])
    )
}
