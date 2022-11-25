use std::{env::current_dir, io::{Read, Seek}, thread, time::Duration};

fn main() {
    let path = current_dir().unwrap().join("communication");
    let mut modified = path.metadata().unwrap().modified().unwrap(); // we want to check when the file was last modified

    // we could theoretically use a socket, as that is also just a file but for the sake of it I am using a regular file
    let mut file = std::fs::OpenOptions::new()
        .read(true)
        .open(&path)
        .expect("Creating file failed");
    
    loop { // while true
        let modified_again = path.metadata().unwrap().modified().unwrap();
        if modified != modified_again { // if it was modified recently we read the file contents
            file.seek(std::io::SeekFrom::Start(0)).unwrap();
            
            thread::sleep(Duration::from_millis(10)); // HACK: this is used because for some reason if we don't delay the read, we get back an empty string
            // this could be because we check it instantly as it was updated and the file system isn't ready to do that, but we don't even get any errors, just an empty string
            // if you have an explanation as to why this would happen (my theory is the file system is just too slow, or python not being fast enough) please let me know 
            
            let mut comm = String::new();
            file.read_to_string(&mut comm).unwrap(); // we create a string and store the files content into that string


            println!("{}", comm);
            modified = path.metadata().unwrap().modified().unwrap(); // we set the new modified time here
        }

    }
}
