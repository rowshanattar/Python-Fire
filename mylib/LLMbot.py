
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()  # reads ANTHROPIC_API_KEY from the environment


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
    return message.content[0].text  # Return the summary for testing purposes
