class CHomoSapien(object):
    """This class defines the attributes and properties of a human being. This
    class will serve as a superclass/base class for a CPerson object class."""

    strMyType=""  #class Variable
    intCntr=0
    uiExit = 0

    def __init__(self, mySex, myLangauge, canSpeak, canWalk, canRun):
        self.strMySex=mySex           #Instance Variables
        self.strLanguage=myLangauge  #Instance Variables
        self.bCanSpeak=canSpeak       #Instance Variables
        self.bCanWalk=canWalk         #Instance Variables
        self.bCanRun = canRun         #Instance Variables
        
        self.intCntr += 1
        self.vSetMyType()

    def vSetMyType(self):
        if ((self.strMySex=="Male") or (self.strMySex=="male")):
            self.strMyType="man"
        elif self.strMySex=="Female":
            self.strMyType="woman"
        elif self.strMySex=="female":
            self.strMyType="woman"

    def strGetMySex(self):
        return self.strMyType

    def intGetNumHomoSapiens(self):
        return self.intCntr




