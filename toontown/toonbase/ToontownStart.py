from panda3d.core import *

loadPrcFile('config/dev.prc')

if ConfigVariableBool('want-new-ttrloader', False):
    import ToontownStartNEW
    ToontownStartNEW()
else:
    import ToontownStartOLD
    ToontownStartOLD()