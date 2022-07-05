# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# INPUT
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# OUTPUT
# 56.00

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    filtered = []
    
    for (k, v) in student_marks.items():
        if k == query_name:
            filtered.append(v)
    filtered = filtered[0]      
    result = round(sum(filtered) / len(filtered), 2)       
    format_float = "{:.2f}".format(result)
    print(format_float)