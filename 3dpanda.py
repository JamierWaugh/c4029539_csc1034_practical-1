from direct.showbase.ShowBase import ShowBase #Status: Crash

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

app = MyApp()

app.run()