#create a list from other

def example_1_with_a_cycle():
    course =[]
    for character in 'python':
        course.append(character)
    print(course)

def compressionList():
    cuourse = [letras for letras in 'python']
    print(cuourse)


def compressionNumberList():
    list_a = [1,2,3,4,5,6,7]
    list_b = [i*2 for i in list_a] #compress a list using a cycle inside brackets, you can manipulate the variable to add wanted behaviour
    print(list_b)

compressionNumberList()