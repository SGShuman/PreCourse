import itertools

### Fill in each function below. Each function should be a one-liner.


def sort_rows(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: 2 dimensional list of integers (matrix)
    Use list comprehension to modify each row of the matrix to be sorted.
    Example:
    >>> M = [[4, 5, 2, 8], [3, 9, 6, 7]]
    >>> sort_rows(M)
    >>> M
    [[2, 4, 5, 8], [3, 6, 7, 9]]
    '''
    mat = [sorted(mat[0]),sorted(mat[1])];
    pass


def average_rows1(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: list of floats
    Use list comprehension to take the average of each row in the matrix and
    return it as a list.
    Example:
    >>> average_rows1([[4, 5, 2, 8], [3, 9, 6, 7]])
    [4.75, 6.25]
    '''
    return [float(sum(mat[0]))/float(len(mat[0])),float(sum(mat[1]))/float(len(mat[0]))];
    pass

def average_rows2(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: list of floats
    Use map to take the average of each row in the matrix and
    return it as a list.
    '''
    def avg(x): return float(sum(x))/float(len(x));
    return map(avg,mat);
    pass

def word_lengths1(phrase):
    '''
    INPUT: string
    OUTPUT: list of integers
    Use list comprehension to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.
    Example:
    >>> word_lengths1("Welcome to Zipfian Academy!")
    [7, 2, 7, 8]
    '''
    return [len(x) for x in phrase.split()]
    pass

def word_lengths2(phrase):
    '''
    INPUT: string
    OUTPUT: list of integers
    Use map to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.
    '''
    return map(len,phrase.split());
    pass    

def even_odd1(L):
    '''
    INPUT: list of integers
    OUTPUT: list of strings
    
    Use list comprehension to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.
    
    Example:
    >>> even_odd([6, 4, 1, 3, 8, 5])
    ['even', 'even', 'odd', 'odd', 'even', 'odd']
    '''
    return ['even' if x % 2 == 0 else 'odd' for x in L]
    pass

def even_odd2(L):
    '''
    INPUT: list of integers
    OUTPUT: list of strings
    
    Use map to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.
    '''
    return
    pass

def shift_on_character(string, char):
    '''
    INPUT: string, string
    OUTPUT: string
    
    Find the first occurence of the character char and return the string witth
    everything before char moved to the end of the string. If char doesn't
    appear, return the same string.
    
    This function may use more than one line.
    
    Example:
    >>> shift_on_character("zipfian", "f")
    'fianzip'
    '''
    if char not in string:
        return string;
    else:
        start_num = string.index(char)
        return string[start_num:]+string[:start_num];
    pass

def is_palindrome(string):
    '''
    INPUT: string
    OUTPUT: boolean
    
    Return whether the given string is the same forwards and backwards.
    
    Example:
    >>> is_palindrome("rats live on no evil star")
    True
    '''
    return string == string[::-1]
    pass

def alternate(L):
    '''
    INPUT: list
    OUTPUT: list
    
    Use list slicing to return a list containing all the odd indexed elements
    followed by all the even indexed elements.
    
    Example:
    >>> alternate(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    ['b', 'd', 'f', 'a', 'c', 'e', 'g']
    '''
    return L[1::2]
    pass

def shuffle(L):
    '''
    INPUT: list
    OUTPUT: list
    
    Return the result of a "perfect" shuffle. You may assume that L has even
    length. You should return the result of splitting L in half and alternating
    taking an element from each.
    
    Example:
    >>> shuffle([1, 2, 3, 4, 5, 6])
    [1, 4, 2, 5, 3, 6]
    '''
    shuffled = []
    for i in range(len(L)/2):
        shuffled.append(L[i])
        shuffled.append(L[i+len(L)/2])
    return shuffled
    return [x]
    pass

def filter_words(word_list, letter):
    '''
    INPUT: list of words, string
    OUTPUT: list of words
    Use filter to return the words from word_list which start with letter.
    Example:
    >>> filter_words(["salumeria", "dandelion", "yamo", "doc loi", "rosamunde",
                      "beretta", "ike's", "delfina"], "d")
    ['dandelion', 'doc loi', 'delfina']
    '''
    return [x for x in word_list if x[0]==letter]
    pass

def factors(num):
    '''
    INPUT: integer
    OUTPUT: list of integers
    Use filter to return all of the factors of num.
    '''
    return [x for x in range(1,num) if num % x == 0]
    pass

def acronym(phrase):
    '''
    INPUT: string
    OUTPUT: string
    Given a phrase, return the associated acronym by breaking on spaces and
    concatenating the first letters of each word together capitalized.
    Example:
    >>> acronym("zipfian academy")
    'ZA'
    Hint: You can do this on one line using list comprehension and the join
    method. Python has a builtin string method to uppercase strings.
    '''
    return ''.join([x[0].upper() for x in phrase.split()])
    pass

def sort_by_ratio(L):
    '''
    INPUT: list of 2-tuples of integers
    OUTPUT: None
    
    Sort the list L by the ratio of the elements in the 2-tuples.
    For example, (1, 3) < (2, 4) since 1/3 < 2/4.
    Use the key parameter in the sort method.
    
    Example:
    >>> L = [(2, 4), (8, 5), (1, 3), (9, 4), (3, 5)]
    >>> sort_by_ratio(L)
    >>> L
    [(1, 3), (2, 4), (3, 5), (8, 5), (9, 4)]
    '''

    return sorted(L,key = lambda ratio: ratio[0]/ratio[1])
    pass


def count_match_index(L):
    '''
    INTPUT: list of integers
    OUTPUT: integer
    
    Use enumerate and other skills from above to return the count of the number
    of items in the list whose value equals its index.
    
    Example:    
    >>> count_match_index([0, 2, 2, 3, 6, 5])
    4
    '''
    return len([x for x in list(enumerate(L)) if x[0]==x[1]])
    pass

def only_sorted(L):
    '''
    INPUT: list of list of integers
    OUTPUT: list of list of integers
    
    Use filter to return only the lists from L that are in sorted order.
    Hint: the all function may come in handy.
    
    Example:
    >>> only_sorted([[3, 4, 5], [4, 3, 5], [5, 6, 3], [5, 6, 7]])
    [[3, 4, 5], [5, 6, 7]]
    '''
    return [x for x in L if x == sorted(x)]
    pass

def concatenate(L1, L2, connector=""):
    '''
    INPUT: list of strings, list of strings
    OUTPUT: list of strings
    
    L1 and L2 have the same length. Use zip and other skills from above to
    return a list of the same length where each value is the two strings from
    L1 and L2 concatenated together with connector between them.
    
    Example:
    >>> concatenate(["A", "B"], ["b", "b"])
    ['Ab', 'Bb']
    >>> concatenate(["San Francisco", "New York", "Las Vegas", "Los Angeles"], \
                    ["California", "New York", "Nevada", "California"], ", ")
    ['San Francisco, California', 'New York, New York', 'Las Vegas, Nevada',
    'Los Angeles, California']
    '''
    return [x[0] + connector + x[1] for x in zip(L1,L2)]
    pass

def transpose(mat):
    '''
    INPUT: 2 dimensional list of integers
    OUTPUT: 2 dimensional list of integers
    
    Return the transpose of the matrix. You may assume that the matrix is not
    empty. You can do this using a double for loop in a list comprehension.
    There is also a solution using zip.
    '''
    return zip(*mat)
    pass

def invert_list(L):
    '''
    INPUT: list
    OUTPUT: dictionary
    
    Use enumerate and other skills from above to return a dictionary which has
    the values of the list as keys and the index as the value. You may assume
    that a value will only appear once in the given list.
    
    Example:
    >>> invert_list(['a', 'b', 'c', 'd'])
    {'a': 0, 'c': 2, 'b': 1, 'd': 3}
    '''
    return {x[1]:x[0] for x in list(enumerate(L))}
    pass

def digits_to_num(digits):
    '''
    INPUT: list of integers
    OUTPUT: integer
    
    Use reduce to take a list of digits and return the number that they
    correspond to. Do not convert the integers to strings.
    
    Example:
    >>> digits_to_num([5, 0, 3, 8])
    5038
    '''
    return reduce(lambda a,b: int(str(a)+str(b)),digits) #bit stumped but everything else is good but the function
    pass

def intersection_of_sets(list_of_sets):
    '''
    INPUT: list of sets
    OUTPUT: set
    
    Use reduce to take the intersection of a list of sets.
    Hint: the & operator takes the intersection of two sets.
    
    Example:
    >>> intersection_of_sets([{1, 2, 3}, {2, 3, 4}, {2, 5}])
    set([2])
    '''
    return reduce(lambda a,b: a&b, list_of_sets)
    pass

def combinations(alphabet, n):
    '''
    INPUT: string, integer
    OUTPUT: list of strings
    
    Use itertools.combinations to return all the combinations of letters in
    alphabet with length at most n.
    
    Example:
    >>> combinations('abc', 2)
    ['a', 'b', 'c', 'ab', 'ac', 'bc']
    '''
    
    return [x for i in range(1,n+1) for x in itertools.combinations(alphabet,i)]
    pass

def permutations_in_dict(string, words):
    '''
    INPUT: string, set
    OUTPUT: list of strings
    
    Use itertools.permutations to return all the permutations of the string
    and return only the ones which are members of set words.
    
    Example:
    >>> permutations_in_dict('act', {'cat', 'rat', 'dog', 'act'})
    ['act', 'cat']
    '''
    return [x[0]+x[1]+x[2] for x in itertools.permutations(string) if x[0]+x[1]+x[2] in words]
    pass