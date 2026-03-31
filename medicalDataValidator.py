# this program validates a set of medical data to ensure that it complies with a set of rules

# create medical data list of dicts, each dict represents a patient
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