def resetCube():
    
    attr='GlobalMove.Reset_Cube'
    
    if cmds.getAttr(attr)==1:
        
        old=cmds.ls("*_Move_01_parentConstraint1")
        if not old:
            print("No existing parent constraint on joint")
        else:
            for each in old:
                cmds.delete(each)
        
        z=['CTRL_Front','CTRL_MidZ', 'CTRL_Back']
        y=['CTRL_Top','CTRL_MidY', 'CTRL_Bott']
        x=['CTRL_Side_L','CTRL_MidX', 'CTRL_Side_R']
        move=cmds.ls("*_Move_01")
        
        for i in z:
            cmds.setAttr(i+'.rotateZ',0)

        for i in y:
            cmds.setAttr(i+'.rotateY',0)

        for i in x:
            cmds.setAttr(i+'.rotateX',0)
        
        for i in move:
            cmds.setAttr(i+'.rotateZ',0)
            cmds.setAttr(i+'.rotateY',0)
            cmds.setAttr(i+'.rotateX',0)
            cmds.setAttr(i+'.translateZ',0)
            cmds.setAttr(i+'.translateY',0)
            cmds.setAttr(i+'.translateX',0)            
        
        cmds.setAttr('GlobalMove.Reset_Cube',0)
        

cmds.scriptJob(attributeChange=['GlobalMove.Reset_Cube',resetCube])
