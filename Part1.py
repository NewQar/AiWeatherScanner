import os
import random
import shutil

dataOrgFolder = "C:\Users\User\Downloads\New folder\Training Image\Weather"
dataBaseFolder = "C:\Users\User\Downloads\New folder\Training Image\Trainings"

dataDirList = os.listdir(dataOrgFolder)
print(dataDirList)

splitSize = .85

# build files array

def split_data (SOURCE , TRAINING , VALIDATION , SPLIT_SIZE):
    files = []

    for filename in os.listdir(SOURCE) :
        file = SOURCE + filename
        print(file)
        if os.path.getsize(file) > 0 :
            files.append(filename)
        else:
            print(filename + " has 0 length , will not copy this file !!")

    # print number of files :
    print(len(files))


    trainLength = int(len(files) * SPLIT_SIZE )
    validLength = int( len(files) - trainLength )

    suffleDataSet = random.sample(files, len(files))

    trainingSet = suffleDataSet[0:trainLength]
    validSet = suffleDataSet[trainLength:]

    # copy the train images 
    for filename in trainingSet:
        f = SOURCE + filename
        dest = TRAINING + filename
        shutil.copy(f, dest) 
    
    # copy the valid images 
    for filename in validSet:
        f = SOURCE + filename
        dest = VALIDATION + filename
        shutil.copy(f, dest) 



cloudySourceFolder = "C:\Users\User\Downloads\New folder\Training Image\Weather\cloudy"
cloudyTrainFolder = "C:\Users\User\Downloads\New folder\Training Image\Train\cloudy"
cloudyValidFolder = "C:\Users\User\Downloads\New folder\Training Image\Valid\cloudy"

foggySourceFolder = "C:\Users\User\Downloads\New folder\Training Image\Weather\foggy"
foggyTrainFolder = "C:\Users\User\Downloads\New folder\Training Image\Train\foggy"
foggyValidFolder = "C:\Users\User\Downloads\New folder\Training Image\Valid\foggy"

rainyySourceFolder = "C:\Users\User\Downloads\New folder\Training Image\Weather\rainy"
rainyTrainFolder = "C:\Users\User\Downloads\New folder\Training Image\Train\rainy"
rainyValidFolder = "C:\Users\User\Downloads\New folder\Training Image\Valid\rainy"

shineSourceFolder = "C:\Users\User\Downloads\New folder\Training Image\Weather\shine"
shineTrainFolder = "C:\Users\User\Downloads\New folder\Training Image\Train\shine"
shineValidFolder = "C:\Users\User\Downloads\New folder\Training Image\Valid\shine"

sunriseSourceFolder = "C:\Users\User\Downloads\New folder\Training Image\Weather\sunrise"
sunriseTrainFolder = "C:\Users\User\Downloads\New folder\Training Image\Train\sunrise"
sunriseValidFolder = "C:\Users\User\Downloads\New folder\Training Image\Valid\sunrise"






split_data(cloudySourceFolder , cloudyTrainFolder , cloudyValidFolder , splitSize)
split_data(foggySourceFolder , foggyTrainFolder , foggyValidFolder , splitSize)
split_data(rainyySourceFolder , rainyTrainFolder , rainyValidFolder , splitSize)
split_data(shineSourceFolder , shineTrainFolder , shineValidFolder , splitSize)
split_data(sunriseSourceFolder , sunriseTrainFolder , sunriseValidFolder , splitSize)




# split_data ( "C:/Python-cannot-upload-to-GitHub/Weather/original-dataset/cloudy/", # dont forget the last " / "
#     "C:/Python-cannot-upload-to-GitHub/Weather/dataset/Train/cloudy/",
#     "C:/Python-cannot-upload-to-GitHub/Weather/dataset/validate/cloudy/",
#     splitSize)