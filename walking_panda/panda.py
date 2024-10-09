from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

music = "../src/windy-forest-and-birds-ambience-211720.wav"

from math import pi, sin, cos

#All imports above

class WalkingPanda(ShowBase):
    def __init__(self, no_rotate=False, scale=1.0, no_walk=False, baby_panda=False,baby_no_rotate = False):
        ShowBase.__init__(self)
        #Load environment model
        self.scene = self.loader.loadModel("models/environment")

        #Reparent the model to render
        self.scene.reparentTo(self.render)

        #Apply scale and position transform the model
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8,42,0)

        #Load background music
        self.background_music = self.loader.loadMusic(music)
        # Set background music to loop
        self.background_music.setLoop(True)
        # Start playing background music
        self.background_music.play()

        #Add the spinCameraTask procedure to the task manager to spin camera depending on no_rotate
        if no_rotate == True or baby_no_rotate == True:
            self.taskMgr.add(self.noSpinCameraTask, "NoSpinCameraTask")
        elif no_rotate == False:
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        
        #Load and transform the panda actor
        self.pandaActor = Actor("models/panda-model",
            {"walk": "models/panda-walk4"})
        if baby_panda == True or baby_no_rotate == True: #Creates second panda actor when applicable
            self.pandaActor1 = Actor("models/panda-model",
            {"walk": "models/panda-walk4"}) 
            self.pandaActor1.setScale(0.010,0.010,0.010) #In this case, this panda is the mother so is scaled larger
            self.pandaActor1.setPos(-3,8,0) #The position of this panda is moved so that it can fit in the frame and not clip into the baby panda
            self.pandaActor1.reparentTo(self.render)
            self.pandaActor1.loop("walk")

        self.pandaActor.setScale((scale*0.005), (scale*0.005), (scale*0.005)) #increases size of panda based upon scale variable (default 1)
        self.pandaActor.reparentTo(self.render) #Renders panda model

        #Loop walk
        if no_walk == False:
            self.pandaActor.loop("walk")

    def spinCameraTask(self, task): #Function for spinning camera
        angleDegrees = task.time * 7.0
        angleRadians = angleDegrees * (pi/180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees,0,0)
        return Task.cont
    
    def noSpinCameraTask(self, task): #Loads the camera position when camera is not rotating
        self.camera.setPos(3,-20,3)
        self.camera.setHpr(15,0,0)
        return Task.cont
        
