'''
In this file, we build a CLI using the click library. The main function uses Claude with a simple prompt: "Give me a summary about {Microsoft, Machine Learning, Python, etc.} in x sentences." The output is printed in the console.
'''

import click
from anthropic import Anthropic
from dotenv import load_dotenv
from mylib.LLMbot import claude

load_dotenv()
client = Anthropic()  # reads ANTHROPIC_API_KEY from the environment


@click.command()
@click.option('--topic', prompt='Enter a topic', help='The topic to summarize')
@click.option('--sentences', default=2, help='The number of sentences for the summary')
def main():
    topic = click.prompt('Enter a topic')
    sentences = click.prompt('Enter the number of sentences for the summary', default=2, type=int)
    claude(topic, sentences)



if __name__ == '__main__':
    main()