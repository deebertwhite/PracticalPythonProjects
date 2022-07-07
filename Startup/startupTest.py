import os
import glob

tempPath = r'C:\Users\JAMES~1.W_U\AppData\Local\Temp'

glob_wild_card = os.path.join(tempPath, "*.*")

for file in glob.glob(glob_wild_card):
   try:
      os.remove(file)
   except Exception as e:
      print(f"Error is {e} from {file}")