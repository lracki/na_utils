"""
Convert DNA sequences to RNA sequences
"""
def rna(seq):
    """Convert a DNA sequence to RNA."""

    #determine if the original sequence was uppercase
    seq_upper = seq.isupper()

    #convert to lowercase
    seq = seq.lower()

    #swap out 't' for 'u':
    seq = seq.replace('t','u')

    #return upper or lower, depending on input
    if seq_upper:
        return seq.upper()
    else:
        return seq



def reverse_complement(seq):
    """Convert a DNA sequence into its reverse complement as RNA"""

    #determine if the original sequence was uppercase
    seq_upper = seq.isupper()

    # reverse sequence
    seq = seq[::-1]

    # Convert to uppercase
    seq = seq.upper()

    # compute complement
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')

    # return in appropriatecase
    if seq_upper:
        return seq.upper()
    else:
        return seq
        
def reverse_rna_complement(seq):
    """Convert a DNA sequence into its reverse complement as RNA"""

    #determine if the original sequence was uppercase
    seq_upper = seq.isupper()

    # reverse sequence
    seq = seq[::-1]

    # Convert to uppercase
    seq = seq.upper()

    # compute complement
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')

    # return in appropriatecase
    if seq_upper:
        return seq.upper()
    else:
        return seq
