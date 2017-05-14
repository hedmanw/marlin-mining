import re


def main(file_name):
    copy = 0
    paste = 0
    undo = 0
    deleteKey = 0
    backspaceKey = 0
    copyChanges = 0
    enterKey = 0
    tabKey = 0
    typeIfDef = 0
    typeElse = 0
    typeEndif = 0
    typeAny = 0
    textCorrections = 0
    selections = 0

    with open(file_name) as log_file:
        lines = log_file.readlines()
        typed_previous = False
        for line in lines:
            reset_type = True

            def c(string):
                return string in line
            if c("M1+c") or c("M1+x"):
                copy += 1
            elif c("M1+v"):
                paste += 1
            elif c("M1+z"):
                undo += 1
            elif c("Del"):
                deleteKey += count_times(line)
            elif c("BackSpace"):
                backspaceKey += count_times(line)
            elif c("Copy Current"):
                copyChanges += 1
            elif c("key-type Enter"):
                enterKey += count_times(line)
            elif c("key-type Tab"):
                tabKey += count_times(line)
            elif re.match(r".*#ifdef.*", line, re.IGNORECASE):
                typeIfDef += 1
                typed_previous = True
                reset_type = False
            elif re.match(r".*#else.*", line, re.IGNORECASE):
                typeElse += 1
                typed_previous = True
                reset_type = False
            elif re.match(r".*#endif", line, re.IGNORECASE):
                typeEndif += 1
                typed_previous = True
                reset_type = False
            elif c("type-text"):
                typeAny += 1
                typed_previous = True
                reset_type = False
            elif c("select-range"):
                selections += 1

            if typed_previous and (c("BackSpace") or c("Del")):
                textCorrections += 1

            if reset_type:
                typed_previous = False

    fn_index = file_name.rfind('/')+1
    identifier = file_name[fn_index:fn_index+5]
    values = [identifier, copy, paste, undo, deleteKey, backspaceKey, copyChanges, enterKey, tabKey, typeIfDef, typeElse, typeEndif, typeAny, textCorrections, selections]
    print ",".join(map(str, values))


def count_times(line):
    if "times" in line:
        return int(line[line.rfind(' '):])
    else:
        return 1

if __name__ == '__main__':
    main("PATH")