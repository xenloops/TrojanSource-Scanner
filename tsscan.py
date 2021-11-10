# Short POC for reporting Unicode directional control characters in source code,
# an attack revealed by the paper "Trojan Source: Invisible Vulnerabilities"
#
# @article{boucher_trojansource_2021,
#   title = {Trojan {Source}: {Invisible} {Vulnerabilities}},
#   author = {Nicholas Boucher and Ross Anderson},
#   year = {2021},
#   journal = {Preprint},
#   eprint = {2111.00169},
#   archivePrefix = {arXiv},
#   primaryClass = {cs.CR},
#   url = {https://arxiv.org/abs/2111.00169}
# }
# 
# By Nathan Larson 9 Nov 2021
# More info at https://trojansource.codes/

import sys
if sys.getdefaultencoding() == "utf-8":
    print("UTF-8 supported; good to go!")
else:
    print("This probably won't work if the system doesn't support UTF-8.")

with open('evilexample.java') as file:
    fileGuts = file.read()
    charCount = 0
    for char in fileGuts:
        charCount += 1
        if char == '\u202A': print("LRE at char " + str(charCount))
        if char == '\u202B': print("RLE at char " + str(charCount))
        if char == '\u202D': print("LRO at char " + str(charCount))
        if char == '\u202E': print("RLO at char " + str(charCount))
        if char == '\u2066': print("LRI at char " + str(charCount))
        if char == '\u2067': print("RLI at char " + str(charCount))
        if char == '\u2068': print("FSI at char " + str(charCount))
        if char == '\u202C': print("PDF at char " + str(charCount))
        if char == '\u2069': print("PDI at char " + str(charCount))

print("== END ==")

    