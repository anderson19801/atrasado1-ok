"""
KATA = forma
1- se a posição for multipla de 3: fizz
2- se a "        "     "      "  5: buzz
3- "  "   "       "     "     "  3 e 5: fizzbuzz
4- para qualqquer outra posição fale o proprio nº
"""

#robot = None   TypeError: 'NoneType' object is not callable

#def robot():    TypeError: robot() takes no arguments (1 given)
#    pass

#def robot(pos):  AssertionError  '''todo erro diferente de assert error é chamado de erro no test, quando temos um assertionError nos temos uma falha no teste'''
#    pass

#import partial
from functools import partial
#import unittest


multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)

'''
def multilpe_of(base, num):
    return num % base == 0


def multiple_of_5(num):
    return multiple_of(5, num)
    #return num % 5 == 0
'''

def multiple_of_3(num):
    return multiple_of(3, num)
    #return num % 3 == 0


def robot(pos):
    say = str(pos)

    if multiple_of_3(pos) and multiple_of_5(pos):
    #if pos % 15 == 0:
        say = 'fizzbuzz'
        #return 'fizzbuzz'
    #if pos % 15 == 0:
     #   return 'fizzbuzz'

    elif multiple_of_5(pos):
    #elif pos % 5  == 0:
    #if pos % 5 == 0:
        say = 'buzz'
        #return 'buzz'
    #if pos - pos//5 * 5 == 0:
     #   return 'buzz'
    #if pos in (20, 10, 5):
     #   return 'buzz'
    #if pos == 20 or pos == 10 or pos == 5:
     #   return 'buzz'
    #if pos == 10:
     #   return 'buzz'
    #if pos == 5:
     #   return 'buzz'
    elif multiple_of_3(pos):
        say = 'fizz'
    #elif pos % 3 == 0:
    #if pos % 3 == 0:
        say = 'fizz'
        #return 'fizz'
    #if pos - pos//3 * 3 == 0:
     #   return 'fizz'
    #if pos in(9, 6, 3):
    #if pos == 9 or pos == 6 or pos == 3:
     #   return 'fizz'
    #if pos == 6:
     #   return 'fizz'
    #if pos == 3:
     #   return 'fizz'
    return say
    #return str(pos)



"""
if __name__ == '__main__':
    unittest.main()



    if pos == 4:
        #return '4'
        #return str(4)
        return str(pos)
    if pos == 2:
        #return '2'
        #return str(2)
        return str(pos)
    #return '1'
    #return str(1)
    return str(pos)
    '''

"""
def assert_equal(result, expected):
    from sys import _getframe

    msg = 'Fail: Line {} got {} expecting{}'

    if not result == expected:
        current = _getframe()
        caller = current.f_back
        line_no = caller.f_lineno
        print(msg.format(line_no, result, expected))
        #print(msg.format(line, result, expected))
    #try:
     #   assert first == second
    #except AssertionError:
     #   print(msg.format(line, first, second))
        #print(expr)

"""
if __name__ == '__main__':
    assert_equal(robot(1),  '1')
    assert_equal(robot(2),  "2")
    assert_equal(robot(4),  '4')


    #try:
     #   assert robot(3) == 'fizz'
    #except AssertionError:
     #   print('falha na linha 102')

    assert_equal(robot(3) ,  'fizz')
    assert_equal(robot(6) ,  'fizz')
    assert_equal(robot(9) ,  'fizz')

    assert_equal (robot(5) , 'buzz')
    assert_equal (robot(10),  'buzz')
    assert_equal (robot(20),  'buzz')

    assert_equal(robot(15) ,  'fizzbuzz')
    assert_equal(robot(30) ,  'fizzbuzz')
    assert_equal(robot(45) ,  'fizzbuzz')

"""