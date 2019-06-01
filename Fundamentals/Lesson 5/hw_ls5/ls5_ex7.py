# write a function that removes the dollar sign ($) in a string

def remove_dollar_sign(s):
    str = s.replace('$', '')
    return str

remove_sign = remove_dollar_sign("I have $50 in my bank account.")
print(remove_sign)