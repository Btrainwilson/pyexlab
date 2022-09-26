from ..fileio import makeDirectory, save_pickle

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

    def __init__(self, save_folder, test_subjects, print_report = True):

        self.save_folder = save_folder 
        self.test_subjects = test_subjects
        self.print_report = print_report

    def record(self):

        for test_id, test_subject in enumerate(self.test_subjects):
            test_subject.record(self.save_folder, test_id)
            

    def run(self, epochs=100):

        for epoch in range(epochs):

            if self.print_report : print("Experiment Epoch %d" %(epoch))

            for test_subject in self.test_subjects:
                output = test_subject.measure(epoch = epoch)

                if not output is None and self.print_report:
                    print(output)

            self.record()
        
        #Final Measurements
        for test_subject in self.test_subjects:
            test_subject.final_measure()

        #One last record
        self.record()