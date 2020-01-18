def func2(x , originx , originy , psizex ,psizey  ):
    nx = x.shape[0]
    ny = x.shape[1]
    for i in range(nx):
      for j in range(ny):
        if(x[i][j][0]>50):
          x[i][j][0]= 1
        else:
          x[i][j][0]=0
    x = x[:,:,0]
    mxx = 0 
    mxy = 0 
    mnx = 128
    mny = 128
    vis = np.full((x.shape[0],x.shape[1]),0)
    for i in range(0,x.shape[0]):
        for j in range(0,x.shape[1]):
          #print(i, j, x[i][j])
          if(vis[i][j]==1 or x[i][j]==0):
              continue
          tempi= []
          tempj = []
          tempi.append(i), tempj.append(j)
        
          #print(i,j)
          while(tempi!=[]):
              u = tempi.pop(0)
              v = tempj.pop(0)
              
              if(u<0 or v<0 or u>=nx or v>=ny or vis[u][v]==1 or x[u][v]==0):
                  continue
              #print(len(ax), u , v , x[u][v] )
              vis[u][v]=1 
              mxx = max(mxx,u)
              mnx = min(mnx,u)
              mxy = max(mxy,v)
              mny = min(mny,v)
              
              
              if(u+1<nx and v+1<ny and vis[u+1][v+1]==0 ):
                tempi.append(u+1)
                tempj.append(v+1)
              if(v+1<ny and vis[u][v+1]==0):
                tempi.append(u)
                tempj.append(v+1)
              if(u+1<nx and vis[u+1][v]==0):
                tempi.append(u+1)
                tempj.append(v)
              if(u-1>=0 and v+1<ny and vis[u-1][v+1]==0):
                tempi.append(u-1)
                tempj.append(v+1)
              if(u+1<nx and v-1>=0 and vis[u+1][v-1]==0):
                tempi.append(u+1)
                tempj.append(v-1)
              if(u-1>=0 and v-1>=0 and vis[u-1][v-1]==0):
                tempi.append(u-1)
                tempj.append(v-1)
              if(u-1>=0 and vis[u-1][v]==0):
                tempi.append(u-1)
                tempj.append(v)
              if(v-1>=0 and vis[u][v-1]==0):
                tempi.append(u)
                tempj.append(v+1)
          

    return(originx+mnx*psizex,originy+mny*psizey,originx+mxx*psizex,originy+mxy*psizey)
def func(x , originx , originy , psizex , psizey):
    ax = 0 
    ay = 0
    val = 0 
    nx = x.shape[0]
    ny = x.shape[0]
    for i in range(nx):
      for j in range(ny):
        if(x[i][j][0]>val):
          val = x[i][j][0]
          ax = i 
          ay = j
    return originx+(ax*psizex) , originy+(ay*psizey)
for i in range(34):
  shutil.copy("drive/My Drive/results/"+str(i)+"_img.png",str(i)+"_img.png")
  shutil.copy("drive/My Drive/results/"+str(i)+"_pred.png",str(i)+"_pred.png")
  shutil.copy("drive/My Drive/results/"+str(i)+"_true.png",str(i)+"_true.png")
X = []
Y = []
for i in range(34):
  x = cv2.imread(str(i)+"_pred.png")
  ax , ay = func(x,0,0,1,1)
  if(x[ax][ay][0]<100):
    X.append(-1)
    Y.append(-1)
    continue
  mnx,mny,mxx,mxy = func2(x,0,0,1,1)
  X.append([mnx,mxx])
  Y.append([mny,mxy])
length = []
xc = []
yc = []
for i in range(34):
  if(X[i]==-1):
    continue
  xc.append((X[i][0]+X[i][1])/2.0)
  yc.append((Y[i][0]+Y[i][1])/2.0)
  length.append((((X[i][1]-X[i][0])**2)+((Y[i][1]-Y[i][0])2))**(0.5))