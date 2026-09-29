from mylib.LLMbot import claude

def test_claude():
    # Test with a sample topic and number of sentences
    topic = "python"
    sentences = 2
    result = claude(topic, sentences)
    
    # Check if the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0
    assert topic in result.lower()  # Ensure the topic is mentioned in the summary