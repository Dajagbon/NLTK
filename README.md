# Text Processing and Analysis Project

## Purpose

This project's purpose is to perform text processing and analysis on a set of text files. It includes tokenization, stemming, lemmatization, part-of-speech tagging, named entity recognition, and n-gram frequency analysis. The results are stored and displayed for each text file.

## Project Structure

The project consists of a single Python script, `NLTK.py`, which performs the following tasks:

1. **Download necessary NLTK data**: Ensures all required NLTK data packages are available.
2. **Define file paths**: Specify the paths to the text files to be processed.
3. **Process each text file**: Reads the content of each text file, performs various text processing tasks, and stores the results.
4. **Display results**: Prints the most common words, most common trigrams, and the number of named entities for each text file.

## Implementation

The project does not use custom classes but uses functions and standard Python libraries to perform the tasks. Below is an explanation of the key components:

### Functions

#### `process_text(file_path, n=3)`

- **Purpose**: Processes a single text file and performs tokenization, stemming, lemmatization, part-of-speech tagging, named entity recognition, and n-gram frequency analysis.
- **Parameters**:
  - `file_path` (str): The path to the text file to be processed.
  - `n` (int): The number of tokens to include in each n-gram (default is 3 for trigrams).
- **Attributes**:
  - `tokens` (list): The list of tokens obtained from tokenizing the text.
  - `stemmed_tokens` (list): The list of tokens after applying stemming.
  - `lemmatized_tokens` (list): The list of tokens after applying lemmatization.
  - `word_freq` (Counter): The frequency distribution of lemmatized tokens.
  - `ngrams_list` (list): The list of n-grams created from lemmatized tokens.
  - `ngrams_freq` (Counter): The frequency distribution of n-grams.
  - `pos_tags` (list): The list of token part-of-speech tags.
  - `named_entities` (Tree): The named entity tree obtained from named entity recognition.
  - `named_entity_count` (int): The count of named entities in the text.
- **Returns**: None (results are stored in global dictionaries).

### Global Dictionaries

- **`all_word_freqs`**: Stores the word frequency and n-gram frequency for each text file.
- **`all_named_entities`**: Stores the named entity count for each text file.

## Usage

1. Ensure you have the necessary NLTK data packages by running the script.
2. Define the paths to the text files you want to process.
3. Run the script to process each text file and display the results.

## Limitations

- The script assumes that the text files are encoded in UTF-8. If the files use a different encoding, you may need to adjust the encoding parameter in the `open` function.
- The n-gram analysis is limited to trigrams by default. You can change the value of `n` in the `process_text` function call to analyze different n-gram sizes.
- The script processes each text file sequentially and stores the results in memory. For very large text files or a large number of files, this may lead to high memory usage.

## Example

To process a set of text files and display the results, run the script with the following command:


python NLTK.py

The script will print the most common words, most common trigrams, and the number of named entities for each text file.

**Dependencies**

- Python 3.x

- NLTK

- Collections

Ensure you have the necessary libraries installed by running:

**pip install nltk**

## Conclusion

This project provides a comprehensive text processing and analysis tool using NLTK. It demonstrates the use of various NLP techniques and provides a foundation for further text analysis and processing tasks.
