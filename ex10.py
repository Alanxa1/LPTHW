a = "I am 6'2\" tall." #escape double-quote inside string
b = 'I am 6\'2" tall.' #escape single-quote inside string.

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

c = "\a BEL"
d = "\b backspace"
e = "\f formfeed"
f = "\LATIN SMALL LETTER C"
g = "\r Carriage return"
h = "\u1234"
i = "\u1234567"
j = "\v Vertical Tab \v Vert"
k = "\123 Octal Value?!"
l = "\x16 Hex value"

print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)

