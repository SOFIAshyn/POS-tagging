from main.helpers.specific_tagging import assign_unk
from main.helpers.init import initialize
from main.helpers.viterbi import viterbi_forward, viterbi_backward
from main.helpers.print_examples import print_data_example, print_emission, print_transition, print_examples_of_prediction


def get_prep(f_data_list_test, vocab):
    '''
    Change unknown words to be exact tokens
    :param f_data_list_test: list(str: words)
    :param vocab: dict(word: number)
    :return: list(str), list(str)
    '''
    orig, prep = [], []
    for word in f_data_list_test:
        word = word.strip().lower()
        orig += [word]
        if vocab.get(word, None) is None:
            word = assign_unk(word)
        prep += [word]
    return orig, prep


def run_pos_algorithm(f_data_list_test, vocab, tag_counts, states, A, B):
    '''
    Pass here test data as a list of words, some prepared dicts
    and lists to get a pre-processing and then prediction.
    :param f_data_list_test: list( 'word', ... )
    :param vocab: dict(word: unique num)
    :param tag_counts: dict(tag: count)
    :param states: list(tags)
    :param A: np array
    :param B: np array
    :return: list(orig words), list(modified words), list(predicted words)
    '''
    orig, prep = get_prep(f_data_list_test, vocab)

    best_probs, best_paths = initialize(states, tag_counts, A, B, prep, vocab, s_token='NOUN')
    best_probs, best_paths = viterbi_forward(A, B, prep, best_probs, best_paths, vocab)
    pred = viterbi_backward(best_probs, best_paths, prep, states)
    return orig, prep, pred


def get_prep_and_y(f_data_list_valid, vocab):
    '''
    Prepare unknown words and structures of words and labels.
    :param vocab: dict(word: num)
    :param f_data_list_valid: list( 'word tag', ... )
    :return: list(orig words), list(modified words), list(labels)
    '''
    orig, prep, y = [], [], []
    for line in f_data_list_valid:
        try:
            word = line.split()[0]
            orig += [word]
            if vocab.get(word, None) is None:
                word = assign_unk(word)
            prep += [word]
            y += [line.split()[1]]
        except IndexError:
            pass
    return orig, prep, y


def validate_algorithm(f_data_list_valid, vocab, tag_counts, states, A, B):
    '''
    Pass here validation data that you want to predict labels for.
    :param f_data_list_valid: list( 'word tag', ... )
    :param vocab: dict(word: unique num)
    :param tag_counts: dict(tag: count)
    :param states: list(tags)
    :param A: np array
    :param B: np array
    :return: list(orig words), list(modified words), list(predicted words), list(labels)
    '''
    orig, prep, y = get_prep_and_y(f_data_list_valid, vocab)

    best_probs, best_paths = initialize(states, tag_counts, A, B, prep, vocab, s_token='NOUN')
    best_probs, best_paths = viterbi_forward(A, B, prep, best_probs, best_paths, vocab)
    pred = viterbi_backward(best_probs, best_paths, prep, states)
    return orig, prep, pred, y
