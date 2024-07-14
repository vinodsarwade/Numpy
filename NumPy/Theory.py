#why numpy
'''In Python we have lists that serve the purpose of arrays, but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.'''

#why numpy is faster than list
'''NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
This behavior is called locality of reference in computer science.
This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.'''

#
'''An array is defined as a collection of items that are stored at contiguous memory locations.
array items are of same data type ex: arr = [1 2 3 4 ] all elements are int only.'''