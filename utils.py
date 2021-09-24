#source: https://www.tutorialspoint.com/How-to-find-the-nth-occurrence-of-substring-in-a-string-in-Python
def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)

def componentsProcess(component_str):
    component = []
    tmp = component_str.split('(')
    tmp2 = tmp[0].strip(' ').split(',')
    for word in tmp2:
        component.append(word.strip(' '))
    return component

def levelsProcess(level_str):
    tmp = []
    if('wizard' in level_str):
        tmp = level_str[level_str.find('wizard'):level_str.find('wizard')+8]
        level = int(tmp[-1])
    else:
        level = 0
    return level