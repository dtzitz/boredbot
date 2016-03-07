
def removeGarbage(dirtyList):

    for item in dirtyList:
        if item.text == 'CL Recommends':
            dirtyList.remove(item)

    for item in dirtyList:
        if item.text == 'User Submitted':
            dirtyList.remove(item)

    for item in dirtyList:
        if item.text == 'All Ages':
            dirtyList.remove(item)

    for item in dirtyList:
        if item.text == 'Members Pick':
            dirtyList.remove(item)

    # for item in dirtyList:
        # print(item.get('href'))
