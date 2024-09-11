import os #for making folders and changing directories
import lxgrtgr as lxgr

#Test the tool
sample1 = lxgr.tag("This is a very important opportunity that only comes once in a lifetime.")
lxgr.printer(sample1) #by default, the format is: token_id,text,lemma,complexity_tag
lxgr.printer(sample1,verbose = True) #by default, the format is: token_id,text,lemma,complexity_tag

#Tag corpus files
## First, we will make sure that we are in the correct working directory (yours will look a bit different!)
os.chdir('/Users/kristopherkyle/Desktop/Programming/GitHub/LCR-ADS-Lab/LxGrTgr/workshop_files/')

## Then, we will make sure that we have a folder to put tagged files in
os.mkdir("MICUSP_sample_tagged/")

## Tag folder
lxgr.tagFolder("MICUSP_Sample/","MICUSP_sample_tagged/")

###########################
### Fix tag your files! ###
###########################

## Count tags
sampleCountDictionary = lxgr.countTagsFolder("MICUSP_sample_tagged/")
lxgr.writeCounts(sampleCountDictionary,"sampleMicuspOutputFile.txt")

os.mkdir("MICASE_sample_tagged/") #create a folder for processed files


