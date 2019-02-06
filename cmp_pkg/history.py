import sys

def history(**kwargs):
    history = []
    index = 1
    padsize = 0

    sys.stdout.write("\n")
    with open('.history') as fp:
        history = fp.readlines()

    if 'params' in kwargs:
        if len(kwargs['params']) > 0:
            cmd_num = kwargs['params'][0]
            return history[int(cmd_num)]

    hsize = len(history)

    hout = ""
    for h in history:
        hout += " "+str(index).zfill(3)+" "+h.strip()
        index += 1

    return hout