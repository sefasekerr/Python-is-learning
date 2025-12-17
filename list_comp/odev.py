def read_file(file_name):
    with open(file_name,"r") as file:
        file_contents=file.read()
    return file_contents
           
    """ Reads and returns the entire contents of a file as a single string.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function.
        2. Print the contents of the file.
        3. Return the contents of the file.

    Args:
        file_name (str): Name of the file to be read.

    Returns:
        str: Entire contents of the file.
    """
    ### WRITE SOLUTION HERE
    

def read_file_into_list(file_name):
    with open(file_name,"r") as file:
        liste = file.readlines()
    return liste



def write_first_line_to_file(file_contents, output_filename):

    ilksatir = file_contents.split("\n")[0]

    with open(output_filename,"w") as file:
        file.write(str(ilksatir))
        



def read_even_numbered_lines(file_name):
    with open(file_name,"r") as file:
        liste = file.readlines()
    sira =[line for idx,line in enumerate(liste,start=1)  if (idx%2==0)]
    return sira

    


def read_file_in_reverse(file_name):
    with open(file_name,"r") as f:
        sira = f.readlines()
    reverse_sira = list(reversed(sira))
    return reverse_sira


def main():
    file_contents = read_file("sampletext.txt")
    print("File Contents:\n", file_contents)
    
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "output.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()
