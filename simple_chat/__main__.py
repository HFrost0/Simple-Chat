import os
import openai
from rich.console import Console
from rich.markdown import Markdown
from rich.rule import Rule
import logging


def main():
    if not (key := os.getenv("OPENAI_API_KEY")):
        return logging.error(" Can not find OPENAI_API_KEY, pls set env variable")
    console = Console()
    openai.api_key = key
    messages = []
    while s := input("🙋Please Input: "):
        messages.append({"role": "user", "content": s})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        msg = response['choices'][0]['message']
        usage = response['usage']
        console.print(
            Rule(title="ChatGPT:", align="left", style="cyan"),
            Markdown(msg['content']),
            Rule(title=f"token prompt:{usage['prompt_tokens']}, completion:{usage['completion_tokens']},"
                       f" total:{usage['total_tokens']}", style="cyan", align="right"), "",
        )
        messages.append(msg)


if __name__ == '__main__':
    main()
