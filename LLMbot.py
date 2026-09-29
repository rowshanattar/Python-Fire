'''
In this file, we build a CLI using the click library. The main function uses Claude with a simple prompt: "Give me a summary about {Microsoft, Machine Learning, Python, etc.} in x sentences." The output is printed in the console.
'''

import click
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()  # reads ANTHROPIC_API_KEY from the environment


@click.command()
@click.option('--topic', prompt='Enter a topic', help='The topic to summarize')
@click.option('--sentences', default=2, help='The number of sentences for the summary')
def claude(topic, sentences):
    """Generate a summary about the given topic in the specified number of sentences."""
    message = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=1024,
        system="You are a helpful assistant that summarizes topics in a concise manner.",
        messages=[
            {
                "role": "user",
                "content": f"Give me a summary about {topic} in {sentences} sentences.",
            }
        ],
    )

    click.echo(message.content[0].text)
    return message.content[0].text  # Return the summary for testing purposes


if __name__ == '__main__':
    claude()