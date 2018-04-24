import sys
from ishell import MyPrompt
from quick_sort import QuickSort

prompt_obj = MyPrompt()

# if sys.argv[1] == '-connect' and sys.argv[2]:
#     prompt_obj.do_connectdb(sys.argv[2])

a = len(sys.argv)

for i in range(a):

    if sys.argv[i] == '-connect' and sys.argv[i+1]:
        prompt_obj.do_connectdb(sys.argv[i+1])

    
    elif sys.argv[i] == '-i':
        prompt_obj.do_createuser() 
        prompt_obj.do_insert_data()
    
    elif sys.argv[i] == '-u':
        prompt_obj.do_update_data()
    
    elif sys.argv[i] == '-r':
        prompt_obj.do_retrieve_users()

    elif sys.argv[i] == '-all':
        prompt_obj.do_get_all_users()
    
    try:    
        if sys.argv[i] == '-d' and sys.argv[i+1]:
            prompt_obj.do_delete_users(sys.argv[i+1])
    except:
        if sys.argv[i] == '-d':
            prompt_obj.do_delete_users()
        
    try:    
        if sys.argv[i] == '-search' and sys.argv[i+1]:
            prompt_obj.do_search_user(sys.argv[i+1])
    except:
        if sys.argv[i] == '-search':
            prompt_obj.do_search_user()
    
    try:
        if sys.argv[i] == '-sort' and sys.argv[i+1]:
            prompt_obj.do_sort_user(sys.argv[i+1])
    except:
        if sys.argv[i] == '-sort':
            prompt_obj.do_search_user()
