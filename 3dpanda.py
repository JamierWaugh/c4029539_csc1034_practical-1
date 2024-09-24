from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        #Load environment model
        self.scene = self.loader.loadModel("models/environment")
        #Reparent the model to render
        self.scene.reparentTo(self.render)

        #Apply scale and position transform the model

        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8,42,0)



app = MyApp()

app.run() #Starts Panda screen