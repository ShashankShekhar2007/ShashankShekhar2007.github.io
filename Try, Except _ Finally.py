# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    FINALLY    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
try:
    open("any.txt")

except Exception as e:
    print(e)
finally:
    print('Run this anyway...')

print("Something Important.")

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    ELSE    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


try:
    open("any_2.txt")
    # Try to rename the file name by an existing text file.
    # Then the statement of the else block will be executed.
except IOError as e:
    print(e)
    # There are many type of errors such as EOFError,IOError,OSError and many more...
    # To know about these errors you have to replace Exception by the following error names.
    # For Example:
    """
    except IOError as e:    
        print(e)
    """
else:
    print('This line will be executed if exception will not occur')

print("Another Important Statement.")