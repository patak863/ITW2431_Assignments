# Name: Mike Patak
# ITW 2431
# Lab 10 Prob. 3
# File name: ITW2431_L10_P3_mpatak.py
# MODIFIED: 3/24/22
# PURPOSE:  Create a class named "GOT_cast". The class will have two
#           methods, one for calculating a cast members BMI and a second
#           for determining the cast members BMI category. The program
#           will output the cast members name, height, weight, BMI, and
#           BMI category.
# ASSUMPTIONS:
###########################################################################

# define the class GOT_cast
class GOT_cast:
    # class constructor
    def __init__(self, name, height, weight):
        # initialize instance variable
        self.name = name
        self.height = height
        self.weight = weight
        self.BMI = 0
        self.BMI_category = ""

    # class method to calculate BMI
    def calc_bmi(self):
        # calculate the BMI
        self.BMI = (self.weight / (self.height * self.height)) * 703
        # format the float to always show to significant digits
        format_BMI = "{:.2f}".format(self.BMI)
        # return the value of the BMI
        return format_BMI


    # class method to BMI category
    def bmi_category(self):
        # determine BMI category
        if self.BMI < 18.5:
            self.BMI_category = "underweight"
        elif self.BMI >= 18.5 and self.BMI < 25:
            self.BMI_category = "normal weight"
        elif self.BMI >= 25 and self.BMI < 30:
            self.BMI_category = "overweight"
        elif self.BMI >= 30:
            self.BMI_category = "obese"
        # return the value of the BMI category
        return self.BMI_category


# create a GOT_cast object for Jon Snow, Sawell Tarly, and Tyrion Lannister
js = GOT_cast("Jon Snow", 68, 170)
st = GOT_cast("Samwell Tarly", 68, 238)
tl = GOT_cast("Tyrion Lannister", 53, 110)
# print the BMI data output for Jon Snow
print("The BMI for \"" + str(js.name) + " with height " + str(js.height) +
      " and weight " + str(js.weight) + " lbs is: " + str(js.calc_bmi()) +
      "\nThe category is " + str(js.bmi_category()))
# print the BMI data output for Sawell Tarly
print("The BMI for \"" + str(st.name) + " with height " + str(st.height) +
      " and weight " + str(st.weight) + " lbs is: " + str(st.calc_bmi()) +
      "\nThe category is " + str(st.bmi_category()))
# print the BMI data output for Tyrion Lannister
print("The BMI for \"" + str(tl.name) + " with height " + str(tl.height) +
      " and weight " + str(tl.weight) + " lbs is: " + str(tl.calc_bmi()) +
      "\nThe category is " + str(tl.bmi_category()))
# Name: Mike Patak
# ITW 2431
# Lab 10 Prob. 3
# File name: ITW2431_L10_P3_mpatak.py
# MODIFIED: 3/24/22
# PURPOSE:  Create a class named "GOT_cast". The class will have two
#           methods, one for calculating a cast members BMI and a second
#           for determining the cast members BMI category. The program
#           will output the cast members name, height, weight, BMI, and
#           BMI category.
# ASSUMPTIONS:
###########################################################################

# define the class GOT_cast
class GOT_cast:
    # class constructor
    def __init__(self, name, height, weight):
        # initialize instance variable
        self.name = name
        self.height = height
        self.weight = weight
        self.BMI = 0
        self.BMI_category = ""

    # class method to calculate BMI
    def calc_bmi(self):
        # calculate the BMI
        self.BMI = (self.weight / (self.height * self.height)) * 703
        # format the float to always show to significant digits
        format_BMI = "{:.2f}".format(self.BMI)
        # return the value of the BMI
        return format_BMI


    # class method to BMI category
    def bmi_category(self):
        # determine BMI category
        if self.BMI < 18.5:
            self.BMI_category = "underweight"
        elif self.BMI >= 18.5 and self.BMI < 25:
            self.BMI_category = "normal weight"
        elif self.BMI >= 25 and self.BMI < 30:
            self.BMI_category = "overweight"
        elif self.BMI >= 30:
            self.BMI_category = "obese"
        # return the value of the BMI category
        return self.BMI_category


# create a GOT_cast object for Jon Snow, Sawell Tarly, and Tyrion Lannister
js = GOT_cast("Jon Snow", 68, 170)
st = GOT_cast("Samwell Tarly", 68, 238)
tl = GOT_cast("Tyrion Lannister", 53, 110)
# print the BMI data output for Jon Snow
print("The BMI for \"" + str(js.name) + " with height " + str(js.height) +
      " and weight " + str(js.weight) + " lbs is: " + str(js.calc_bmi()) +
      "\nThe category is " + str(js.bmi_category()))
# print the BMI data output for Sawell Tarly
print("The BMI for \"" + str(st.name) + " with height " + str(st.height) +
      " and weight " + str(st.weight) + " lbs is: " + str(st.calc_bmi()) +
      "\nThe category is " + str(st.bmi_category()))
# print the BMI data output for Tyrion Lannister
print("The BMI for \"" + str(tl.name) + " with height " + str(tl.height) +
      " and weight " + str(tl.weight) + " lbs is: " + str(tl.calc_bmi()) +
      "\nThe category is " + str(tl.bmi_category()))
