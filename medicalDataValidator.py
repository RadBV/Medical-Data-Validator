# this program validates a set of medical data to ensure that it complies with a set of rules

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


def findInvalidRecords(patientID, age, gender, diagnosis, medications, lastVisitID):
    constraints = {}
    return constraints

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
        # checks whether keys in dict match keySet, prints error message if not and sets isInvalid to True
        if set(dictionary.keys()) != keySet:
            print(f"Invalid format: {dictionary} at position {index} has missing and/or invalid keys.")
            isInvalid = True

    # if isInvalid is True, return False
    if isInvalid:
        return False
    
    # if all checks pass, print message and return True
    print("Valid format.")
    return True

validate(medicalRecords)