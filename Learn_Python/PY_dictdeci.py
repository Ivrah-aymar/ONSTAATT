if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #print(student_marks)
    for name,scores in student_marks.items():
        if name == query_name:
            marks=list(student_marks.get(name))
    avg=sum(marks)/len(marks)
    print(f'{avg:.2f}')
