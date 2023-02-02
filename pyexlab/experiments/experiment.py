from ..fileio import makeDirectory, save_pickle, datetime_now_str

class Experiment():
    """
    A class for running Experiments. 
    The experiment design pattern is based on how lab experiments are performed.
    We have a set of independent test subjects and we record their change over time.


    ...

    Attributes
    ----------
    save_folder : str
        a valid path to a folder for saving the experiment data
    test_subjects : list(TestSubject)
        list of TestSubject objects
    print_report : Boolean
        determines if test output is printed to the terminal

    Methods
    -------
    record()
        Records information from each test subject in test_subjects
    run(epochs=100)
        Runs 100 epochs for each test subject and records the output to the save_folder
    """

    def __init__(self, save_folder, test_subjects, id="Experiment", print_report = True, pkl_copy = True):

        folder_name = id + datetime_now_str()
        self.save_folder = makeDirectory(save_folder, folder_name)

        self.test_subjects = test_subjects
        self.print_report = print_report
        self.pkl_copy = pkl_copy

        self.experiment_info = {}
        self.analysis_info = {}

    def record(self):

        for test_idx, test_subject in enumerate(self.test_subjects):

            #Pass up any information that needs to be recorded.
            self.experiment_info[test_subject.id(test_idx)] = test_subject.record(self.save_folder, test_idx)
        

    def run(self, epochs=100):

        for epoch in range(epochs):

            if self.print_report : print("Experiment Epoch %d" %(epoch))

            for test_idx, test_subject in enumerate(self.test_subjects):

                try:
                    output = test_subject.measure(epoch = epoch)
                except:
                    print("Exception occurred during measurement of %s" %(test_subject.id(test_idx)))
                    self.record()
                    raise

                if not output is None and self.print_report:
                    print(output)

            
        #Final Measurements
        for test_idx, test_subject in enumerate(self.test_subjects):
            try:
                test_subject.final_measure(epoch = epoch)
            except:
                print("Exception occurred during final measurement of %s" %(test_subject.id(test_idx)))
                self.record()
                raise

        #One last record
        self.record()
        
        if self.pkl_copy:
            save_pickle(self.save_folder, "exp", self)

    def analysis(self):

        for test_idx, test_subject in enumerate(self.test_subjects):

            #Pass up any information that needs to be recorded.
            self.analysis_info[test_subject.id(test_idx)] = test_subject.analysis()
        
        return self.analysis_info

    def graph(self):
        for test_idx, test_subject in enumerate(self.test_subjects):

            #Pass up any information that needs to be recorded.
            self.analysis_info[test_subject.id(test_idx)] = test_subject.graph()
        
        return self.analysis_info
