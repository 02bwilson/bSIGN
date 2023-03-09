# bSIGN

bSIGN is a file signing program that can be run in either GUI mode or terminal mode.

## Usage

To run bSIGN in GUI mode, use the following command:

```python bSIGN.py```


To run bSIGN in terminal mode, use the following command:

```python bSIGN.py -f FILE1 FILE2 -a HASH_TYPE```


Replace `FILE1` and `FILE2` with the names of the files you want to sign, and replace `HASH_TYPE` with the hash algorithm you want to use (e.g. `sha256`).

## Requirements

bSIGN requires the following packages:

- cryptography (39.0.2)
- PyQt6 (6.4.2)

## Installation

To install bSIGN, first clone the repository:

```git clone https://github.com/02bwilson/bSIGN.git```

Then, install the required packages:

```pip install -r requirements.txt```


## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
![GitHub](https://img.shields.io/github/license/02bwilson/bSIGN)



