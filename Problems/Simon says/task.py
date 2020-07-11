def what_to_do(instructions):
    sub = 'Simon says'
    if sub in instructions:
        ind = instructions.find(sub)
        len_i = len(instructions)
        len_s = len(sub)

        if ind == 0 and len(instructions[len_s + 1:]) == len_i - len_s - 1:
            return 'I {}'.format(instructions.lstrip(sub + ' '))
        if ind > 0 and len(instructions[:len_s + 1]) == len_i - len_s - 1:
            return 'I {}'.format(instructions.rstrip(' ' + sub))

    return 'I won\'t do it!'
