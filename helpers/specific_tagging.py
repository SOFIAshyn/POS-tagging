"""
Created by Sofiia Petryshyn 16/02/21
"""

import string

# Punctuation characters
punct = set(string.punctuation)

# Morphology rules used to assign unknown word tokens
noun_suffix = ["action", "age", "ance", "cy", "dom", "ee", "ence", "er", "hood", "ion", "ism", "ist", "ity", "ling",
               "ment", "ness", "or", "ry", "scape", "ship", "ty"]
verb_suffix = ["ate", "ify", "ise", "ize"]
adj_suffix = ["able", "ese", "ful", "i", "ian", "ible", "ic", "ish", "ive", "less", "ly", "ous"]
adv_suffix = ["ward", "wards", "wise"]

# All POS tags of the SpaCy pos data (POS notation: https://universaldependencies.org/u/pos/all.html#al-u-pos/X):
# We have added --s--
# ['SPACE', 'ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'DET', 'INTJ',
# 'NOUN', 'NUM', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X']


def get_word_tag(line, vocab):
    def word_tag_of_an_empty_line():
        word = "--n--"  # it was an empty line, so the word in none
        tag = "SPACE"
        return word, tag
    if not line.split():
        return word_tag_of_an_empty_line()
    else:
        # try:
        word, tag = line.split()[0].lower(), line.split()[1]
        # except (ValueError, IndexError) as err:
        #     if line.strip() == 'SPACE':
        #         return word_tag_of_an_empty_line()
        #     return None, None
        if vocab.get(word, None) is None:
            # Handle unknown words
            word = assign_unk(word)
            tag = tag
        return word, tag


def assign_unk(tok):
    """
    Assign unknown word tokens
    """
    # Digits
    if any(char.isdigit() for char in tok):
        return "--unk_digit--"

    # Punctuation
    elif any(char in punct for char in tok):
        return "--unk_punct--"

    # Upper-case
    elif any(char.isupper() for char in tok):
        return "--unk_upper--"

    # Nouns
    elif any(tok.endswith(suffix) for suffix in noun_suffix):
        return "--unk_noun--"

    # Verbs
    elif any(tok.endswith(suffix) for suffix in verb_suffix):
        return "--unk_verb--"

    # Adjectives
    elif any(tok.endswith(suffix) for suffix in adj_suffix):
        return "--unk_adj--"

    # Adverbs
    elif any(tok.endswith(suffix) for suffix in adv_suffix):
        return "--unk_adv--"

    return "--unk--"

# def assign_unk(tok):
#     """
#     Assign unknown word tokens
#     """
#     # Digits
#     if any(char.isdigit() for char in tok):
#         return "NUM"
#
#     # Punctuation
#     elif any(char in punct for char in tok):
#         if any(char in [',', '.', '(', ')'] for char in tok):
#             return "PUNCT"
#         else:
#             return 'SYM'
#
#     # Upper-case
#     elif any(char.isupper() for char in tok):
#         return "NOUN"
#
#     # Nouns
#     elif any(tok.endswith(suffix) for suffix in noun_suffix):
#         return "NOUN"
#
#     # Verbs
#     elif any(tok.endswith(suffix) for suffix in verb_suffix):
#         return "VERB"
#
#     # Adjectives
#     elif any(tok.endswith(suffix) for suffix in adj_suffix):
#         return "ADJ"
#
#     # Adverbs
#     elif any(tok.endswith(suffix) for suffix in adv_suffix):
#         return "ADV"
#
#     return "X"
