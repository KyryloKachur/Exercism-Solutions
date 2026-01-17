"""Functions for creating, transforming, and adding prefixes to strings."""

def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    result = []
    result.append(prefix)
    for word in vocab_words[1:]:
        result.append(prefix + word)
    result = " :: ".join(result)
    return result
        
def remove_suffix_ness(word):
    new_word = word[:-4][:-1] + "y" if word[:-4].endswith("i") else word[:-4]
    return new_word
    
def adjective_to_verb(sentence, index):
    word = sentence.split()[index]
    new_word = word.strip(".,") + "en"
    return new_word
   
