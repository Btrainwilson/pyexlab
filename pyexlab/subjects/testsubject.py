from datetime import datetime
from .. import fileio as fio


class TestSubject():
    """
    A class for handling a test subject. 
    The test subject is dependent on some parameters and its output is recorded

    ...

    Attributes
    ----------
    name : str
        name of the test subject

    Methods
    -------
    measure(**kwargs)
        Outputs a measurement dependent on **kwargs
    final_measure(epochs=100)
        Final measurement on the system. If final state has unique behavior, need to let test_subject know that final measurement is occuring.
    record(save_folder, test_id)
        Saves information dictionary to save_folder\test_id
    load(load_folder)
        Loads the information dictionary from load_folder
    """
    __name__ = "TestSubject"

    def __init__(self, name = None):

        self.test_dict = {}
        self.test_dict['Measurements'] = {}
        self.test_dict['Info'] = {}
        
        #Record starttime of test
        self.test_dict['Info']['Absolute Datetime Start'] = fio.datetime_now_str()

        if name is None or type(name) != str:
            self.test_dict['Info']['Name'] = self.__name__
        else:
            self.test_dict['Info']['Name'] = name
            self.__name__ = name
        pass

    def measure(self, **kwargs):
        #Measure state at current epoch
        pass

    def final_measure(self, **kwargs):
        #Final measurement
        self.test_dict['Info']['Absolute Datetime Finish'] = fio.datetime_now_str()

    def record(self, save_folder, test_id):

        test_name = "%s_%d" % (self.__name__, test_id)

        self.test_dict['Info']['Test ID'] = test_name

        test_folder = fio.makeDirectory(save_folder, test_name)

        fio.save_dict_expansion(test_folder, self.test_dict)

    def load(self, load_folder):
        self.test_dict = fio.load_dict_folder(load_folder)

        
        