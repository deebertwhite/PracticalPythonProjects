import os, shutil, winshell

## TEMP FOLDER EMPTY PROCESS ##
## SOME FILES WILL NOT BE DELETED ##

tempPathLocal = r'C:\Users\JAMES~1.W_U\AppData\Local\Temp'
tempDeleteLocal = os.listdir(tempPathLocal)

for file in tempDeleteLocal:
    tempDeletePath = os.path.join(tempPathLocal, file)
    try:
        if os.path.isfile(tempDeletePath) or os.path.islink(tempDeletePath):
            os.unlink(tempDeletePath)
        elif os.path.isdir(tempDeletePath):
            shutil.rmtree(tempDeletePath)
    except Exception as e:
        print('Failed to delete %s. Reason %s' % (tempDeletePath, e))

## TEMP FOLDER EMPTY PROCESS ##
## SOME FILES MAY NOT BE DELETED ##

tempPath = r'C:\Windows\Temp'
tempDelete = os.listdir(tempPath)

for file in tempDelete:
    tempDeletePath = os.path.join(tempPath, file)
    try:
        if os.path.isfile(tempDeletePath) or os.path.islink(tempDeletePath):
            os.unlink(tempDeletePath)
        elif os.path.isdir(tempDeletePath):
            shutil.rmtree(tempDeletePath)
    except Exception as e:
        print('Failed to delete %s. Reason %s' % (tempDeletePath, e))

## EMPTY RECYCLE BIN IF FULL ##

isBinEmpty = list(winshell.recycle_bin())

if isBinEmpty == []:
    print('Nothing to delete')
else:
    winshell.recycle_bin().empty()
