import re

stra="kewal"
word="kewal"
kw=word.replace("e","_")
pattern=r"[aeiou]"
pat=re.sub(pattern,"_",stra)
print(pat)
print(kw)
hi=list(word)
print(hi)
print(hi[1])
for le in word:
   print(le)



print(word)
