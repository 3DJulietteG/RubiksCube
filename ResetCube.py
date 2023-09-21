def resetCube():
    
    attr='GlobalMove.Reset_Cube'
    
    if cmds.getAttr(attr)==1:
        
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
        
        z=['CTRL_Front','CTRL_MidZ', 'CTRL_Back']
        y=['CTRL_Top','CTRL_MidY', 'CTRL_Bott']
        x=['CTRL_Side_L','CTRL_MidX', 'CTRL_Side_R']
        move=cmds.ls('*_Move*',exactType='transform')
        
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
        
        for i in move :
            if '_Move_01' in i:
                n=i.split('_Move')
                try:
                    cmds.parent(i,n[0]+'_Offset_01')
                except RuntimeError:
                    continue
                
        for i in move:
            if '_Move_01' in i:
                continue
            else:
                cmds.delete(i)
    
        cmds.setAttr('GlobalMove.Reset_Cube',0)
        

cmds.scriptJob(attributeChange=['GlobalMove.Reset_Cube',resetCube])
