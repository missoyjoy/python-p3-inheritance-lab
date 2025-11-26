#!/usr/bin/env python

from user import User

class Student(User):

    knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]
    
    def learn(self, New_information):
        self.knowledge = Student.knowledge
        self.knowledge.append(New_information)
        return self.knowledge