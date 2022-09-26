from datetime import datetime
import pickle
import numpy as np
import os

def datetime_now_str():

    now = datetime.now()
    return now.strftime("%Y_%m_%d_%H_%M_%S")
    
#Checks to see if a directory exists. If it doesn't it creates it. If it does exist, it does nothing.
def makeDirectory(parent_dir, new_dir):

    save_path = os.path.join(parent_dir, new_dir)

    if not os.path.exists(save_path):
        os.mkdir(save_path)

    return save_path

#Save dictionary as folder structure
def save_dict_expansion(cur_path, dict_struct):

    for key in dict_struct:
        save_type(cur_path, key, dict_struct[key])

def load_dict_folder(cur_path):

    dict_struct = {}

    for f in list(os.scandir(cur_path)):
        
        dict_struct[os.path.splitext(f.name)[0]] = load_type(f.path)

    return dict_struct
        
def load_type(f_path):

    if os.path.isdir(f_path):
        return load_dict_folder(f_path)
    
    extension = os.path.splitext(f_path)[1]

    if extension == '.npy':
        return np.load(f_path)

    elif extension == '.pkl': 
        return load_pickle(f_path)
    
def save_type(cur_path, name, structure):

    if type(structure) == dict and 'is_folder' in structure:
                dict_dir = makeDirectory(cur_path, name)
                save_dict_expansion(dict_dir, structure)
    else: 
        save_pickle(cur_path, name, structure)

def save_dataset(dataset):
    if type(dataset) == np.ndarray:
        np.save()

def load_dataset(data_path):

    split_file = os.path.splitext(data_path)

    if split_file[1] == '.npy':
        return np.load(data_path)

    elif split_file[1] == '.pkl':
        return load_pickle(data_path)

    else:
        return None

def load_pickle(file_str):

    #f = open(file_str, encoding="cp856")
    #p_obj = pickle.load(f)
    #return p_obj
    
    with open(file_str, "rb") as input_file:
        structure = pickle.load(input_file)

    return structure

def save_pickle(folder, file_name, structure):

    file_path = os.path.join(folder, file_name + ".pkl")

    with open(file_path, "wb") as f:
        pickle.dump(structure, f)

def load_test_subject_dicts(folder):
    test_dict = {}
    for subfolder in [ f for f in os.scandir(folder) if f.is_dir() ] :
        key_name = os.path.splitext(subfolder.name)[0]
        test_dict[key_name] = load_dict_folder(subfolder.path)
    return test_dict

#Courtesy of poppie at https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory
def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders