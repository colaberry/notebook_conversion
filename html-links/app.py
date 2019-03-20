import os

def main():        
        # singleCommand = 'jupyter nbconvert --to html htmlFiles/{0}'
        multiplefileCommand = 'jupyter nbconvert '
        allFiles = ''
        directory='notebooks' ## Use '.' if the files are in the same directory 
        # directory='allFiles'

        for root, dirs, files in os.walk(directory):
                for filename in files:
                        allFiles += directory+'/'+filename+' '
                
        p=multiplefileCommand+allFiles
        os.system(p)

if __name__ == "__main__":
    main()
