
"""
Returns the iterable 'iter' with the value 'val'
added to its front and back.

i.e., surround(['a', 'b'], 'c') will return ['c', 'a', 'b', 'c']
"""
def surround(iter, val):
	iter.append(val)
	iter.insert(0, val)
	return iter	

"""
Returns a list of items from the dictionary 'dicti' 
where the key is equal to the value.

i.e. same_key_vals({"a": 1, "b" : "b", "c": 2, "d": "d"})
will return ['b', 'd']
"""
def same_key_vals(dicti):
	l = list()
	for key, value in dicti.items():
		if key == value:
		   l.append(key) 
	return l


"""
If the key 'gene' is present in the dictionary 'dicti'
remove it from the dictionary,
otherwise add the key/value pair 'gene': 'cool' 
to the dictionary. Either way, return the new dictionary

i.e. add_gene_key({'a': 1}) will return {'a': 1, 'gene': 'cool'}
and add_gene_key({'gene': 'butt', 'b': False}) will return {'b': False}.
"""
def add_gene_key(dicti):
    if 'gene' in dicti:
    	del dicti['gene'] 
    else:
    	dicti['gene'] = 'cool' 
	print(dicti)
    return dicti


"""
Return the first and last item of the iterable passed.

i.e., first_and_last([1, 2, 3, 4, 5]) will return [1, 5]
"""
def first_and_last(iterable):
    return iterable[0], iterable[-1] 


"""
Return True if the integer is odd, False if the  integer is even.
0 is considered "odd".

i.e. is_odd(1) is True
is_odd(-2) is False
is_odd(0) is True
"""
def is_odd(integer):
    if integer == 0:
    	return True 
    elif integer % 2 == 0:
    	return False
    else:
    	return True 