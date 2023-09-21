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
                clist=[]
                current=cmds.listRelatives(good[1],p=True)
                while '_Move_' in current[0]:
                    clist.append(current[0])
                    current=cmds.listRelatives(current[0],p=True)
                move=clist[-1]
                joint.append(move)    
            else:
                continue
                
        old=cmds.listRelatives("CTRLs_01",ad=True,f=False,type='joint')
        move=[]
        if old:
            for i in old:
                ilist=[]
                current=[i]
                while 'CTRL_' not in current[0]:
                    ilist.append(current[0])
                    current=cmds.listRelatives(current[0],p=True)
                move.append(ilist[-1]) 
            for i in move:
                n=i.split('_Move')
                cmds.parent(i,n[0]+'_Offset_01')

        for i in joint:
            cmds.parent(i,selected[0])
        cmds.select(selected[0])
        
cmds.scriptJob(event=['SelectionChanged','rubikCube()']) 
#ResetCube
'''
cmds.scriptNode(st=2, bs=myCode.replace("'''","''" ), n='SN_RubikCube', stp='python')
