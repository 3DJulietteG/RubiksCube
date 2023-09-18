myCode='''

import maya.cmds as cmds

def rubikCube():
    
    selected=[]
    selected=cmds.ls(sl=True, tr=True)

    if selected and "CTRL_" in selected[0] :
        temp=selected[0].split("CTRL_")
        part=temp[1]
        lst=cmds.ls("Check_Box_{}*".format(part))
        joint=[]
        joint.clear()
        
        for x in range(0,len(lst)):
            d=cmds.getAttr(lst[x]+'.Result')
            if d==1 :
                good=lst[x].split("_to_")
                move=str(good[1]+"_Move_01")
                joint.append(move)    
            else:
                continue
                
        old=cmds.ls("*_Move_01_parentConstraint1")
        if not old:
            print("No existing parent constraint on joint")
        else:
            for each in old:
                cmds.delete(each)
            
        for i in joint:
            cmds.parentConstraint(selected[0], i, mo=True)


cmds.scriptJob(attributeChange=['GlobalMove.Reset_Cube',resetCube])
#resetCube script
'''
cmds.scriptNode(st=2, bs=myCode.replace("'''","''" ), n='SN_RubikCube', stp='python')
