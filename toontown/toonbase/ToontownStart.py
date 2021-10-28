from panda3d.core import *

print('Toontown Rewritten Private is an ongoing project by Redex Development')
loadPrcFile('config/dev.prc')

if ConfigVariableBool('want-new-ttrloader', False):
    import ToontownStartNEW
    ToontownStartNEW()
else:
    import ToontownStartOLD
    ToontownStartOLD()
