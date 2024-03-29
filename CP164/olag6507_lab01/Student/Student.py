'''
Student class definition
stores simple student data 
'''

class Student:
    """ 
    constants
    """
    
    GENDERS = ("F", "M", "T")  # Define allowed gender values
    
    def __init__(self, student_id, surname, forename,gender, birth_date):
        
        
        """
        Initializes student Attributes
        
        Returns:
            A student object
        """
        
        assert gender in Student.GENDERS, \
        "Gender must be one of {}".format(Student.GENDERS)
        
        assert len(student_id)==9 and student_id.isdigit(), \
        "Student ID must be a 9 digit string"
        
        self.student_id = student_id  
        self.surname = surname
        self.forename =forename
        self.gender = gender
        self.birth_date = birth_date
        
        
              
    def __str__(self):
        """
        Return a string version of a student in the format 
        id
        surname, forename
        gender, birthdate
        Use: print(student)
        Use: print("{}".format(student))
        Use: string = str(student)
        -----------------------------------------------
        Returns:   
            string - a formatted version of the student dat(str)
        -----------------------------------------------
        """
        string = """{}
    {},{}
    {},{}""".format(self.student_id, self.surname,
                        self.forename, self.gender,self.birth_date)
        return string
    
    def __eq__(self, other):
        """ 
        ---------------------------------------------
        compares against another student for equality.
        Use: student == other
        ----------------------------------------------
        Parameters:
            other - other student to compare to
        Returns:
           result - True if student ID match, False otherwise (boolean)    
        """
        
        result = self.student_id == other.student_id
        return result
    
    def __lt__(self, other):
        """
        -----------------------------------------------
        Determines if this student precedes another.
        If student IDs don't match (using already defined == operator),
        compare student's by name then by ID.
        Use: student < other
        ---------------------------------------------------
        """
        
        if self == other:
            result = False
        else:
            result = \
               (self.surname.lower(), self.forename.lower(),self.birth_date) < \
               (other.surname.lower(), other.forename.lower(),other.birth_date) 
        return result
    
    def __le__(self, other):
            
        """
        -----------------------------------------------
        Determines if this student precedes another.
        If student IDs don't match (using already defined == operator),
        compare student's by name then by ID.
        Use: student < other
        ---------------------------------------------------
        """     
        result = (self == other or self < other) 
        return result
        