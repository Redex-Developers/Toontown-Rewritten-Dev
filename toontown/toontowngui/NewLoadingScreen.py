from direct.gui.DirectGui import *
from direct.gui import DirectGuiGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import DirectObject
import string
import time
from threading import Timer
from otp.otpbase import OTPGlobals
from otp.otpbase import OTPLocalizer
from direct.interval.IntervalGlobal import LerpScaleInterval, Sequence, Func
from panda3d.core import *
from toontown.toonbase import ToontownGlobals

class NewLoadingScreen(DirectObject.DirectObject):

    def __init__(self):
        DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)

    def newMusic(self):
        base.musicManager.setConcurrentSoundLimit(2)
        global music
        global music2
        music = base.musicManager.getSound('phase_3/audio/bgm/ttr_d_theme_phase1.ogg')
        music2 = base.musicManager.getSound('phase_3/audio/bgm/ttr_d_theme_phase2.ogg')
        if music:
            music.setVolume(0.8)
            music2.setVolume(0)
            music.setLoop(True)
            music2.setLoop(True)
            music.play()
            music.setTime(2.859)
            music2.play()
            music2.setTime(2.859)
        base.musicManager.update() 

    def exitMusic(self):
        music.stop()
        music2.stop()

    def newVersion(self):
        serverVersion = config.GetString('server-version', 'no_version_set')
        global version
        version = OnscreenText(serverVersion, pos=(-1, -1.2), scale=0.055, font=loader.loadFont('phase_3/models/fonts/ImpressBT.ttf'), fg=Vec4(1, 1, 1, 1), align=TextNode.ALeft)
        version.setPos(0.12,0.045)
        version.reparentTo(base.a2dBottomLeft)
        stop = version.cleanup
        return version

    def connectBackground(self):
        global connectbg
        connectbg = OnscreenImage(image='phase_3/maps/tt_t_gui_pat_background.jpg', scale = (2, 2, 1))
        connectbg.setBin('background', 1)

    def newLogo(self):
        logobam = loader.loadModel('phase_3/models/gui/toontown-logo')
        findlogo = logobam.find('**/logo')
        global logo
        logo = OnscreenGeom(geom = findlogo, pos = (0, 0, 0.35))
        logoSeq = Sequence(
        LerpScaleInterval(logo, 3.25, Vec3(0.20625, 0.225, 0.20625), Vec3(0.1375, 0.3, 0.1375), blendType='easeInOut'),
        LerpScaleInterval(logo, 3.25, Vec3(0.1375, 0.3, 0.1375), Vec3(0.20625, 0.225, 0.20625), blendType='easeInOut')).loop()

    def cleanup(self):
        version.destroy()
        logo.destroy()
        connectbg.destroy()

    def musicFade(self):
        music.setVolume(0.8)
        music2.setVolume(0.1)
        time.sleep(0.05)
        music.setVolume(0.75)
        music2.setVolume(0.15)
        time.sleep(0.05)
        music.setVolume(0.7)
        music2.setVolume(0.2)
        time.sleep(0.05)
        music.setVolume(0.65)
        music2.setVolume(0.25)
        time.sleep(0.05)
        music.setVolume(0.6)
        music2.setVolume(0.3)
        time.sleep(0.05)
        music.setVolume(0.55)
        music2.setVolume(0.35)
        time.sleep(0.05)
        music.setVolume(0.5)
        music2.setVolume(0.4)
        time.sleep(0.05)
        music.setVolume(0.45)
        music2.setVolume(0.45)
        time.sleep(0.05)
        music.setVolume(0.4)
        music2.setVolume(0.5)
        time.sleep(0.05)
        music.setVolume(0.35)
        music2.setVolume(0.55)
        time.sleep(0.05)
        music.setVolume(0.3)
        music2.setVolume(0.6)
        time.sleep(0.05)
        music.setVolume(0.25)
        music2.setVolume(0.65)
        time.sleep(0.05)
        music.setVolume(0.2)
        music2.setVolume(0.7)
        time.sleep(0.05)
        music.setVolume(0.15)
        music2.setVolume(0.75)
        time.sleep(0.05)
        music.setVolume(0.1)
        music2.setVolume(0.8)
        time.sleep(0.05)
        music.setVolume(0)
        music2.setVolume(0.8)
        time.sleep(0.05)