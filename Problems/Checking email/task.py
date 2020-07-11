def check_email(string):
    s_list = string.split('@')
    if len(s_list) == 2 and not s_list[1].startswith('.'):
        if len(s_list[0]) == 0 or len(s_list[1]) == 0:
            return False
        if (' ' in s_list[0]) or (' ' in s_list[1]) or ('.' not in s_list[1]):
            return False
        return True
    return False
