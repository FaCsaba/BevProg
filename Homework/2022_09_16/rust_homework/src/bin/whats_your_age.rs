
fn prompt_for_input<F, T: std::str::FromStr>(prompt_msg: &str, validation: F) -> T 
where 
F: FnOnce(&T) -> bool + Copy, <T as std::str::FromStr>::Err: std::fmt::Debug {
    println!("{}", prompt_msg);
    let mut inp = String::new();
    let mut inp_change_type: T;
    loop {
        std::io::stdin()
            .read_line(&mut inp).expect("Couldn't read from std in");
        if inp.trim().parse::<T>().is_ok()  {
            inp_change_type = inp.trim().parse().expect("unreachable");
            if !inp.is_empty() && validation(&inp_change_type) {break}
        }
    }
    inp_change_type
}

fn main() {
    let age: u32 = prompt_for_input("What is your age?", |x| {x > &0});
    if age >= 21 {
        println!("You can legally drink in the USA!")
    }
    if age >= 18 {
        println!("You can legally consume tobacco products in Hungary")
    }
    if age >= 17 {
        println!("You can legally get your drivers license in Hungary")
    }
    if age >= 12 {
        println!("You can legally watch the greatest movie of all time: Shrek 2")
    } else {
        println!("You are a baby. You can't do anything")
    }
}
