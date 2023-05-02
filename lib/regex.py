import re

my_pattern = r"\w*'*\w[\w' ]*today'*[\w, ]*[?\.]+"

my_regex = re.compile(my_pattern)


