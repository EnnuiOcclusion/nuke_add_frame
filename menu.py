import addFrameNow

toolbar = nuke.menu("Nodes")
eoMenu = toolbar.addMenu("EO Tools")

eoMenu.addCommand("Time/Add Frame Now", "addFrameNow.addFrameNow()", "n")
