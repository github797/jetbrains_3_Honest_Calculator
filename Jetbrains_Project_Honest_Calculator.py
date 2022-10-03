msg_: list = ["Enter an equation",
              "Do you even know what numbers are? Stay focused!",
              "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
              "Yeah... division by zero. Smart move...",
              "Do you want to store the result? (y / n):",
              "Do you want to continue calculations? (y / n):",
              " ... lazy",
              " ... very lazy",
              " ... very, very lazy",
              "You are",
              "Are you sure? It is only one digit! (y / n)",
              "Don't be silly! It's just one number! Add to the memory? (y / n)",
              "Last chance! Do you really want to embarrass yourself? (y / n)"]

memory = 0.0


def is_one_digit(v):
    if -10 < v < 10 and float(v).is_integer() is True:
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) is True and is_one_digit(v2) is True:
        msg = msg + msg_[6]
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_[7]
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_[8]
    if msg != '':
        msg = msg_[9] + msg
        print(msg)


while True:
    calc = input('{}\n'.format(msg_[0]))
    x, oper, y = calc.split()

    try:
        x = memory if x == 'M' else float(x)
        y = memory if y == 'M' else float(y)

        if oper in '+-*/':
            check(x, y, oper)
            result = x + y if oper == '+' else x - y if oper == '-' else x * y if oper == '*' else x / y
            print(result)
        else:
            print(msg_[2])

    except ValueError:
        print(msg_[1])

    except ZeroDivisionError:
        print(msg_[3])

    else:
        while True:  # Do you want to store the result?
            answer_1 = input('{}\n'.format(msg_[4]))
            if answer_1 == 'y':

                if is_one_digit(result):
                    msg_index = 10
                    while msg_index <= 12:
                        answer_3 = input('{}\n'.format(msg_[msg_index]))
                        if answer_3 == 'y':
                            if msg_index < 12:
                                msg_index += 1
                            else:
                                memory = result
                                break
                        elif answer_3 == 'n':
                            break
                        else:
                            continue
                else:
                    memory = result
                    break
            elif answer_1 == 'n':
                break
            break

        while True:  # Do you want to continue calculations?
            answer_2 = input('{}\n'.format(msg_[5]))
            if answer_2 == 'y':
                break
            elif answer_2 == 'n':
                quit()
