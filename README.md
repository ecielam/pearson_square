Pearson Square
===

My dad is learning python and was going to use a Pearson Square calculator to learn with.

I figured I'd write a quick sample so he can refer to it when he's done with his implementation.

And why not share it with the world?

What's a Pearson Square?
---

A Pearson Square is a simple method to calculate the ratios for animal feed ingredients.

Basically, you have a target nutrient percentage, and two input ingredients.  The Pearson Square tells you
what the ratio should be.

For more info, see http://www.ext.colostate.edu/pubs/livestk/01618.html

Usage
---

Just call it with a --target argument and two --input arguments.  All values are integer percentages of nutrient.

For example

~~~
    pearson.py --target 14 --input 10 --input 45
~~~

Will give you the sample output:

~~~
Processing feed requirements for a target percentage of 14%
Inputs:
  Input 1 is 10 percent protein
  Input 2 is 45 percent protein
   
You should use 4 parts of ingredient 1 (10%) and 31 parts of ingredient 2 (45%)
~~~

Easy, eh?
