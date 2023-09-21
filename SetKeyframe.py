import maya.cmds as cmds

#Key all controllers
ctrl=cmds.ls("CTRL_*",exactType='transform')
for i in ctrl:
    cmds.setKeyframe(i, shape=False)

#Detect joint in controllers hierarchy
bind=cmds.listRelatives("CTRLs_01",ad=True,f=False,type='joint')
move=[]
if bind:
    #Detect latest group move for each joint in controllers hierarchy
    for i in bind:
        ilist=[]
        current=[i]
        while 'CTRL_' not in current[0]:
            ilist.append(current[0])
            current=cmds.listRelatives(current[0],p=True)
        move.append(ilist[-1])
    #Move back joint to originals groups and create new move above precedent to recieve next transformation 
    for i in move:
        n=i.split('_Move')
        cmds.parent(i,n[0]+'_Offset_01')
        x=1
        while True:
            if cmds.objExists(str(n[0])+"_Move_0"+str(x)):
                x=x+1
                continue
            else:
                cmds.createNode('transform',n=str(n[0])+"_Move_0"+str(x))
                offset=cmds.ls(sl=True)
                cmds.matchTransform(offset,i)
                cmds.parent(offset,n[0]+'_Offset_01')
                cmds.makeIdentity(offset,apply=True)
                cmds.parent(i,offset)
                break
    #Key all existing moves            
    x=cmds.ls('*_Move*',exactType='transform')
    cmds.setKeyframe(x, shape=False)
else:
    #In case there is no joints in controller, detect the latest move and set keyframe
    touti=cmds.listRelatives("Joints_01",ad=True,f=False,type='joint')
    for i in touti:
        ilist=[]
        current=[i]
        while '_Offset' not in current[0]:
            ilist.append(current[0])
            current=cmds.listRelatives(current[0],p=True)
        move.append(ilist[-1])
     
    for i in move:
        cmds.setKeyframe(i, shape=False)
