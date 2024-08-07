students = {
    'student1': {
        'name': 'Eman',
        'age': 20,
        'grades': {
            'Math': 90,
            'Science': 85,
            'English': 88
        }
    },
    'student2': {
        'name': 'Laiba',
        'age': 22,
        'grades': {
            'Math': 78,
            'Science': 82,
            'English': 79
        }
    },
    'student3': {
        'name': 'Momina',
        'age': 21,
        'grades': {
            'Math': 85,
            'Science': 90,
            'English': 87
        }
    }
}
print("Nested Dictionary of Students:")
for student, info in students.items():
    print(f"\n{student}:")
    for key, value in info.items():
        print(f"  {key}: {value}")