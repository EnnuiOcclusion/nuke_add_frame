import nuke

def addFrameNow():
	AddFrame = nuke.nodes.addFrame(skipFrame = nuke.frame(), inputs = nuke.selectedNodes())
	nuke.connectViewer(0,AddFrame)
	AddFrame.selectOnly()
