import os
import time
from paths import relativepaths as rl

def timeit(method):
    """The timeit decorator"""
    def running_time(*args, **kwargs):
        start_time = time.time()
        result = method(*args, **kwargs)
        end_time = time.time()
        print('%r %2.2f ms' % (method.__name__,(end_time - start_time) % 1000))
    return running_time


@timeit
def convert_ipynb_html(dir: str):
    multiplefile_command = 'jupyter nbconvert '
    separator = '/'
    all_files = str()
    directory=rl[dir] 
    space = ' '

    for  _,_,files in os.walk(directory):
        for filename in files:
            if '.ipynb' in filename:
                all_files += directory+separator+filename+space
    final_command=multiplefile_command+all_files
    os.system(final_command)

def relocate(dir: str):
    create_file = 'mkdir static_html'
    static_html_directory = os.getcwd()+'/static_html'
    relocate_command = 'mv {0}/{1} '+static_html_directory

    try:
        os.system(create_file)
    except:
        print('Already Exists')

    for _,_,files in os.walk(rl[dir]):
        for filename in files:
            if '.html' in filename:
                os.system(relocate_command.format(rl[dir], filename))      
    
if __name__ == "__main__":
    directory = 'bigFiles' # <--------------------- 
    convert_ipynb_html(directory)
    relocate(directory)
