import re


#r'' results in the raw string
#/d recognised a digit character
MRegex = re.compile(r'^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$')
#UKNumbRegex = re.compile(r'+44/d/d/d/d/d/d/d/d/d/d')

mo = MRegex.search('ksarhgbaksjvbasf 07414949199 asfasjgl +447414949199 askldjbvaksljdf 447414949199'
)


print(mo.group())
