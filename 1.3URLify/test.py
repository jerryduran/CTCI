def urlify(in_str, in_str_length):
    return ''.join('%20'if c == " " or c == ' ' else c for c in  in_str[:in_str_length])


new_str = urlify('Mr john Smith', 13)
print(new_str)
