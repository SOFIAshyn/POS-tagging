def compute_accuracy(pred, y):
    '''
    Input:
        pred: a list of the predicted parts-of-speech
        y: a list of lines where each word is separated by a '\t' (i.e. word \t tag)
    Output:

    '''
    num_correct = 0
    total = 0

    # Zip together the prediction and the labels
    for prediction, y in zip(pred, y):
        # Check if the POS tag label matches the prediction
        if y.strip() == prediction.strip():  # complete this line
            # count the number of times that the prediction
            # and label match
            num_correct += 1
        # keep track of the total number of examples (that have valid labels)
        total += 1

    return num_correct / total