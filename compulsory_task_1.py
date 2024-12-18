class Course:
    """
    A class representing a course.
    Attributes:
        name (str): The name of the course.
        contact_website (str): The website for course enquiries.
    """
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def head_office_location(self):
        print("The Head Office is located in Cape Town.")

class OOPCourse(Course):
    """
    A class representing a specific OOP course, inheriting from generic
    course class.
    Attributes:
        description (str): A brief description of the course.
        trainer (str): The name of the course trainer.
    """
    def __init__(self, description="OOP Fundementals", trainer="Mr Anon A. Mouse"):
        self.description = description
        self.trainer = trainer

    def trainer_details(self):
        print(f"The course is about {self.description} and is presented by {self.trainer}.")

    def show_course_id(self):
        print("The course ID is #12345")


# Creating an object of subclass
course_1 = OOPCourse()

# Calling required methods
course_1.contact_details()
course_1.head_office_location()
course_1.trainer_details()
course_1.show_course_id()
