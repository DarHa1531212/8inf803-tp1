#source: https://www.tutorialspoint.com/How-to-find-the-nth-occurrence-of-substring-in-a-string-in-Python

def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)

def componentsProcess(component_str):
    component = []
    if ('V' in component_str):
        component.append('V')
    if ('S' in component_str):
        component.append('S')
    if ('M' in component_str):
        component.append('M')
    return component