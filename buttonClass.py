from graphics import *
#buttonClass.py

class Button:
    """A rectangular is a labeled rentnagle in a window. It is enabled or
disabled with the activate() and deactivate(0 methods. The is Clciked(pt)
method returns True if the btton in enabled and pt is inside it."""
    #first, set up the constructor method
    #this is automatically called each time the Button class is instantiatited
    def __init__(self,win,height, width, centerPt, words):
        """Creastes a rectangular button, where:
        win is the GraphWin object where the button will be drawn,
        height is an integer,
        width is an integer
        centerPt is a Point object the button will be centered on
        words is a string that will appear on the button"""
        x,y=centerPt.getX(),centerPt.getY()
        self.xmax= x + width/2
        self.xmin= x - width/2
        self.ymax= y + height/2
        self.ymin= y - height/2
        self.rect = Rectangle(Point(self.xmin,self.ymin),Point(self.xmax,self.ymax))
        self.rect.draw(win)
        self.rect.setFill("LightGray")
        self.label=Text(centerPt, words)
        self.label.draw(win)
        self.activate()
    # add more button methods here
    def isClicked(self, pt):
        """returns true if Point pt is inside"""
        if self.active and self.xmin <= pt.getX() <=self.xmax and self.ymin <= pt.getY() <= self.ymax:
            return True
        else:
            return False
    def activate(self):
        """Sets this button to active"""
        self.active = True
        self.rect.setWidth(2)
        self.label.setFill('black')

    def deactivate(self):
        self.active =False
        self.rect.setWidth(1)
        self.label.setFill("gray")

    def setLabel(self,newLabel):
        """Mutator method"""
        self.label.setText(newLabel)

    def getLabel(self):
        """Accessor method returning the words on the button"""
        return self.label.getText()

def main():
    gwin=GraphWin("button test",600,600)
    #instantiate the Button class
    #i.e. create a Button object called myButton
    myButton= Button(gwin,50,75,Point(300,300),"click me")
    #print(myButton.xmax)
    pt = gwin.getMouse()
    if myButton.isClicked(pt):
        print("You clicked the button")
    else:
        print("You did not click the button")

    myButton.deactivate()
    pt=gwin.getMouse()
    if myButton.isClicked(pt):
        print("You clicked the button")
    else:
        print("You did not click the button")
    myButton.setLabel("Dont click me")
    print(myButton.getLabel())

    #myButton.label
    
    gwin.getMouse()
    gwin.close()

    
if __name__ == '__main__':
    main()
    
    
    

                 
                 
