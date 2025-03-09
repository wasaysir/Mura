# MURA
Wasay's custom BLOGGING LANGUAGE

The goal is to create a more powerful markup language that leverages the barebones simplicity of something like markdown but with the potential flexibility to include more powerful web-features. A langauge that is truly a web-forward language. 

Some inspirations are Rust (functional programming is my fav)
Typst! (I LOOOOOVE TYPST'S MODULARITY, I wanted a Typst for the web)
Flex (Fast Lexical Analyser Generator) BIG FAN OF THE SIMPLICITY OF THE LEXER, I basically copied it verbatim. 

Process:
1. Program compiles tokenizer to generate lexer
2. Lexer is called on blog and breaks it into tokens
3. Parser generates a parse-tree
4. Assembler converts parse tree into React code

Inspo:
https://automerge.org/docs/quickstart/
