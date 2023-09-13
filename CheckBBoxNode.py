import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMpx

nodeName ="CheckBBoxNode"
nodeID = OpenMaya.MTypeId(0x100fff)

class CheckBBoxNode(OpenMayaMpx.MPxNode):
   
    inBBMin = OpenMaya.MObject()
    inBBMax = OpenMaya.MObject()
    inPosition = OpenMaya.MObject()
    outCondition = OpenMaya.MObject() 
    
    def __init__(self):
        OpenMayaMpx.MPxNode.__init__(self)
    
    def compute(self,plug,dataBlock):

        if plug==CheckBBoxNode.outCondition:
            
            dataHandleBBMin = dataBlock.inputValue(CheckBBoxNode.inBBMin)
            dataHandleBBMax = dataBlock.inputValue(CheckBBoxNode.inBBMax)
            dataHandlePosition = dataBlock.inputValue(CheckBBoxNode.inPosition)
            
            BBMinVal = dataHandleBBMin.asFloat3()
            BBMaxVal = dataHandleBBMax.asFloat3()
            inPositionVal = dataHandlePosition.asFloat3()
        
            if BBMinVal[0]<=inPositionVal[0]<=BBMaxVal[0]:
                if BBMinVal[1]<=inPositionVal[1]<=BBMaxVal[1]:
                    if BBMinVal[2]<=inPositionVal[2]<=BBMaxVal[2]:
                        outCondition=1
                    else:
                        outCondition=0
                else:
                    outCondition=0
            else:
                outCondition=0
            
            dataHandleCondition = dataBlock.outputValue(CheckBBoxNode.outCondition)
            dataHandleCondition.setFloat(outCondition)
            
            dataBlock.setClean(plug)
            
        else:
            return OpenMaya.kUnknownParameter
    
def nodeCreator():
    return OpenMayaMpx.asMPxPtr(CheckBBoxNode())

def nodeInitializer():
    
    mFnAttr=OpenMaya.MFnNumericAttribute()
    
    #Create attributes
    CheckBBoxNode.inBBMin = mFnAttr.create("BoundingBoxMin", "BBMin", OpenMaya.MFnNumericData.k3Float, 0.0)
    mFnAttr.setReadable(True)
    mFnAttr.setWritable(True)
    mFnAttr.setStorable(True)
    
    CheckBBoxNode.inBBMax = mFnAttr.create("BoundingBoxMax", "BBMax", OpenMaya.MFnNumericData.k3Float, 0.0)
    mFnAttr.setReadable(True)
    mFnAttr.setWritable(True)
    mFnAttr.setStorable(True)    
    
    CheckBBoxNode.inPosition = mFnAttr.create("Position", "p", OpenMaya.MFnNumericData.k3Float, 0.0)
    mFnAttr.setReadable(True)
    mFnAttr.setWritable(True)
    mFnAttr.setStorable(True)

    CheckBBoxNode.outCondition = mFnAttr.create("Result", "r", OpenMaya.MFnNumericData.kFloat)
    mFnAttr.setReadable(True)
    mFnAttr.setWritable(False)
    mFnAttr.setStorable(False)  
    
    CheckBBoxNode.addAttribute(CheckBBoxNode.inBBMin)
    CheckBBoxNode.addAttribute(CheckBBoxNode.inBBMax)
    CheckBBoxNode.addAttribute(CheckBBoxNode.inPosition)
    CheckBBoxNode.addAttribute(CheckBBoxNode.outCondition)
    
    CheckBBoxNode.attributeAffects(CheckBBoxNode.inBBMax, CheckBBoxNode.outCondition)
    CheckBBoxNode.attributeAffects(CheckBBoxNode.inBBMin, CheckBBoxNode.outCondition)
    CheckBBoxNode.attributeAffects(CheckBBoxNode.inPosition, CheckBBoxNode.outCondition)
    

def initializePlugin(mobject):
    mplugin = OpenMayaMpx.MFnPlugin(mobject)
    try:
        mplugin.registerNode(nodeName, nodeID, nodeCreator, nodeInitializer)
    except:
        sys.stderr.write("Failed to register command: %s\n" % nodeName)
        
def uninitializePlugin(mobject):
    mplugin = OpenMayaMpx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode(nodeName, nodeID, nodeCreator, nodeInitializer)
    except:
        sys.stderr.write("Failed to register command: %s\n" % nodeName)
    