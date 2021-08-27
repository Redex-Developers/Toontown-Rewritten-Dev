from panda3d.core import *
import __builtin__
import os

if __debug__:
    # __debug__ is only 1 in dev builds; Mirai's builder will set it to 0
    # (and it will, in fact, remove entire if __debug__: sections)
    loadPrcFile('config/dev.prc')

# The VirtualFileSystem, which has already initialized, doesn't see the mount
# directives in the config(s) yet. We have to force it to load those manually:
from panda3d.core import VirtualFileSystem, ConfigVariableList, Filename
vfs = VirtualFileSystem.getGlobalPtr()
mounts = ConfigVariableList('vfs-mount')
for mount in mounts:
    mountfile, mountpoint = (mount.split(' ', 2) + [None, None, None])[:2]
    vfs.mount(Filename(mountfile), Filename(mountpoint), 0)

import glob
for file in glob.glob('resources/*.mf'):
    mf = Multifile()
    mf.openReadWrite(Filename(file))
    names = mf.getSubfileNames()
    for name in names:
        ext = os.path.splitext(name)[1]
        if ext not in ['.jpg', '.jpeg', '.ogg', '.rgb']:
            mf.removeSubfile(name)
    vfs.mount(mf, Filename('/'), 0)

class game:
    name = 'toontown'
    process = 'client'


__builtin__.game = game()
import time
import sys
import random
import __builtin__
try:
    launcher
except:
    from toontown.launcher.TTRLauncher import TTRLauncher
    launcher = TTRLauncher()
    __builtin__.launcher = launcher

if launcher.isDummy():
    http = HTTPClient()
else:
    http = launcher.http
tempLoader = Loader()
from direct.gui import DirectGuiGlobals
import ToontownGlobals
DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
launcher.setPandaErrorCode(7)
import ToonBase
ToonBase.ToonBase()
print 'ToontownStart: loading settings module'
print 'ToontownStart: Starting the game.'
print 'ToontownStart: setting default font'
from panda3d.core import *
if base.win == None:
    print 'Unable to open window; aborting.'
    sys.exit()
from direct.gui.DirectGui import *
#backgroundNode = tempLoader.loadSync(Filename('phase_3/models/gui/loading-background'))
backgroundNode = tempLoader.loadSync(Filename('phase_3/models/gui/entering-background'))
eyes = loader.loadModel('phase_3/models/gui/toontown-logo')
findeyes = eyes.find('**/eyes')
launcher.setPandaErrorCode(0)
launcher.setPandaWindowOpen()
ConfigVariableDouble('decompressor-step-time').setValue(0.01)
ConfigVariableDouble('extractor-step-time').setValue(0.01)
backgroundNodePath = aspect2d.attachNewNode(backgroundNode, 0)
backgroundNodePath.setPos(0.0, 0.0, 0.0)
backgroundNodePath.setScale(aspect2d, VBase3(2))
eyes = OnscreenGeom(geom = findeyes, pos = (0, 0, 0), scale = (0.25, 0.25, 0.25))

# Framerate meter for TTR Private: Change in 'dev.prc' to toggle

if ConfigVariableBool('tt-framerate', False):
    from toontown.toonbase.TTFrameRateMeter import TTFrameRateMeter
    TTFrameRateMeter()

base.graphicsEngine.renderFrame()
DirectGuiGlobals.setDefaultRolloverSound(base.loader.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
DirectGuiGlobals.setDefaultClickSound(base.loader.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
DirectGuiGlobals.setDefaultDialogGeom(loader.loadModel('phase_3/models/gui/dialog_box_gui'))
import TTLocalizer
from otp.otpbase import OTPGlobals
OTPGlobals.setDefaultProductPrefix(TTLocalizer.ProductPrefix)
print 'ToontownStart: Loading default gui sounds'
DirectGuiGlobals.setDefaultRolloverSound(base.loader.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
DirectGuiGlobals.setDefaultClickSound(base.loader.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
music = None
import ToontownLoader
from direct.gui.DirectGui import *
serverVersion = config.GetString('server-version', 'no_version_set')
print 'ToontownStart: serverVersion: ', serverVersion
from ToonBaseGlobal import *
from direct.showbase.MessengerGlobal import *
from toontown.distributed import ToontownClientRepository
cr = ToontownClientRepository.ToontownClientRepository(serverVersion, launcher)
cr.music = music
base.initNametagGlobals()
base.cr = cr
loader.endBulkLoad('init')
from otp.friends import FriendManager
from otp.distributed.OtpDoGlobals import *
cr.generateGlobalObject(OTP_DO_ID_FRIEND_MANAGER, 'FriendManager')
if not launcher.isDummy():
    base.startShow(cr, launcher.getGameServer())
else:
    base.startShow(cr)
time.sleep(0.5)
backgroundNodePath.reparentTo(hidden)
backgroundNodePath.removeNode()
del backgroundNodePath
del backgroundNode
eyes.destroy()
del eyes
del tempLoader

'''New Loading Screen'''
from toontown.toontowngui import NewLoadingScreen

loading = NewLoadingScreen.NewLoadingScreen()

loading.newMusic()
loading.newVersion()
loading.connectBackground()
loading.newLogo()

base.loader = base.loader
__builtin__.loader = base.loader
autoRun = ConfigVariableBool('toontown-auto-run', 1)
if autoRun:
    try:
        run()
    except SystemExit:
        raise
    except:
        from direct.showbase import PythonUtil
        print PythonUtil.describeException()
        raise
