room_numbers = {"CS101": 3004,"CS102": 4501,"CS103": 6755, "NT110": 1244,"CM241": 1411}

instructors = {"CS101": "Haynes","CS102": "Alvarado","CS103": "Rich","NT110": "Burke","CM241": "Lee"}

meeting_times = {"CS101": "8:00 a.m.","CS102": "9:00 a.m.","CS103": "10:00 a.m.","NT110": "11:00 a.m.","CM241": "1:00 p.m."}
def get_course_info(course_number):
    room = room_numbers.get(course_number)
    instructor = instructors.get(course_number)
    time = meeting_times.get(course_number)

    if room and instructor and time:
        return f"Course Number: {course_number}\nRoom Number: {room}\nInstructor: {instructor}\nMeeting Time: {time}"
    else:
        return "Course not found."
course_number = input("Enter a course number (e.g., CS101): ")
print(get_course_info(course_number))