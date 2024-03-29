def file_split(f_in, f_word, f_words):
    """
    -------------------------------------------------------
    Copies the contents of f_in to f_word and f_words depending
    on the contents of f_in:
        Lines containing a single word are copied to f_word.
        Lines containing more than one word are copied to f_words.
        Empty lines are ignored.
    Use: file_split(f_in, f_word, f_words)
    -------------------------------------------------------
    Parameters:
        f_in - source file (file handle - already open for reading)
        f_word - file to contain lines with single words from f_in (file handle
            - already open for writing)
        f_words - file to contain lines with multiple words from f_in
            (file handle - already open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    # Your code here
    for line in f_in:
        line = line.strip()
        if not line:
            continue

    words = line.split()
    if len(words) == 1:
      f_word.write(line + "\n")
    else:
      f_words.write(line + "\n")
      