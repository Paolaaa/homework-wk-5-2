from __future__ import division
def get_at_content(dna):
#in order to get the correct AT content regardless of having a sequence with a bunch of unknow sequences we can remove all the N characters before the calculations are carried out
    dna = dna.replace('N','')
    length = len(dna)
#to solve the lower case problem, convert the input sequence to upper case before starting the calculation
    a_count = dna.upper() .count('A')
    t_count = dna.upper() .count('T')
    at_content = (a_count + t_count) / length
#the round function takes the argument you want to round and the number of sig. figs. you want.
    return round(at_content, 2)

my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
print(str(my_at_content))
print(get_at_content("ATGCGCGATCGATCGAATCG"))
print(get_at_content("aactgtagctagctagcagcgta"))



