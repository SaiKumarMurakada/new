#creating folder structure
import os
path= 'C:\\Users\\SMURAKAD\\Desktop\\New folder\\new\\DWCode\\CareTeam'

  if not os.path.exists(path):
    os.makedirs(path)
 
 else:
    print("folder already exists.")
