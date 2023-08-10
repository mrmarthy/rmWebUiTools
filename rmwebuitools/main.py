# This main function is only used to test scripts in the module.
from rmwebuitools.tree import get_tree
from rmwebuitools.upload import upload_to_rm
def main(): 
    # The reMarkable Tree should be printed
    get_tree()

    # If the "test_folder" folder exists in the reMarkable, the file "test_file.pdf" will be uploaded to it.
    upload_to_rm("test_upload", "data/test_file.pdf")

    

if __name__ == '__main__':
    main()