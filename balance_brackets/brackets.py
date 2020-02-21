import re

class Brackets:

    def balance_brackets(self, input_string):
      """
      input: string
      output: int
      description: Given a string containing a number of open and close parentheses, find the count needed to balance them
      """
      new_string = input_string
      while True: # get all matches of '()' and replace with ''
          new_string = re.subn(pattern = "\(\)", repl = "", string=new_string)[0]
          if re.subn(pattern = "\(\)", repl = "", string=new_string)[1] == 0:
              break
      scount = len([i for i in new_string if i=='(']) # count remaining brackets
      ecount = len([i for i in new_string if i==')'])
      return(ecount+scount)
