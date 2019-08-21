def unique(lst: list):
    """Return a list containing only the first occurrence of each distint
       element in list.  That is, all duplicates are omitted.

    Arguments:
        lst: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(["b","a","a","b","b","b","a","a"])
    ['b', 'a']
    >>> unique([])
    []
    >>> unique('p')
    Traceback (most recent call last):
    ...
    TypeError: 'p' is not a list
    """
    if not isinstance(lst, list):
        # If 'lst' is not list, raise TypeError
        raise TypeError(f"'{lst}' is not a list")
    else:
        # Create empty list to contain element
        unique_list = []
        for element in lst:
            if element not in unique_list:
                unique_list.append(element)
        return unique_list


if __name__ == "__main__":
    """ Run the doctests in all methods. """
    import doctest
    doctest.testmod(verbose=True)
