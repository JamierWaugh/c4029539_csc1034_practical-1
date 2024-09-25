from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

from math import pi, sin, cos
#All imports above

class WalkingPanda(ShowBase):
    def __init__(self, no_rotate=False):
        ShowBase.__init__(self)

        #Load environment model
        self.scene = self.loader.loadModel("models/environment")
        #Reparent the model to render
        self.scene.reparentTo(self.render)

        #Apply scale and position transform the model

        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8,42,0)

        #Add the spinCameraTask procedure to the task manager to spin camera
        if no_rotate == False:
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        #Load and transform the panda actor
        self.pandaActor = Actor("models/panda-model",
        {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render) #Renders panda model

        #Loop walk
        self.pandaActor.loop("walk")

    def spinCameraTask(self, task):
        angleDegrees = task.time * 7.0
        angleRadians = angleDegrees * (pi/180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees,0,0)
        return Task.cont

