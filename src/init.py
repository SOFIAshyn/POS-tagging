"""
Created by Sofiia Petryshyn 16/02/21
"""

import math
import numpy as np


def initialize(states, tag_counts, A, B, corpus, vocab, s_token='SPACE'):
    '''
    Input:
        states: a list of all possible parts-of-speech
        tag_counts: a dictionary mapping each tag to its respective count
        A: Transition Matrix of dimension (num_tags, num_tags)
        B: Emission Matrix of dimension (num_tags, len(vocab))
        corpus: a sequence of words whose POS is to be identified in a list
        vocab: a dictionary where keys are words in vocabulary and value is an index
    Output:
        best_probs: matrix of dimension (num_tags, len(corpus)) of floats
        best_paths: matrix of dimension (num_tags, len(corpus)) of integers
    '''
    # Get the total number of unique POS tags
    num_tags = len(tag_counts)

    # Initialize best_probs matrix
    # POS tags in the rows, number of words in the corpus as the columns
    best_probs = np.zeros((num_tags, len(corpus)))

    # Initialize best_paths matrix
    # POS tags in the rows, number of words in the corpus as columns
    best_paths = np.zeros((num_tags, len(corpus)), dtype=int)

    # Define the start token
    s_idx = states.index(s_token)

    # Go through each of the POS tags
    for i in range(num_tags):  # complete this line

        # Handle the special case when the transition from start token to POS tag i is zero
        if A[s_idx, i] == 0:  # complete this line

            # Initialize best_probs at POS tag 'i', column 0, to negative infinity
            best_probs[i, 0] = float("-inf")

        # For all other cases when transition from start token to POS tag i is non-zero:
        else:
            # Initialize best_probs at POS tag 'i', column 0
            # Before doing this we do prep over the data we feed as a validation or
            # test set, so we change original data with unknown words into --unk-- words
            best_probs[i, 0] = np.vectorize(math.log)(A[s_idx, i]) + np.vectorize(math.log)(B[i, vocab[corpus[0]]])

    return best_probs, best_paths

