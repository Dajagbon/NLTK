import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import ne_chunk, pos_tag
from nltk.util import ngrams
from collections import Counter

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')

# Define a list of file paths
file_paths = [
    "C:/Users/danie/Downloads/School/Info/RJ_Martin.txt",
    "C:/Users/danie/Downloads/School/Info/RJ_Lovecraft.txt",
    "C:/Users/danie/Downloads/School/Info/RJ_Tolkein.txt"
]

# Create dictionaries to store results
all_word_freqs = {}
all_named_entities = {}

# Function to process a single text file
def process_text(file_path):
    # Read the text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text
    tokens = word_tokenize(text)

    # Create stemmer and lemmatizer objects
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    # Apply stemming and lemmatization
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Create a frequency distribution for this text
    word_freq = Counter(lemmatized_tokens)

    # Store the word frequency for this file
    all_word_freqs[file_path] = word_freq

    # Perform POS tagging
    pos_tags = pos_tag(tokens)

    # Perform named entity recognition
    named_entities = ne_chunk(pos_tags)

    # Count named entities
    named_entity_count = sum(1 for chunk in named_entities if hasattr(chunk, 'label'))

    # Store the named entity count for this file
    all_named_entities[file_path] = named_entity_count

# Process each text file
for file_path in file_paths:
    process_text(file_path)

# Print results for each text file
for file_path, word_freq in all_word_freqs.items():
    print(f"\nMost common words in {file_path}:")
    most_common_words = word_freq.most_common(20)
    for word, count in most_common_words:
        print(f"{word}: {count}")

# Print named entity counts for each text file
for file_path, named_entity_count in all_named_entities.items():
    print(f"\nNumber of named entities in {file_path}: {named_entity_count}")

# Determine the subject of all three texts based on the most common tokens and named entities
print("\nDetermining the subject of all three texts:")
for file_path in file_paths:
    print(f"\nSubject analysis for {file_path}:")
    most_common_words = all_word_freqs[file_path].most_common(20)
    named_entity_count = all_named_entities[file_path]
    print(f"Most common words: {[word for word, count in most_common_words]}")
    print(f"Number of named entities: {named_entity_count}")
    # Simple heuristic to determine the subject based on common words and named entities
    if named_entity_count > 10:
        print("The text likely discusses specific people, places, or organizations.")
    else:
        print("The text likely discusses general topics or concepts.") 




# Define a list of file paths
file_paths = [
    "C:/Users/danie/Downloads/School/Info/RJ_Martin.txt",
    "C:/Users/danie/Downloads/School/Info/RJ_Lovecraft.txt",
    "C:/Users/danie/Downloads/School/Info/RJ_Tolkein.txt",
    "C:/Users/danie/Downloads/School/Info/Martin.txt"
]

# Function to process a single text file
def process_text(file_path, n=3):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    tokens = word_tokenize(text)

    # Create a lemmatizer object
    lemmatizer = WordNetLemmatizer()

    # Lemmatize tokens
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Create n-grams
    ngrams_list = list(ngrams(lemmatized_tokens, n))

    # Create a frequency distribution for n-grams
    ngram_freq = Counter(ngrams_list)

    # Get the 20 most common n-grams
    most_common_ngrams = ngram_freq.most_common(20)

    return most_common_ngrams

# Process each text file and print the most common trigrams
for file_path in file_paths:
    most_common_ngrams = process_text(file_path, n=3)
    print(f"\nMost common trigrams in {file_path}:")
    for ngram, count in most_common_ngrams:
        print(f"{ngram}: {count}")