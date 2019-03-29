from language.language_help import C_to_N

def words_to_number(words, pattern = "1-111-111-1111"):
    dashes = get_dash_locations(pattern)

    number_out = words.replace('-','')

    for k in C_to_N.keys():
    	number_out = number_out.replace(k,C_to_N[k])

    for idx in dashes:
    	number_out = number_out[:idx] + '-' + number_out[idx:]

    return number_out

def get_dash_locations(pattern):
    dashes = []
    for i,c in enumerate(pattern):
        if c == '-':
            dashes += [i]
    return dashes