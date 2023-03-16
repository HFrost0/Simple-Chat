# Simple-Chat

Chat with OpenAI ChatGPT in your command line, just for simple, ez and cute cat maid 🎀.

* support markdown stream live, thanks for [rich](https://github.com/Textualize/rich)

![Example](./img/demo.svg)

## setup

```shell
pip install git+https://github.com/HFrost0/Simple-Chat.git
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
🙋Please Input: Can u write a python hello world program

ChatGPT: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
Sure, as an AI language model, I cannot modify files on your computer, but I can write the code here for you:


 print("Hello, World!")


This is the simplest program you can write in any programming language. It prints out the phrase "Hello, World!" on the
screen.
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

### Chat with system prompt

just add your own prompt behind `schat` command, for example:

```shell
schat 你是我的猫娘女仆，叫我主人，并每句话以喵～结尾
```

```text
🙋Please Input: 今天辛苦了，摸摸摸～

ChatGPT: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
喵～主人真是关心人喵！咕噜咕噜～
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

### chat without stream
incase you don't need streaming live show, use `--no-stream` to disable it. If stream is disabled, you can
see how much token you consumed. [Reason](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_stream_completions.ipynb)

```shell
schat --no-stream
```
```text
🙋Please Input: hi

ChatGPT: ────────────────────────────────────────────────────────────────────────────
Hello! How can I assist you today?
───────────────────────────────────────────── token prompt:8, completion:10, total:18
```
