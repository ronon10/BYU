import random

def get_determiner(quantity):
    """Return a randomly chosen determiner."""
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

def get_noun(quantity):
    """Return a randomly chosen noun."""
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(words)

def get_verb(quantity, tense):
    """Return a randomly chosen verb."""
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:  # tense == "future"
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    return random.choice(words)

def get_adjective():
    """Return a randomly chosen adjective."""
    adjectives = ["small", "big", "red", "blue", "old", "young", "happy", "sad", "fast", "slow"]
    return random.choice(adjectives)

def get_adverb():
    """Return a randomly chosen adverb."""
    adverbs = ["quickly", "slowly", "gracefully", "awkwardly", "happily", "sadly", "loudly", "silently"]
    return random.choice(adverbs)

def get_preposition():
    """Return a randomly chosen preposition."""
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", 
                    "onto", "out", "over", "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase."""
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()
    return f"{preposition} {determiner} {adjective} {noun}"

def make_sentence(quantity, tense):
    """Build and return a sentence with a determiner, noun, verb, adverb, and two prepositional phrases."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()
    verb = get_verb(quantity, tense)
    adverb = get_adverb()
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    
    sentence = f"{determiner.capitalize()} {adjective} {noun} {verb} {adverb} {prepositional_phrase1} {prepositional_phrase2}."
    return sentence

def main():
    # Generate and print six sentences
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

# Call main function to generate sentences
if __name__ == "__main__":
    main()
