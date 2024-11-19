txt = (
    "@Developer It is possible to have a report that has no mean"
    "ing at all, called "
    "a zero meaning report, as in the\n"
    "https://medor-specific examples from Pythonista et al. (2018):\n"
    "EN [Peter]i la la ftp://medium.com #NPL @developer\n"
    "XXXXX"
)


import re

print(txt)

print()

txt = re.sub(r"#\S", "", txt)
print(txt)

print()

txt = re.sub("(http[s]?)|(ftp)\://\S+", "", txt)
print(txt)