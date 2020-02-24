import re

class Brackets(str):
    def __init__(self):
        print("Brackets class is in module: ", __name__)
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

if __name__ == "__main__":
    ## Block executed only if module is run (not if it is imported)
    b=Brackets()
    print("number to balance: ", b.balance_brackets("()()("))
