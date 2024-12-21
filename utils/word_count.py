def count_words(text):
    """
    Count words in a given text.
    
    Args:
        text (str): The input text to count words from
        
    Returns:
        dict: Dictionary containing:
            - total_words: Total number of words
            - word_frequencies: Dictionary of word frequencies
            - sentence_count: Number of sentences
    """
    # Clean the text
    text = text.strip()
    
    # Split into words and clean each word
    words = text.split()
    cleaned_words = []
    
    for word in words:
        # Remove punctuation from edges of words
        word = word.strip(".,!?():;\"'")
        if word:  # Only add non-empty strings
            cleaned_words.append(word.lower())
    
    # Count word frequencies
    word_frequencies = {}
    for word in cleaned_words:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    
    # Count sentences (roughly - looks for .!?)
    sentence_count = len([char for char in text if char in '.!?'])
    if sentence_count == 0 and len(text) > 0:
        sentence_count = 1  # Text without sentence endings counts as 1 sentence
    
    return {
        'total_words': len(cleaned_words),
        'word_frequencies': word_frequencies,
        'sentence_count': sentence_count
    }

# Example usage
if __name__ == "__main__":
    sample_text = """Early access testing offers a crucial opportunity to examine how frontier AI models maintain alignment with human values and intentions as their capabilities advance. As these models develop increasingly sophisticated reasoning abilities, early testers play a vital role in understanding how well they preserve and interpret human values across complex scenarios. This is particularly critical given the potential for subtle misalignments to compound into significant problems as AI systems become more capable.
The core challenge isn't just about preventing obvious failures or harmful outputs - it's about deeply understanding how these models interpret and pursue human-specified goals. Through early testing, we can explore how models handle increasingly abstract objectives, watching for signs of potential misalignment that could emerge as capabilities scale. This includes examining how models balance competing priorities, handle ambiguous instructions, and maintain appropriate constraints when optimizing for given goals.
Independent testing from diverse perspectives is especially valuable for alignment challenges. Each tester brings different scenarios and edge cases that probe how models maintain alignment with human values under pressure. This variety of approaches helps identify subtle misalignment risks that might be missed by more narrowly focused testing. Working alongside leading safety institutions, early testers can build a more comprehensive understanding of how to keep AI systems reliably aligned with human interests as they grow more powerful.
The flexibility of early access allows testers to explore crucial alignment scenarios: How do models handle increasingly abstract goals while maintaining alignment with human values? What happens when optimizing for one objective creates tensions with unstated but important human values? Can models reliably distinguish between intended outcomes and potentially harmful literal interpretations of instructions? These hands-on evaluations help surface potential alignment failures before they become critical issues in deployed systems.
At its core, early access testing is about ensuring that as AI systems become more capable, they remain fundamentally aligned with human values and interests. By carefully examining how these models handle complex goal structures and maintain alignment across different scenarios, testers can help build AI systems that reliably pursue beneficial outcomes while avoiding the pitfalls of misaligned optimization."""
    
    results = count_words(sample_text)
    
    print(f"Total words: {results['total_words']}")
    print(f"Sentence count: {results['sentence_count']}")
    print("\nWord frequencies:")
    for word, count in sorted(results['word_frequencies'].items()):
        print(f"{word}: {count}")