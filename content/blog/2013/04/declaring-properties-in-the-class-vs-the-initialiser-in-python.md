Title: Declaring properties in the class vs the initialiser, in Python
Date: 2013-04-10
Category: Blog
Tags: python
Summary: How I learned an important lesson about scoping properties

I've just learned, to the tune of a wasted 50 minutes that properties defined in
a Python class declaration are not treated the same as when they're set in the
initialiser. For example, you can set the same values in both the below cases:

```python
class MyClass:
    foo = 'bar'
```

and

```python
class MyClass:
    def __init__(self):
        self.foo = 'bar'
```

This means that in the first example, the value of foo is effectively shared
between all instances of a class. If you changed that value in one instance, it
would carry over til the next time you instantiated that class. It's basically a
static property, but Python allows you to change it, 'cos Python doesn't judge
(except on whitespace).

The second one works when you need a property to be manageable for each specific
instance of a class, not shared among the instances; the downside is that you
have to create an object from the class in order to access the property, 'cos
it's not static. This was confirmed in a
[StackOverflow answer](http://stackoverflow.com/a/7809443).

I guess there's no problem in doing both if you need it, but I got completely
befuddled because I'd done method A, not B. If'd done B or both I'd have been
fine, but basically I was constantly adding to a list of static properties and
wondering why they were being shared between instances of a class. And now I
know.

I don't feel bad that this isn't something I know, 'cos I'm self-taught in
pretty much everything I do, but when you look at the difference and spend a
little time considering the logic, it's kind of silly to think that this would
be a point of confusion, especially for an OOP fan like me.

But hey, every day's a school day.
