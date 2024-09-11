import os #for making folders and changing directories
import lxgrtgr as lxgr

#Test the tool
sample1 = lxgr.tag("This is a very important opportunity that only comes once in a lifetime.")
lxgr.printer(sample1) #by default, the format is: token_id,text,lemma,complexity_tag
#lxgr.printer(sample1,verbose = True) #by default, the format is: token_id,text,lemma,complexity_tag

## Output:
# #sentid = 0
# 0 This this None
# 1 is be None
# 2 a a None
# 3 very very rb+jjrbmod
# 4 important important attr+npremod
# 5 opportunity opportunity None
# 6 that that None
# 7 only only rb+advl
# 8 comes come finitecls+rel
# 9 once once rb+advl
# 10 in in None
# 11 a a None
# 12 lifetime lifetime None
# 13 . . None

#Tag MICUSP files
## First, we will make sure that we are in the correct working directory (yours will look a bit different!)
os.chdir('/Users/kristopherkyle/Desktop/Programming/GitHub/kristopherkyle/AACL2024_Workshop/')

## Then, we will make sure that we have a folder to put tagged MICUSP files in
os.mkdir("MICUSP_sample_tagged/")

## Tag files in MICUSP folder
lxgr.tagFolder("MICUSP_Sample/","MICUSP_sample_tagged/") #12 seconds on my computer

###########################
### Fix tag your files! ###
###########################

## Count tags
micuspDictionary = lxgr.countTagsFolder("MICUSP_sample_tagged/")
lxgr.writeCounts(micuspDictionary,"sampleMicuspOutputFile.txt")

# Tag MICASE files
## First, we will make sure that we are in the correct working directory (yours will look a bit different!)
os.chdir('/Users/kristopherkyle/Desktop/Programming/GitHub/kristopherkyle/AACL2024_Workshop/')

## Then, we will make sure that we have a folder to put tagged MICUSP files in
os.mkdir("MICASE_sample_tagged/")

## Tag files in MICUSP folder
lxgr.tagFolder("MICASE_Sample/","MICASE_sample_tagged/") #40 seconds on my computer

###########################
### Fix tag your files! ###
###########################

## Count tags
micaseDictionary = lxgr.countTagsFolder("MICASE_sample_tagged/")
lxgr.writeCounts(micaseDictionary,"sampleMicaseOutputFile.txt")

################################################
### Conduct awesome, world-changing analyses ###
################################################


