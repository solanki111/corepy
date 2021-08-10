# Creating the context manager using a class
class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# with Open_File('sample.txt', 'w') as f:
#     f.write('testing...')
# print(f.closed)
# Creating the context manager using a function


from contextlib import contextmanager
import os


@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file('sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(f.closed)


cwd = os.getcwd()
os.chdir('Sample_dir')
print(os.listdir())
os.chdir(cwd)

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('Sample'):
    print(os.listdir())


# Iterators and Iterable:

nums = [1, 2, 3, 4, 5]
i_nums = iter(nums)

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

