class StringUtility:
  
  def __init__(self, string):
    self.string = string
    return

  def __str__(self):
    return self.string

  def vowels(self):
    """
    Uses .count to count the number of vowels. If it is greater than 4, it returns many.
    Takes the object and uses its string
    Returns a string
    """
    return str(self.string.count("a") + self.string.count("e") + self.string.count("i") + self.string.count("o") + self.string.count("u")) if (self.string.count("a") + self.string.count("e") + self.string.count("i") + self.string.count("o") + self.string.count("u")) < 5 else "many"

  def bothEnds(self):
    """
    Takes the string and returns a new string that is made of the first 2 and last 2 characters
    Takes the object and uses its string
    returns a string
    """
    return "" if len(self.string) < 3 else (self.string[0] + self.string[1] + self.string[-2] + self.string[-1])

  def fixStart(self):
    """
    Returns a new string, but stars replace the starting letter, should that letter repeats
    Takes the object and uses its string
    returns a string
    """
    return "" if len(self.string) < 2 else (self.string[0] + self.string[1:].replace(self.string[0], "*"))

  def asciiSum(self):
    """
    Returns the ASCII sum of the string.
    Takes the object and uses its string
    returns an int
    """
    return sum(map(ord, self.string))

  def cipher(self):
    """
    Changes the string based on the string length and character.
    Takes the object and uses its string
    returns a string
    """
    stringLength = len(self.string)
    cipher = ""
    for i in range (stringLength):
      if stringLength > 26:
        movement = stringLength%26
        alphabet = ord(self.string[i])+movement
      else:
        alphabet = ord(self.string[i])+stringLength
      if(self.string[i]==" "):
        alphabet = ord(" ")
      elif(alphabet>ord("z")):
        alphabet+=-26
      elif(alphabet>ord("Z") and alphabet<ord("a")):
        alphabet+=-26
      letter = chr(alphabet)
      cipher+=letter
    return(cipher)

