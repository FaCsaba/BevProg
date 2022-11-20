How to run the inter-process communication homework

you will need cargo which you can get by running this:
`curl https://sh.rustup.rs -sSf | sh`

please navigate to this folder and build the rust project by running the following command:

```bash
cargo build --manifest-path=./rust_client/Cargo.toml
```
this build the project now we can run it
I recommend opening two terminals
1st command: `./rust_client/target/debug/rust_client`
2nd command: `python communicate.py`

now we have inter-process communication!!!