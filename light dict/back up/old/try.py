

def get_file_above(file_name):
        import os.path
        import sys
        
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "..", file_name))
        f = open(filepath, "r")
        return f

file_name = "Readme.md"

f = get_file_above(file_name)

