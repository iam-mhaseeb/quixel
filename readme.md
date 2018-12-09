# quixel

quixel is light weight open source project for text content analysis semantically.

## Installation

Installation is simple:

1. Download repository
2. Install dependencies with `pip install -r requirements.txt`
3. You are ready to go

## Usage

Check out [A simple usage example](Example/main.py) for a short intro. A sample usage is:

```python
# Import Quixel 

q = Quixel()
q.analyze('your text to analyze')
```

From [example](Example/main.py):
```python
from quixel.quixel import Quixel

q = Quixel()
q.analyze("Jon Skeet is a Java developer working for Google in London. He is a C# author and community leader,"
          "spending far too much time on the Stack Overflow developer Q&A site.")  # That's it!

```
    
## Contributing

Feel free to submit pull requests to me.

## Authors

* **Muhammad Haseeb** - *Initial work* - [Muhammad Haseeb](https://github.com/iam-mhaseeb)

## Licensing
The Quixell project is [MIT Licenced](LICENSE). Feel free to use commercially or personally.
