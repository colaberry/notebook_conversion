import os
from paths import relativepaths as rl

def main():        
        # singleCommand = 'jupyter nbconvert --to html htmlFiles/{0}'
        multiplefileCommand = 'jupyter nbconvert '
        allFiles = ''
        directory=rl['bigFiles'] 

        for root, dirs, files in os.walk(directory):
                for filename in files:
                        allFiles += directory+'/'+filename+' '
                
        p=multiplefileCommand+allFiles
        os.system(p)

def relocate():
        pass

if __name__ == "__main__":
    main()
