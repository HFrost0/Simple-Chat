# Simple-Chat
Chat with OpenAI ChatGPT in your command line, just for simple and ez.

* support markdown show, thanks for [rich](https://github.com/Textualize/rich)

## setup
```shell
pip install git+https://github.com/HFrost0/Simple-Chat.git

# or install from PyPI
pip install schat
```

Before you start, pls set your environment variable
```shell
export OPENAI_API_KEY=xxxxxxxxxxxxxxx
```
You can obtain your openai api key by [url](http://platform.openai.com)

## Usage
just use command `schat` to communicate with ChatGPT
```shell
schat
```
example:
```
schat

🙋Please Input: Can u write a python hello world program and explain it
ChatGPT: ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Yes, I can write a Python hello world program and explain it.                                                                                                                                                                      

Here's the code:                                                                                                                                                                                                                   

                                                                                                                                                                                                                                   
 print("Hello, World!")                                                                                                                                                                                                            
                                                                                                                                                                                                                                   

Explanation:                                                                                                                                                                                                                       

 • print() is a built-in Python function used to display text on the screen.                                                                                                                                                       
 • "Hello, World!" is the text we want to display. It's enclosed in double quotes to indicate that it's a string literal.                                                                                                          
 • The entire statement is terminated by a parenthesis followed by a newline character, which tells Python to execute the statement and move on to the next line.                                                                  

When we run this program, the output will be:                                                                                                                                                                                      

                                                                                                                                                                                                                                   
 Hello, World!                                                                                                                                                                                                                     
                                                                                                                                                                                                                                   

This is a very simple program, but it's often used as a first example when learning a new programming language because it's easy to understand and illustrates the basic syntax of the language.                                   
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── token prompt:73, completion:167, total:240

🙋Please Input: ....
```
