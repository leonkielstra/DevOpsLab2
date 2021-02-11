import connexion
import six

from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util
from swagger_server.services import student_service


def add_student(body):  # noqa: E501
    """Add a new student

     # noqa: E501

    :param body: Student object that needs to be added
    :type body: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
    return student_service.add_student(body)


def delete_student(student_id):  # noqa: E501
    """Delete student by ID

     # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int

    :rtype: Student
    """
    return student_service.delete_student(student_id)


def get_student_by_id(student_id=None, subject=None):  # noqa: E501
    """Find student by ID

    Returns a single student # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int

    :param subject: The subject name
    :type subject: str

    :param last_name: The student's last name
    :type last_name: str

    :rtype: Student
    """

    return student_service.get_student_by_id(student_id, subject)

def get_student_by_last_name(last_name=None):
    """Find student by query

    Returns a single student # noqa: E501

    :param last_name: The student's last name
    :type last_name: str

    :rtype: Student
    """

    return student_service.get_student_by_last_name(last_name)
