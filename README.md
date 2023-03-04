# Random-Sentence-Generator

A Context Free Language is a language of all the strings that can be generated by a context free grammar.

A Context Free Grammar (CFG) is a set of rules and pathways that a string in the language can follow.

It is made up of two types of variables:
* A non-terminal (usually capital)
* A terminal (usually lowercase)

It looks something like this:

X -> aXb | ɛ

A non-terminal is a symbol that can be expanded by following another rule, such as X. When generating a string in the lanuage, X can be expanded to "aXb" or just ɛ, the empty string (meaning nothing is added to the string)

A terminal is a character of the string that cannot expanded, and the character itself is used in the string.

The language of a CFG is all the strings that can be generated by the CFG, meaning that in the language of the CFG above, the strings ɛ, "ab", "aabb", "aaabbb", and so on, are all in the string.

The language of the string can be described as {a<sup>n</sup>b<sup>n</sup> | where n is a non-negative integer}.

I have created several CFGs, where the terminals are characters, and the non-terminals are variables enclosed by angle brackets.

Here is one:

  <start> -> Every morning at 8:30, I eat <int> bowls of <pluralnoun> with whole milk.

  <int> -> 4 | 5 | 9 | 33

  <pluralnoun> -> nanobots | fried noodles | <adjective> potatoes

  <adjective> -> lumpy | smooth
  

