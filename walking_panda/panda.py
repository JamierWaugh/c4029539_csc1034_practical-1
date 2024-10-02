from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

from math import pi, sin, cos
#All imports above

class WalkingPanda(ShowBase):
    def __init__(self, no_rotate=False, scale=False, no_walk=False, baby_panda=False,baby_no_rotate = False):
        ShowBase.__init__(self)

        #Load environment model
        self.scene = self.loader.loadModel("models/environment")
        #Reparent the model to render
        self.scene.reparentTo(self.render)

        #Apply scale and position transform the model

        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8,42,0)

        #Add the spinCameraTask procedure to the task manager to spin camera
        if no_rotate == True or baby_no_rotate == True:
            self.taskMgr.add(self.noSpinCameraTask, "NoSpinCameraTask")
        elif no_rotate == False:
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        
        #Load and transform the panda actor
        self.pandaActor = Actor("models/panda-model",
            {"walk": "models/panda-walk4"})
        if baby_panda == True or baby_no_rotate == True:
            self.pandaActor1 = Actor("models/panda-model",
            {"walk": "models/panda-walk4"})
            self.pandaActor1.setScale(0.010,0.010,0.010)
            self.pandaActor1.setPos(-3,8,0)
            self.pandaActor1.reparentTo(self.render)
            self.pandaActor1.loop("walk")

        if scale == True:
            self.taskMgr.add(self.incScale, "incScale")
        else:
            self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render) #Renders panda model

        #Loop walk
        if no_walk == False:
            self.pandaActor.loop("walk")

    def spinCameraTask(self, task):
        angleDegrees = task.time * 7.0
        angleRadians = angleDegrees * (pi/180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees,0,0)
        return Task.cont
    
    def noSpinCameraTask(self, task): #Loads the camera position when camera is not rotating
        self.camera.setPos(3,-20,3)
        self.camera.setHpr(15,0,0)
        return Task.cont
    
    def incScale(self,task):
        self.pandaActor.setScale(0.020, 0.015, 0.015) #increases size of panda


