import os
import time
from paths import relativepaths as rl


def timeit(method):
        """The timeit decorator"""
        def running_time(*args, **kwargs):
                start_time = time.time()
                result = method(*args, **kwargs)
                end_time = time.time()
                print('%r %2.2f ms' % (method.__name__, (end_time - start_time) % 1000))
        return running_time


@timeit
def convert_ipynb_html():
        # singleCommand = 'jupyter nbconvert --to html htmlFiles/{0}'
        multiplefileCommand = 'jupyter nbconvert '
        allFiles = ''
        directory=rl['smallFiles'] 

        for root, dirs, files in os.walk(directory):
                for filename in files:
                        allFiles += directory+'/'+filename+' '
        p=multiplefileCommand+allFiles
        os.system(p)

def relocate():
        pass

if __name__ == "__main__":
    convert_ipynb_html()
