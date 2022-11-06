# Assignment 3 Problem 1: Z-score

#################
#  SAMPLE DATA  #
#################
# First data set: a list of positive integers (not a normal distribution)
population1 = [14, 28, 96, 97, 21, 29, 29, 4, 58,
               42, 25, 97, 49, 33, 75, 53, 14, 53,
               45, 87, 75, 66, 62, 55, 57, 44, 44,
               94, 19, 96, 12, 59, 86, 88, 61, 68,
               37, 64, 19, 46, 68, 98, 19, 54, 65,
               30, 1, 82, 76, 3]

# Second data set: a list of negative and positive integers (normal distribution)
population2 = [-16, 10, -15, -6, -5, -20, -11, 9, -9, -7, 5, -14, 6, -10, -22, -19, 21, 11, -18, -13, -24, -21, 14, 19,
               20, 13, 16, 8, 4, 3, 18, 22, 17, 7, -12, -3, 23, -8, 2, -2, -4, 1, 12, -25, -1, 15, 0, -23, -17, 24]

# Third data set: a list of positive integers (normal distribution)
population3 = [125, 475, 275, 550, 350, 325, 575, 25, 225, 150, 425, 75, 175, 650, 600, 625, 675, 250, 100, 0, 375, 500,
               400, 450, 300, 525, 50, 200]

#Fourth Data Set: Chosen by Tester

#Fifth Data Set: Chosen by Tester

#################
#  FUNCTIONS    #
#################

def mean(data_set):
    """
    This function will return the mean of the data_set(population)
    **Do not change this function**
    """
    return sum(data_set) / len(data_set)


def stdev(data_set, avg):
    """
    This function will return the standard deviation of the data_set(population),
     given the mean of the data_set (avg)
    **Do not change this function**
    """
    variance = sum([(integer - avg) ** 2 for integer in data_set]) / len(data_set)
    # return the square root of the variance calculation
    return variance ** .5


def least(data_set):
    """
    returns the least value in the data_set(population)
    **Do not change this function**
    """
    return min(data_set)


def greatest(data_set):
    """
    returns the greatest value in the data_set(population)
    **Do not change this function**
    """
    return max(data_set)


# Your grader will use this function to help them verify your code
def test_z_score_function():
    pop1_avg = mean(population1)
    pop1_sd = stdev(population1, pop1_avg)

    mean_z_score_p1 = z_score(pop1_avg, pop1_avg, pop1_sd)

    pop2_greatest = greatest(population2)
    pop2_avg = mean(population2)
    pop2_sd = stdev(population2, pop2_avg)

    greatest_z_score_p2 = z_score(pop2_greatest, pop2_avg, pop2_sd)

    print("The z-score of the mean of population1 is", mean_z_score_p1)
    print("The z-score of the greatest value of population2 is", greatest_z_score_p2)


#####################################################
# YOUR CODE GOES BELOW THIS BOX.                    #
#                                                   #
# Complete the following z_score function.		      #
# You may call the functions above,		              #
#  but do not define any others (except for testing)#
# You may use arithmetic operators,                 #
#   i.e. +, -, *, **, /					                    #
#####################################################

#OUR CODE:
#Usage: This function is easy to use and requires two inputs.
#The first input is a number from a dataset.
#The second input is a variable representing a set of numbers.
#This function will report whether the data is a normal distribution
#AND the zscore of the datapoint entered in regards to its set.

#NOTE TO TESTER: You will need to find two more data sets to test.
#If possible try to find a set with a normal distrubution and without to verify
#the function in two ways.


#z_score code:

def z_score(data_Point, dataset):
    mean1 = mean(dataset) #Finding Mean
    dev1 = stdev(dataset,mean1) #Determining Standard Deviation
    sum1 = data_Point - mean1 #Point minus Mean
    zscore1 = sum1/dev1 #zscore of the point in regards to the set
    popmax = greatest(dataset) #Extracting Highest Point
    popmin = least(dataset) #Extracting Lowest Point
    sum2 = popmax - mean1 #Max Minus Mean
    sum3 = popmin - mean1 #Min Minus Mean
    zscoremax = sum2 / dev1 #Max zscore
    zscoremin = sum3 / dev1 #Min zscore
    test1 = zscoremax + zscoremin #Summing the Max and Min to test for normalcy
    if test1 == 0: #Condition of normalcy
        print("This is a normal distribution.") #Normal confirmation phrase
    else: print("This is not a normal distribution.") #Abnormal confirmation phrase
    print("The zscore of the datapoint in regards to the set is:") #reporting zscore of point vs set
    return print(zscore1)

