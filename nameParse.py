rawNames = ['John Jacob Jingleheimer Schmidt, Jr.', 'Alan Rickman', 'Bruce Fuckin Willis Jr.', 'Harry Albus Severus James Potter', 'Harry Albus Severus James Potter Jr.', 'Harry Conick, Jr.', 'Adolfo J. Cotilla, Jr., AIA', 'As Many Names As I Want To Have']
commonSuffixes = ['Jr', 'Jr.', 'jr', 'jr.', 'JR', 'JR.', 'Sr.', 'Sr', 'sr', 'sr.', 'SR', 'SR.']

for name in rawNames:
    commaParse = name.split(',')
    try:
        suffix = commaParse[1]
    except:
        suffix = ''
        pass
    nameOnly = commaParse[0].split(' ')
    if len(nameOnly) > 2:
        if nameOnly[-1] in commonSuffixes:
            suffix = nameOnly[-1]
            nameOnly.pop(-1)
            fName = nameOnly[0]
            mName = nameOnly[1]
            lName = ' '.join(nameOnly[2:])
        else:
            fName = nameOnly[0]
            mName = nameOnly[1]
            lName = ' '.join(nameOnly[2:])
    else:
        fName = nameOnly[0]
        mName = ''
        lName = nameOnly[1]

    print('FirstName: ' + fName)
    print('MiddleName: ' + mName)
    print('LastName: ' + lName)
    print('Suffix: ' + suffix)
