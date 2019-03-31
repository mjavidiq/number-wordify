from language.language_help import C_to_N

# Maps a wordified phone number back to its original phone number
#   of the form given by the input patter. Defaults to a 10-digit
#   US phone number.
def words_to_number(words, pattern = "1-111-111-1111"):
    dashes = get_dash_locations(pattern)

    number_out = words.replace('-','')
    number_out = C_to_N(number_out)

    for idx in dashes:
        number_out = number_out[:idx] + '-' + number_out[idx:]

    return number_out

# Finds the locations of the dashes in the given pattern
def get_dash_locations(pattern):
    dashes = []
    for i,c in enumerate(pattern):
        if c == '-':
            dashes += [i]
    return dashes