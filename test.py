import os

# path = "notebooks/research.ipynb"

dir, file = os.path.split("notebooks/research.ipynb")

os.makedirs(dir)
'''
with open(file, "w") as f:
    pass
'''

