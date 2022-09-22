fn prompt_for_input<T>(prompt_msg: &str) -> T
where T: std::str::FromStr {
    println!("{}", prompt_msg);
    let mut inp = String::new();
    loop {
        std::io::stdin()
            .read_line(&mut inp).expect("Couldn't read from std in");
        match inp.trim().parse::<T>() {
            Ok(inp_change_type) => {
                if !inp.is_empty() {return inp_change_type}
            }
            Err(_) => {
                println!("Invalid input");
                inp = String::new();
            }
        }
    }
}

fn main() {
    let na: u32 = prompt_for_input("How many Na-s do you have?");
    let cl2: u32 = prompt_for_input("How many Cl\u{2082}-s do you have?");

    let mut nacl = 0;
    let mut excess_na = 0;
    let mut excess_cl = 0;

    if na == cl2*2 { nacl = na}
    if na > cl2*2 {
        nacl = cl2*2;
        excess_na = na - cl2*2
    }
    if cl2*2 > na {
        nacl = na;
        excess_cl = cl2*2 - na
    }

    println!("You can make {nacl} NaCl, isn't that exciting");
    if excess_na > 0 {
        println!("But you have {excess_na} excess Na")
    }
    if excess_cl > 0 {
        println!("But you have {excess_cl} excess Cl")
    }
}