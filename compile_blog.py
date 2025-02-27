import sys
import tokenizer
import parser
import semantic_analyzer
import assembler

def main():
    n = len(sys.argv)
    if n == 1:
        print('''Expected 1+ files as command line arguments 
              \n Usage: compile_blog [files]''')
    else:
        for i in range(1, n):
            print(sys.argv[i], end=" ")

if __name__ == "__main__":
    main()
