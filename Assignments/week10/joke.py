import pyjokes
import cowsay
import helper

helper.greet("Cow")
joke = pyjokes.get_joke()
cowsay.cow(joke)



