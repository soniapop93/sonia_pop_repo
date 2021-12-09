# Implement a context manager called just_some_exceptions that will handle KeyError, IndexError by
# printing a message and let any other exceptions propagate outside of the context manager.
# Implement the context manager by using both approaches: by using class and by using @contextmanager
# Write examples that prove the functionality for all the handled exceptions and for one exception that is not handled.

list_names = ["Sonia", "Lucian", "James", "Sarah"]

class ContextClass:
    def __init__(self, list_names, char_index_to_upper):
        self.dict_names = {}

        count = 0
        for name in list_names:
            self.dict_names[count] = name
            count += 1

    def __enter__(self):
        return self.dict_names

    def __exit__(self, type, value, tracebnack):
        if type is KeyError:
            print("Key does not exist")
            return True

        if type is IndexError:
            print("Character does not exist in dictionary value")
            return True
        

with ContextClass(list_names, 2) as cont_class:
    # print(cont_class[1][222])  # -> uncomment for IndexError
    # print(cont_class[200]) # -> uncoment for KeyError
    print(cont_class) 
    

#-------------------------------------------------

from contextlib import contextmanager

@contextmanager
def just_some_exceptions(list_names):
    count = 0
    dict_names = {}

    for name in list_names:
        dict_names[count] = name
        count += 1
        
    try:
        yield dict_names
    
    except KeyError:
        print("Key does not exist")

    except IndexError:
        print("Character does not exist in dictionary value")

    finally:
        print(f"Your dictionary has {len(dict_names)} elements.")

with just_some_exceptions(list_names) as dict_names:
    # print(dict_names[1][222])  # -> uncomment for IndexError
    # print(dict_names[200]) # -> uncoment for KeyError
    print(dict_names) 