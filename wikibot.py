import wikipedia

def scrape(name, sentences=2):
    try:
        summary = wikipedia.summary(name, sentences=sentences)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e.options}"
    except wikipedia.exceptions.PageError:
        return "Page not found."
    except Exception as e:
        return f"An error occurred: {e}"

result = scrape("Microsoft", 2)
print(result)