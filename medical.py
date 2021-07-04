import csv

class MedDataSet:
    def __init__(self, fileCSV, getstats = True):
        # read the csv file and put the values in a dictionary
        self.data = {"Error" : [],
                     "Age" : [],
                     "Sex" : [],
                     "BMI" : [],
                     "NChild" : [],
                     "Smoker" : [],
                     "Region" : [],
                     "IC" : []}
        if fileCSV.endswith('.csv'):
            with open(fileCSV) as CSV:
                for row in csv.DictReader(CSV):
                    self.data["Age"].append(int(row["age"],0))
                    self.data["Sex"].append(row["sex"])
                    self.data["BMI"].append(row["bmi"])
                    self.data["NChild"].append(row["children"])
                    self.data["Smoker"].append(row["smoker"])
                    self.data["Region"].append(row["region"])
                    self.data["IC"].append(float(row["charges"]))
            # Compute basic stats about the data
            if getstats:
                self.basicstats()
            return
        # if the string variable doesn't refer to a CSV file we save a trace of the problem
        print("WARNING: Data cannot be loaded because the file is the wrong type !")
        data["Error"].append("Bad file extension")
        return

    def __repr__(self):
        # Compute basic stats about the data that we need for the representation
        self.basicstats(False)
        # return a string with some data but not all for better readability
        return """
        This dataset contains the following informations:
        - Age               : {A0} ... {A1} with an average of {A2}.
        - Sex               : {S0} ... {S1} with {S2} male and {S3} female.
        - BMI               : {B0} ... {B1}
        - Number of children: {C0} ... {C1}
        - Smoker            : {S4} ... {S5}
        - Insurance Cost    : {C2} ... {C3}
                              with an average of {C4}
        - Region            : {R0} ... {R1}
                              The list of unique region is:
                              {R2}

        """.format(
        A0 = ", ".join(map(str, self.data["Age"][:3])), A1 = ", ".join(map(str, self.data["Age"][-3:])), A2 = round(self.meanAge),
        S0 = ", ".join(self.data["Sex"][:3]), S1 = ", ".join(self.data["Sex"][-3:]), S2 = self.numMale, S3 = self.numFemale,
        B0 = ", ".join(self.data["BMI"][:3]), B1 = ", ".join(self.data["BMI"][-3:]),
        C0 = ", ".join(self.data["NChild"][:3]), C1 = ", ".join(self.data["NChild"][-3:]),
        S4 = ", ".join(self.data["Smoker"][:3]), S5 = ", ".join(self.data["Smoker"][-3:]),
        C2 = ", ".join(map(str, self.data["IC"][:3])), C3 = ", ".join(map(str, self.data["IC"][-3:])),
        C4 = self.meanIC,
        R0 = ", ".join(self.data["Region"][:3]), R1 = ", ".join(self.data["Region"][-3:]),
        R2 = ", ".join(self.unique)
        )

    @staticmethod
    def mean(lst):
        # return the mean value of a list
        return sum(lst)/len(lst)

    @staticmethod
    def unique(lst):
        # return the list of all unique element in a given list
        uni = []
        for element in lst:
            if element in uni:
                continue
            uni.append(element)
        return uni

    def basicstats(self,Print = True):
        # return the mean age, the number of male and female, the mean insurance cost and the list of all unique region of the dataset.
        self.meanAge = self.mean(self.data["Age"])
        self.numMale = len([male for male in self.data["Sex"] if male == "male"])
        self.numFemale = len(self.data["Sex"])-self.numMale
        self.meanIC = self.mean(self.data["IC"])
        self.unique = self.unique(self.data["Region"])
        if Print:
            self.printer()
        return self.meanAge, self.numMale, self.numFemale, self.meanIC, self.unique

    def printer(self):
        # print the stats
        print("""
        The average client is {A} years old.
        The number of male and female in the dataset are respectivly: {M} and {F}.
        The average insurance cost is: {I}$.
        """.format(A = round(self.meanAge), M = self.numMale, F = self.numFemale, I = self.meanIC))

    def getdata(self):
        # return the dataset
        return self.data


if __name__ == "__main__":
    Data = MedDataSet("insurance.csv", False)
    print(Data)
