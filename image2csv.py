def func(x , originx , originy , psizex , psizey):
    ax = 0 
    ay = 0
    val = 0 
    nx = x.shape[0]
    ny = x.shape[0]
    for i in range(nx):
      for j in range(ny):
        if(x[i][j][2]>val):
          val = x[i][j][2]
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
  x = cv2.imread(str(i)+"_true.png")
  ax , ay = func(x,0,0,1,1)
  if(x[ax][ay][2]>100):
    X.append(ax)
    Y.append(ay)
  else:
    X.append(-1)
    Y.append(-1)

    