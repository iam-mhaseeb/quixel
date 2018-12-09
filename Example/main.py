import sys
sys.path.append('../')

from quixel.quixel import Quixel

q = Quixel()
q.analyze("Jon Skeet is a Java developer working for Google in London. He is a C# author and community leader,"
          "spending far too much time on the Stack Overflow developer Q&A site.")  # That's it!
