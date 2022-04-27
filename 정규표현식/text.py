a="kbs ccca"

text="""
LIMANKBS
LAOSKBS
KBS
"""
import re

R=re.compile(r"""
                    &[#]    #start of a numeric 이게뭐지..
                    (
                        0[0-7]+ # octal form
                        |\d+ #Decimal form
                        |x\w+ # Hexadecimal
                    ); # Trailing semicolon
                    """,re.X)


r1=re.compile(r"\w*KBS\Z",re.MULTILINE)
m=r1.findall(text)

print(m)

st="""park 032-98777-9632 
jung 02-988-946"""

gr=re.compile(r"(\w+) ((\d+)[-]\w+)",re.MULTILINE)

com=gr.findall(st)

print(com)