import re
str_data = "Doesn't anybody-stay in one place anymore. It would be so fine to see your face at 2 my door."
x = re.findall(r'\ba\w+[-\s0-9.]*([a-zA-Z]+)', str_data)
print(x)

