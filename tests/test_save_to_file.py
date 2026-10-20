import pytest
from gradebook import Roster, GradeBookIOError


def test_save_to_file_writes_expected_content(make_student, mocker):
    # Arrange
    roster = Roster()

    student = make_student("Ali", 101, [80, 90])
    roster.add_student(student)

    mock_open = mocker.patch("builtins.open", mocker.mock_open())

    # Act
    roster.save_to_file("students.txt")

    # Assert
    mock_open.assert_called_once_with("students.txt", "w")

    handle = mock_open()
    handle.write.assert_called_once_with("Ali,101,80,90\n")


def test_save_to_file_handles_os_error(make_student, mocker):
    # Arrange
    roster = Roster()

    student = make_student("Ali", 102, [80, 90])
    roster.add_student(student)

    mocker.patch(
        "builtins.open",
        side_effect=OSError("Disk error")
    )

    # Act & Assert
    with pytest.raises(GradeBookIOError):
        roster.save_to_file("students.txt")