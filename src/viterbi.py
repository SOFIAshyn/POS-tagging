import math
from math import log


def viterbi_forward(A, B, test_corpus, best_probs, best_paths, vocab):
    '''
    Input:
        A, B: The transition and emission matrices respectively
        test_corpus: a list containing a preprocessed corpus
        best_probs: an initilized matrix of dimension (num_tags, len(corpus))
        best_paths: an initilized matrix of dimension (num_tags, len(corpus))
        vocab: a dictionary where keys are words in vocabulary and value is an index
    Output:
        best_probs: a completed matrix of dimension (num_tags, len(corpus))
        best_paths: a completed matrix of dimension (num_tags, len(corpus))
    '''
    # Get the number of unique POS tags (which is the num of rows in best_probs)
    num_tags = best_probs.shape[0]

    # Go through every word in the corpus starting from word 1
    # Recall that word 0 was initialized in `initialize()`
    for i in range(1, len(test_corpus)):

        # Print number of words processed, every 5000 words
        # if i % 5000 == 0:
        #     print("Words processed: {:>8}".format(i))

        # For each unique POS tag that the current word can be
        for j in range(num_tags):  # complete this line

            # Initialize best_prob for word i to negative infinity
            best_prob_i = float('-inf')

            # Initialize best_path for current word i to None
            best_path_i = None

            # For each POS tag that the previous word can be:
            for k in range(num_tags):  # complete this line
                # print(f'A[k, j] = {A[k, j]}')
                # print(f'vocab[test_corpus[i]] = {vocab[test_corpus[i]]}; test_corpus[i] = {test_corpus[i]}')
                # print(f'B[j, vocab[test_corpus[i]]] = {B[j, vocab[test_corpus[i]]]}')

                # Calculate the probability =
                # best probs of POS tag k, previous word i-1 +
                # log(prob of transition from POS k to POS j) +
                # log(prob that emission of POS j is word i)
                prob = best_probs[k, i - 1] + log(A[k, j]) + log(B[j, vocab[test_corpus[i]]])

                # check if this path's probability is greater than
                # the best probability up to and before this point
                if prob > best_prob_i:  # complete this line

                    # Keep track of the best probability
                    best_prob_i = prob

                    # keep track of the POS tag of the previous word
                    # that is part of the best path.
                    # Save the index (integer) associated with
                    # that previous word's POS tag
                    best_path_i = k

            # Save the best probability for the
            # given current word's POS tag
            # and the position of the current word inside the corpus
            best_probs[j, i] = best_prob_i

            # Save the unique integer ID of the previous POS tag
            # into best_paths matrix, for the POS tag of the current word
            # and the position of the current word inside the corpus.
            best_paths[j, i] = best_path_i

    return best_probs, best_paths


def viterbi_backward(best_probs, best_paths, corpus, states):
    '''
    This function returns the best path.

    '''
    # Get the number of words in the corpus
    # which is also the number of columns in best_probs, best_paths
    m = best_paths.shape[1]

    # Initialize array z, same length as the corpus
    z = [None] * m

    # Get the number of unique POS tags
    num_tags = best_probs.shape[0]

    # Initialize the best probability for the last word
    best_prob_for_last_word = float('-inf')

    # Initialize pred array, same length as corpus
    pred = [None] * m

    ## Step 1 ##

    # Go through each POS tag for the last word (last column of best_probs)
    # in order to find the row (POS tag integer ID)
    # with highest probability for the last word
    for k in range(num_tags):  # complete this line

        # If the probability of POS tag at row k
        # is better than the previously best probability for the last word:
        if best_probs[k, -1] > best_prob_for_last_word:  # complete this line

            # Store the new best probability for the last word
            best_prob_for_last_word = best_probs[k, -1]

            # Store the unique integer ID of the POS tag
            # which is also the row number in best_probs
            z[m - 1] = k

    # Convert the last word's predicted POS tag
    # from its unique integer ID into the string representation
    # using the 'states' list
    # store this in the 'pred' array for the last word
    pred[m - 1] = states[z[-1]]

    ## Step 2 ##
    # Find the best POS tags by walking backward through the best_paths
    # From the last word in the corpus to the 0th word in the corpus
    for i in range(m - 1, 0, -1):  # complete this line

        # Retrieve the unique integer ID of
        # the POS tag for the word at position 'i' in the corpus
        pos_tag_for_word_i = z[i]

        # In best_paths, go to the row representing the POS tag of word i
        # and the column representing the word's position in the corpus
        # to retrieve the predicted POS for the word at position i-1 in the corpus
        #         print(np.argmax(best_paths[:,i]), pos_tag_for_word_i)
        z[i - 1] = best_paths[pos_tag_for_word_i, i]

        # Get the previous word's POS tag in string form
        # Use the 'states' list,
        # where the key is the unique integer ID of the POS tag,
        # and the value is the string representation of that POS tag
        pred[i - 1] = states[z[i - 1]]

    return pred