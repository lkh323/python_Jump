"I eat %s apples so I was sick %d days" % ("five" , 3)

"Error is %d%%" % 98

"%10s" % "hi"
"%-10s Jane" % "hi"
'hi        jane.'

"%10.4f" % 3.42134234

"I eat {} apples".format("five")
"I eat {} apples. I was sick {} days".format("five", "three")
"I eat {1} apples. I was sick {0} days".format("five", "three")
"I eat {apple} apples. I was sick {day} days".format( apple = "five", day = "three")

"{0:>10}".format("hi")
"{0:<10}".format("hi")
"{0:^10}".format("hi")

"{0:=>10}".format("hi")
"{0:=<10}".format("hi")
"{0:=^10}".format("hi")

f'{"hi":>10}'
f'{"hi":<10}'
f'{"hi":^10}'

f'{"hi":=>10}'
f'{"hi":=<10}'
f'{"hi":=^10}'

".".join("abcd")

y = 3.42134234
"{0:0.4f}".format(y)

" %10f" % 3.42134234
" %10.4f" % 3.42134234

f"{3.42134234:10.4f}"









 a = ['a', 'c', 'b']
 a.reverse()
 print(a)

a = ['a', 'c', 'b']
a.sort(reverse=True)
a.sort()
print(a)

print("phthon"[::-1])

a = list("12345")
a.reverse()
print(str(a))
