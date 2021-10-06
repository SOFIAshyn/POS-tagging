# Creataed by Sofiia Petryshyn, 22/02/2021
# Universal POS Tags: https://arxiv.org/abs/1104.2086
# 25 page, Table 2.3 : https://etd.ohiolink.edu/apexprod/rws_etd/send_file/send?accession=kent1448502094&disposition=inline

UNIVERSAL_POS_DICTIONARY = {
    'ADJ': ('JJ', 'JJ+', 'JJR', 'JJT', 'VVGJ', 'VVN', 'VVN+', 'VVNJ'),  # adjective: big, old, last
    'ADP': ('II', 'II+', 'TO'),  # adposition: at home, in Milan
    'ADV': ('RR', 'RR+', 'RRR', 'RRT', 'VBG', 'VVG'),  # adverb: very, well, exactly
    'AUX': ('VM', ),  # auxiliary verb: has, is, was
    'CONJ': ('CC', 'CC+', 'CSN'),  # coordinating conjunction: and or but
    'DET': ('DB', ),  # determiner: this which what
    'INTJ': ('DD', ),  # interjection: bravo, hello
    'NOUN': ('NN', 'NN+', 'NNP', 'VVGN'),  # noun
    'NUM': ('MC', ),  # numeral
    'PART': ('CST', ),  # particle
    'PRON': ('PN', 'PNG', 'PND', 'PNR'),  # pronoun
    'PROPN': ('NNS', ),  # proper noun
    'PUNCT': ("''", "(", ")", ",", ".", ":", "GE", "``"),  # punctuation # SPACE
    'SCONJ': ('CS', 'CS+'),  # subordinating conjunction
    'SYM': ('SYM',),  # symbol
    'VERB': ('EX', 'VBB', 'VBD', 'VBI', 'VBN', 'VBZ', 'VHB', 'VHD', 'VHG', 'VHI', 'VHZ', 'VVB', 'VVB+', 'VVD', 'VVD+', 'VVI', 'VVI+', 'VVZ'),  # verb
    'X': (),  # other
}
