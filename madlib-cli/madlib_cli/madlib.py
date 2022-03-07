#import modules
import re

 

def read_template(path):
    """
    1- a read_template function: takes in 
    a path to text file and returns 
    a stripped string of the file’s contents.
    2- read_template should raise a FileNotFoundError if path is invalid.
     
    """
    try : 
       with open(path) as file :
         file_string=file.read()  
         stripped_file_strings=file_string.strip()
         return stripped_file_strings

        
    except FileNotFoundError:
        print("Error:Sorry the file does not exist")
  

def parse_template(template_string):
    """
    parse_template function : takes 
    in a template string and returns
     a string with language parts removed
      and a separate list of those language parts.
    """
    required_text_parts= re.findall(r"\{(.*?)\}", template_string )
    string_two_parts=re.sub(r"\{(.*?)\}","{}",template_string)
    return[string_two_parts,required_text_parts]



def merge(bare_template,user_words):
    """
    a merge function :  takes in a “bare” template 
    and a list of user entered language parts, 
    and returns a string with the language parts inserted into the template.
    """
    output_string=bare_template
    word_to_find_and_replace= '{}'
    for word_to_find_and_replace_it_with in user_words:
        out_string=output_string.replace(word_to_find_and_replace,word_to_find_and_replace_it_with, 1)

    return output_string 

def write_story_to_the_file(story):
    with open('assets/spam.txt','w') as new_file:
        new_file.write(story)

if __name__=="__main__":

    #the path 
    path='assets/dark_and_stormy_night_template.txt'

    #show the welcome message for users##
    print( """************** Welcome to the MADLIBS game \n
    please enter  a word of each type of the words that will requested from you \n 
    to reveal your fun story 
   

    """ )

    #open and read (dark_and_stormy_night_template.txt )file 
    file=read_template(path)
    #parse it 
    use_template=parse_template(file)
    #promot the user for the words 
    user_input_words=[]
    for words in use_template[1]:
        user_input_words.append(input(f'please enter a {words}. > '))

    print("wait your story")

    story=merge(use_template[0],user_input_words)

    write_story_to_the_file(story)
    print (story)