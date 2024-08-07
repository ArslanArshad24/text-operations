from stringcolor import *
  
print(cs("away to space!", "red"))   
print(cs("final fantasy", "#ffff87"))  

print(cs("purple number 4, bold", "purple4").bold()) 

print(cs("blue, underlined", "blue").underline())  

print(bold("bold AND underlined!").underline().cs("red", "gold"))

print(underline("the bottom line."))

print(cs("warning!", "yellow", "#ff0000"))