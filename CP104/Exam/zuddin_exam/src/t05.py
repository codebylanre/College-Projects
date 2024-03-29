from t05_functions import file_split 
# Your code here
# open the files "source.txt", "word.txt" and "words.txt" in appropriate mode, process and close the files.
# Open the source file for reading
with open('source.txt', 'r') as f_in:
    #Open output file for writing
    with open('word.txt', 'w') as f_word, open('words.txt', 'w') as f_words:
        #make function split file contents
        file_split(f_in, f_word, f_words)
