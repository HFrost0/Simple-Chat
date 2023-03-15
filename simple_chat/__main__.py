import os
import click
import openai
from contextlib import contextmanager
from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown
from rich.spinner import Spinner
from rich.rule import Rule
import logging
# to enable command line editing using GNU readline.
import readline


@contextmanager
def bye():
    try:
        yield
    except KeyboardInterrupt:
        pass
    finally:
        print("\nbye\n")


@click.command()
@click.argument("system_prompt", type=str, required=False)
@click.option('--no-stream', 'stream', is_flag=True, default=True, help="if no stream, token usage will be shown.")
@bye()
def main(system_prompt: str, stream: bool):
    if not (key := os.getenv("OPENAI_API_KEY")):
        return logging.error(" Can not find OPENAI_API_KEY, pls set env variable")
    console = Console()
    openai.api_key = key
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    while s := input("🙋Please Input: "):
        messages.append({"role": "user", "content": s})
        with Live(Spinner(name="dots", text="connecting...", style="green"), console=console) as live:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                stream=stream,
            )
            live.update("")
        console.print(Rule(title="ChatGPT:", align="left", style="cyan"))
        if stream:
            msg = ""
            with Live(console=console, auto_refresh=False) as live:
                for chunk in response:
                    msg += chunk['choices'][0]['delta'].get('content', '')
                    live.update(Markdown(msg), refresh=True)
            console.print(Rule(style="cyan"), "")
            messages.append({'role': 'assistant', 'content': msg})
        else:
            msg = response['choices'][0]['message']
            usage = response['usage']
            console.print(
                Markdown(msg['content']),
                Rule(title=f"token prompt:{usage['prompt_tokens']}, completion:{usage['completion_tokens']},"
                           f" total:{usage['total_tokens']}", style="cyan", align="right"), "")
            messages.append(msg)


if __name__ == '__main__':
    main()
