# this program validates a set of medical data to ensure that it complies with a set of rules
import re # imports regular expression module for pattern matching

# var that holds a list of dicts, each dict represents a patient
medicalRecords = [
    {
        'patientID': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'lastVisitID': 'V2301',
    },
    {
        'patientID': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'lastVisitID': 'v2302',
    },
    {
        'patientID': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'lastVisitID': 'v2303',
    },
    {
        'patientID': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'lastVisitID': 'V2304',
    }
]
# var with same format as above that holds invalid info (additional testcase)
invalidMedicalRecords = [
    {
        'patientI': 'g2223',
        'age': -2,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'lastVisitID': 'V2301',
    },
    {
        'patientID': 'p1002',
        'a': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 45],
        'lastVisitID': 'v2302',
    },
]

# function that checks if all arguments are valid and returns a list of invalid arguments as strings, or empty list if all args are valid
def findInvalidRecords(patientID, age, gender, diagnosis, medications, lastVisitID):

    # dict that checks each value of this function's arguments and makes sure it matches the correct pattern
    # key is the name of the arg, value is a bool that is True if arg type/pattern is correct and False if not
    constraints = {
        "patientID": isinstance(patientID, str) and re.fullmatch("p\d+", patientID, re.IGNORECASE), # checks if patientID is a str and matches pattern of "p" followed by digits
        "age": isinstance(age, int) and age >= 18, # checks if age is an int and at least 18
        "gender": isinstance(gender, str) and gender.lower() in ("male","female"), # checks if gender is a str and one of two values (two for simplicity)
        "diagnosis": isinstance(diagnosis, str) or diagnosis is None, # checks if diagnosis is a str or None
        "medications": isinstance(medications, list) and all([isinstance(med, str) for med in medications]), # checks if medications is a list and all items within are str
        "lastVisitID": isinstance(lastVisitID, str) and re.fullmatch("v\d+", lastVisitID, re.IGNORECASE) # checks if lastVisitID is a str and matches pattern of "v" followed by digits
    }
    return [key for key, value in constraints.items() if not value] # returns list of keys in constraints where value is False (invalid data)

# validate function that checks if data is correct
def validate(data):
    ### all variables stored at the top of this function for better readability ###
    isSequence = isinstance(data, (list, tuple)) # var that stores bool indicating whether data type is correct type (list or tuple)
    isInvalid = False # var that stores bool indicating whether any dict in data is invalid (not a dict)
    keySet = set(['patientID', 'age', 'gender', 'diagnosis', 'medications', 'lastVisitID'])  # var that stores set of keys required in each dict
    
    # checks whether data is wrong type, prints error message and returns False
    if not isSequence:
        print("Invalid format: expected a list or tuple.")
        return False
    
    # iterates through index and dict in enumerated data
    for index, dictionary in enumerate(data):
        # checks whether each item in data is a dict, prints error message if not and sets isInvalid to True
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            isInvalid = True
            continue # if not a dict, skip to next item in data (prevents AttributeError on line 75)
        # checks whether keys in dict match keySet, prints error message if not and sets isInvalid to True
        if set(dictionary.keys()) != keySet:
            print(f"Invalid format: {dictionary} at position {index} has missing and/or invalid keys.")
            isInvalid = True
            continue # if keys don't match, skip to next item in data (prevents KeyError on line 80)
        
        invalidRecords = findInvalidRecords(**dictionary) # var that stores list of invalid args in dict
        
        # iterates through invalidRecords, prints error message for each invalid arg and sets isInvalid to True
        for key in invalidRecords:
            print(f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
            isInvalid = True

    # if isInvalid is True, return False
    if isInvalid:
        return False
    
    # if all checks pass, print message and return True
    print("Valid format.")
    return True

validate(invalidMedicalRecords)
