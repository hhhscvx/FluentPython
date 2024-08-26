
my_dict = {}
key = ['asdf']


my_dict.setdefault(key, []).append('new')
"""То же самое, что и (только в 3 раза эффективнее)
if key not in my_dict:
    my_dict[key] = []
my_dict[key].append('new')
"""
