import argparse
from pathlib import Path

def tokenizer():

def main():
    parser = argparse.ArgumentParser(
        prog='Tokenizer',
        description='Converts blog language into series of tokens',
        usage='%(prog)s [filenames]')
    
    args = parser.parse_args()

    target_dir = Path(args.path)
    

if __name__ == "__main__":
    main()