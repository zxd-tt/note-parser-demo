# Note parser demo for personal LLM test
def parse_text_note(raw_text):
    return f"Parsed content: {raw_text}"

if __name__ == "__main__":
    test_note = "Test memo content"
    result = parse_text_note(test_note)
    print(result)
