import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

def main():
    # Define the grammar
    grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | NP PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'man' | 'dog' | 'cat' | 'telescope' | 'park'
    V -> 'saw' | 'walked'
    P -> 'in' | 'with'
    """)

    # Create the parser
    parser = RecursiveDescentParser(grammar)

    # Get input from the user
    sentence = input("Enter a sentence: ").strip().lower()
    sentence_tokens = sentence.split()

    # Parse the sentence
    try:
        for tree in parser.parse(sentence_tokens):
            print(tree)
            tree.pretty_print()
    except ValueError as e:
        print(f"Error parsing sentence: {e}")

if __name__ == "__main__":
    main()
