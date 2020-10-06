def calculate_subpeptides_liner_peptide(n):
    '''The number of subpeptides of a linear peptide of length n'''
    L=1
    while n>=0:
        L=L+n
        n=n-1
    return L

print(calculate_subpeptides_liner_peptide(38996))
