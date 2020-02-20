import re

def count_brackets(input_string):
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


#s = '()))))))))))))))))))))))()()))()))))))))()))))))()))()))))(()))))))))))))()))))))(()))))))))()()))))))))))))()))))(())()))))))(()))))()))))))()))()())))())))))))))))()))())(()()())()()())))))()))))())()))()))))))))))))))()())))()))))()))))))()))())()))())))(()))()))))))))())))())))(())()))))()((()))))))((((()())())())(())))))())())))))))())))))()(()))))()))))())))))()())())()))()))))))))()))))))))))()))))())))))(((()))))()))((())))())))))))())))()()())())))))())))())())))))(())())))))))())))()()))))))))))))(())())())))((()))))))(())))()())))()))))(())))(())))))))))))))(())))(())()))))(()))())())))))))()())(()(())())))))))))))))))))))))))((()())))())))())))((()())))()))())()))))())()())))))))))))(()))))))))))))))()))))))()))))))))))))))))(()(()))(()))()))))))()))()()))))))))))()))())()))))())))()()()))()))))(())))))))))))))()()))))(())))()))))))()))()())()))())()())())))()()(()())))))()())))))))())))())))(())))())))))))()))))))))()((()(())))))))))(())))())))())))))))))()())))()))))))))('

#print("brackets to balance: "+str(count_brackets(s)))
#help(count_brackets)

def utest():
    """
    unit test to check:
    edge cases '' ' ' '('
    cheat sheet 0 0 1
    """
    assert count_brackets('') == 0
    assert count_brackets(' ') == 0
    assert count_brackets('(') == 1
    assert count_brackets('())') == 1
    assert count_brackets('())(') == 2

utest()
#help(utest)
