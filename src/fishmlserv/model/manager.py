import os

def get_model_path():
    #file_path = '/home/hahahellooo/code/fishmlserv/src/fishmlserv/model/'
    file_name = 'model.pkl'
    #model_path = os.path.join(file_path, file_name)
    #return model_path
    my_path = __file__
    # '/home/hahahellooo/code/fishmlserv/src/fishmlserv/model/manager.py'
    dir_name = os.path.dirname(my_path)
    # '/home/hahahellooo/code/fishmlserv/src/fishmlserv/model/'
    model_path = os.path.join(dir_name, file_name)
    return model_path
    

