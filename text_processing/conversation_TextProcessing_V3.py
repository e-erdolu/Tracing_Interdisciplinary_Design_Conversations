import string
import copy
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
import re
import pandas as pd
import streamlit as st
import altair as alt
import json

##################################################################
## Text processing and extracting data: Part 1
##################################################################

f = open("Data_Final_2.txt", encoding="utf8")
raw = f.read()

actor1 = "Paul_Goldberger"
actor2 = "Tony_Fadell"
actor3 = "Rem_Koolhaas"

## List of words with no punctuation but with stamps
tokenizer = nltk.RegexpTokenizer(r"\w+")
wordsNoPunct = tokenizer.tokenize(raw)
# print(wordsNoPunct, len(wordsNoPunct))
# print("BREAK")

f_1 = open("Data_8_2.txt", encoding="utf8")
part_8 = f_1.read()
wordsNoPunct_8 = tokenizer.tokenize(part_8)
# print(wordsNoPunct_8, len(wordsNoPunct_8))
# print("BREAK")

f_2 = open("Data_16_2.txt", encoding="utf8")
part_16 = f_2.read()
wordsNoPunct_16 = tokenizer.tokenize(part_16)
# print(wordsNoPunct_16, len(wordsNoPunct_16))
# print("BREAK")

f_3 = open("Data_24_2.txt", encoding="utf8")
part_24 = f_3.read()
wordsNoPunct_24 = tokenizer.tokenize(part_24)
# print(wordsNoPunct_24, len(wordsNoPunct_24))
# print("BREAK")

f_4 = open("Data_32_2.txt", encoding="utf8")
part_32 = f_4.read()
wordsNoPunct_32 = tokenizer.tokenize(part_32)
# print(wordsNoPunct_32, len(wordsNoPunct_32))
# print("BREAK")

# f_5 = open("Data_40.txt", encoding="utf8")
# part_40 = f_5.read()
# wordsNoPunct_40 = tokenizer.tokenize(part_40)
# print(wordsNoPunct_40, len(wordsNoPunct_40))
# print("BREAK")


## List of words with punctuation and stamps
wordsWithPunct = TreebankWordTokenizer().tokenize(raw)
#print(wordsWithPunct, len(wordsWithPunct))
#print("BREAK")

## Set of stop words
stopWords = {'been', 'some', 'above', "shan't", 'up', 'whom', 'o',\
             'why', 'under', 'if', 'isn', 'on', 'after', 'will', \
             'during', 'before', 'myself', 'had', 'an', 'nor', \
             'from', 'weren', 'yourselves', 'can', "you'd", 'what', \
             'didn', 'there', "doesn't", 'more', "that'll", 'don', \
             'down', 'all', 'once', "wasn't", 'it', 'him', 'did', \
             'yourself', 'does', 'she', "don't", "aren't", "hasn't", \
             'now', 'doing', 'about', 'no', "you've", 'any', 'we', \
             'until', 're', 'have', 'very', 'was', 'm', 'am', 'when', \
             'again', 't', 'ours', "weren't", 'hasn', 'out', 'here', \
             "should've", 'their', "she's", 'not', "won't", 'who', \
             'won', 'yours', 'be', 'at', 'few', 'are', 's', 've', \
             'to', 'couldn', "hadn't", 'shan', 'wasn', 'how', 'than', \
             "needn't", 'doesn', 'these', 'other', 'hers', 'further', \
             'mustn', 'and', 'has', 'itself', 'themselves', "wouldn't", \
             'aren', "shouldn't", 'where', 'should', "isn't", 'most', \
             'same', "haven't", 'her', 'just', 'do', "couldn't", "mustn't", \
             'theirs', 'they', 'such', 'haven', 'having', 'you', 'mightn', \
             'but', 'were', 'against', "mightn't", 'himself', 'hadn', 'a', \
             'below', 'shouldn', 'those', 'herself', 'too', 'this', 'that', \
             'our', 'the', 'with', 'then', 'is', 'in', 'each', 'as', 'by', \
             'he', 'ourselves', 'wouldn', 'both', 'ain', 'only', 'so', 'into', \
             "you'll", 'while', 'd', 'i', 'needn', 'which', 'them', 'over', \
             "didn't", 'own', 'll', 'y', "you're", 'being', 'your', 'its', \
             'or', 'because', 'off', 'between', 'his', 'me', 'through', \
             "it's", 'for', 'ma', 'of', 'my', 'I', 'could', 'also', 'like',\
             'among', 'since', 'maybe', 'may', 'might', 'mightn', "mightn't", \
             'yeah', 'yes', 'wow', 'cuz', 'ok', 'sure', 'well', 'kind', 'would'}
#set(stopwords.words('english'))
#print(stopWords)
#print("BREAK")

nonDoubDisciplinary = {'designs', 'designing', 'design', 'designed', 'produce', \
                       'produced', 'production', 'producing', 'create', 'created', \
                       'creating', 'research', 'develop', 'development', 'public', \
                       'state', 'change', 'changes', 'changed', 'improving', 'improve', \
                       'improvement', 'comfort', 'discomfort', 'security', 'future', \
                       'environments', 'environmental', 'environment', 'comfy', 'secure', \
                       'dystopic', 'utopia', 'utopian', 'cultural', 'social', 'controls', \
                       'control', 'controlling', 'learn', 'learned', 'adapt', 'demographics', \
                       'connect', 'connecting', 'connections',  'communicate', 'communicates', \
                       'communicating', 'culture', 'cultures', 'governments', 'government', \
                       'transgression', 'transgressing', 'conflict', 'transparencies', \
                       'transparent', 'opaque', 'untraceable', 'intelligent', 'program', \
                       'able', 'intelligence', 'sustainability', 'generation', 'generations', \
                       'value', 'values', 'climates', 'protect', 'cooling', 'heating', 'heat', \
                       'heated', 'carbon', 'footprint', 'energy', 'supply', 'costs', 'save', \
                       'saved', 'savings', 'consumption', 'consumed', 'consume',  'market', \
                       'management', 'brand', 'industrial', 'commercial', 'interface', 'interfaces', \
                       'wasting', 'history', 'histories', 'vision', 'pleasurable', 'nonpleasurable', \
                       'knob''physical', 'physicality', 'forces', 'creators', 'innovators', \
                       'innovation', 'tangent', 'retrofitted', 'plumbing', 'phase', 'modernized', \
                       'designers', 'equipment', 'manufacturers', 'performance', 'profit', 'society', \
                       'community', 'customers', 'saves', 'client', 'clients', 'manufacturing', \
                       'codes', 'jurisdiction', 'governmental', 'legislation', 'prototypes', \
                       'context', 'programs', 'test', 'tested', 'aesthetic', 'aesthetics', \
                       'political', 'economic', 'ideological', 'model', 'dimensions', 'composed', \
                       'coherent', 'proportions', 'organism', 'ubiquitous', 'project', 'projects', \
                       'correlation', 'globalization', 'mobilization', 'paradigms', 'territories', \
                       'Western', 'formula', 'literature',  'modern', 'corruption', 'constructed', \
                       'evolution', 'risk', 'iterate', 'renewable', 'policies', 'standard', \
                       'efficiency', 'infrastructure', 'invest', 'investment', 'decorated', \
                       'aluminum', 'norm', 'variation', 'creativity', 'memory', 'memories', \
                       'psyche', 'inventorizing', 'appetite', 'panels', 'conform', 'conformist', \
                       'capsules', 'existential', 'traffic', 'freedom', 'commission', 'construction', \
                       'contractor', 'contractors', 'electrical', 'power', 'powers',  'electricity'}
# print(nonDoubDisciplinary)
# print("BREAK")

disciplinary_1 = {'architecture', 'OMA', 'curator', 'biennial', 'architect', 'architectural', \
                  'biennials', 'architects', 'elements', 'floor', 'door', 'wall', 'ramp', 'buildings', \
                  'modernization', 'pavilions', 'pavilion', 'urban', 'planning', 'building', 'storeys', \
                  'shelves', 'space', 'fireplace', 'fireplaces', 'room', 'house', 'dwelling', 'bed', \
                  'bath', 'houses', 'forms', 'built', 'size', 'apartment', 'kitchen', 'dweller', \
                  'home', 'bedroom', 'spaces', 'town', 'green', 'suburbia', 'apartments', 'city', \
                  'agglomerations', 'places', 'inhabitable', 'units', 'build', 'structures', 'dwell', \
                  'housing', 'urbanism', 'cities', 'urbanistic', 'office', 'homes', 'element', 'residential', \
                  'ceiling', 'curtain', 'tower', 'rooms', 'rebuilding', 'plane', 'handicapped', 'access', \
                  'plan', 'library', 'biennale', 'walls', 'structure', 'homeowners', 'prefab', 'roofs', \
                  'megacity', 'megacities', 'scale', 'buttress', 'buttresses', 'Gothic', 'cathedral', \
                  'Victorian', 'windows', 'window', 'balcony'}
# print(disciplinary_1)
# print("BREAK")

disciplinary_2 = {'technology', 'iPod', 'Apple', 'player', 'Nest', 'products', 'sensor', 'learning', 'devices', \
                  'thermostats', 'Google', 'thermostat', 'system', 'technologies', 'equipped', 'object', \
                  'information', 'cells', 'instant', 'device', 'digital', 'Silicon', 'Valley', 'technophoria', \
                  'technophobia', 'informational', 'cars', 'data', 'car', 'machines', 'technological', 'laptop', \
                  'mobile', 'phones', 'Twitter', 'iPhone', 'simulate', 'smartphone', 'product', 'vehicle', 'dial', \
                  'temperature', 'VCR', 'manual', 'servers', 'tablet', 'computer', 'feedback', 'services', 'stored', \
                  'ads', 'loop', 'programmer', 'functionality', 'store', 'objects', 'smartphones', 'connectivity', \
                  'telephones', 'epsilon', 'algorithms', 'TVs', 'screen', 'technoutopian', 'button', 'Microsoft', \
                  'Windows', 'ID', 'IT', 'consumer', 'personal', 'invention', 'application', 'technophobe', 'inventor', \
                  'iPhones', 'industry', 'installed', 'privacy', 'connected', 'transparency', 'tech', 'computing', \
                  'sensors', 'systems', 'inventions', 'reinvent', 'honeywell', 'wired', 'technical', 'beta', \
                  'engineering', 'technologists', 'calculate', 'calculated', 'computers', 'computer', 'software', \
                  'phone', 'charged', 'transmitting', 'appliances', 'wiring', 'labs', 'TV', 'toaster', 'programmed', \
                  'machine', 'Internet', 'robots', 'steering', 'wheels', 'robotic', 'kilowatt', 'volts', 'hertz', \
                  'current', 'voltage', 'DC'}
# print(disciplinary_2)
# print("BREAK")


## Function that gives the list of words with no punctuation and no stamps
def removeStamps(raw):
    rawSplit = raw.split()

    for word in rawSplit:
        matched1 = re.match(r"\((\d{2}:\d{2})\)", word)
        matched2 = re.match(r"\((\d{2}:\d{2}:\d{2})\)", word)
        matched3 = re.match(r"\[crosstalk", word)
        is_match1 = bool(matched1)
        is_match2 = bool(matched2)
        is_match3 = bool(matched3)
        if is_match1 == True or is_match2 == True or is_match3 == True:
            rawSplit.remove(word)

    for word in rawSplit:
        matched4 = re.match(r"\d{2}:\d{2}:\d{2}\]", word)
        is_match4 = bool(matched4)
        if is_match4 == True:
            rawSplit.remove(word)

    rawJoined = " ".join(rawSplit)
    wordsNoPunctNoStamp = tokenizer.tokenize(rawJoined)

    return wordsNoPunctNoStamp  #, len(wordsNoPunctNoStamp)


## Function that creates an actorInfo dictionary and adds actors' names
## --- { index: [actorName]
def addActors(words): ## wordsNoPunctNoStamp
    actorInfo = {}
    index = -1

    for i in range(len(words) - 1):
        if words[i] == actor1:
            index += 1
            actorInfoList = []
            actorInfoList.append(actor1)
            actorInfo[index] = actorInfoList
        elif words[i] == actor2:
            index += 1
            actorInfoList = []
            actorInfoList.append(actor2)
            actorInfo[index] = actorInfoList
        elif words[i] == actor3:
            index += 1
            actorInfoList = []
            actorInfoList.append(actor3)
            actorInfo[index] = actorInfoList

    return actorInfo


## Function that adds timeStamps to the dictionary
## --- { index: [actorName, timeStamps]
def addTimeStamps(raw, dic): ## actorInfo
    rawSplit = raw.split()
    index = -1

    for word in rawSplit:
        matched1 = re.match(r"\((\d{2}:\d{2})\)", word)
        matched2 = re.match(r"\((\d{2}:\d{2}:\d{2})\)", word)
        is_match1 = bool(matched1)
        is_match2 = bool(matched2)
        if is_match1 == True or is_match2 == True:
            index += 1
            timeStampNoParenth = word.replace("(", "").replace(")", "")
            dic[index].append(timeStampNoParenth)

    return dic


## Function that adds numWords to the dictionary
## --- { index: [actorName, timeStamps, numWords]
def addNumWordsByActor(words, dic):
    index = -1
    countActor1 = 0
    countActor2 = 0
    countActor3 = 0
    actor1_On = False
    actor2_On = False
    actor3_On = False

    for word in words:
        ## Capturing actors' names in the corpus
        if word == actor1:
            index += 1
            actor1_On = True
            actor2_On = False
            actor3_On = False
        elif word == actor2:
            index += 1
            actor1_On = False
            actor2_On = True
            actor3_On = False
        elif word == actor3:
            index += 1
            actor1_On = False
            actor2_On = False
            actor3_On = True

        ## Counting words in actors' phrases and add numWords in the dictionary
        if actor1_On == True and word != actor1:
            countActor1 += 1
            if len(dic[index]) == 2:
                dic[index].append(countActor1)
            elif len(dic[index]) == 3:
                dic[index][2] = countActor1
        elif actor2_On == True and word != actor2:
            countActor2 += 1
            if len(dic[index]) == 2:
                dic[index].append(countActor2)
            elif len(dic[index]) == 3:
                dic[index][2] = countActor2
        elif actor3_On == True:
            if word != actor3:
                countActor3 += 1
            if len(dic[index]) == 2:
                    dic[index].append(countActor3)
            if len(dic[index]) == 3:
                dic[index][2] = countActor3

    return dic


## Function that adds numContentfulWords to the dictionary
## --- { index: [actorName, timeStamps, numWords, numContentfulWords]
def addNumContentfulWordsByActor(words, dic):
    index = -1
    countActor1 = 0
    countActor2 = 0
    countActor3 = 0
    actor1_On = False
    actor2_On = False
    actor3_On = False

    for word in words:
        ## Capturing actors' names in the corpus
        if word == actor1:
            index += 1
            actor1_On = True
            actor2_On = False
            actor3_On = False
        elif word == actor2:
            index += 1
            actor1_On = False
            actor2_On = True
            actor3_On = False
        elif word == actor3:
            index += 1
            actor1_On = False
            actor2_On = False
            actor3_On = True

        ## Counting words in actors' phrases and add numWords in the dictionary
        if actor1_On == True and word != actor1:
            if word not in stopWords:
                countActor1 += 1
                if len(dic[index]) == 3:
                    dic[index].append(countActor1)
                elif len(dic[index]) == 4:
                    dic[index][3] = countActor1
            elif word in stopWords:
                if len(dic[index]) == 3:
                    dic[index].append(countActor1)
                elif len(dic[index]) == 4:
                    dic[index][3] = countActor1

        elif actor2_On == True and word != actor2:
            if word not in stopWords:
                countActor2 += 1
                if len(dic[index]) == 3:
                    dic[index].append(countActor2)
                elif len(dic[index]) == 4:
                    dic[index][3] = countActor2
            elif word in stopWords:
                if len(dic[index]) == 3:
                    dic[index].append(countActor2)
                elif len(dic[index]) == 4:
                    dic[index][3] = countActor2

        elif actor3_On == True and word != actor3:
            if word not in stopWords:
                countActor3 += 1
                if len(dic[index]) == 3:
                    dic[index].append(countActor3)
                elif len(dic[index]) == 4:
                    dic[index][3] = countActor3
            elif word in stopWords:
                if len(dic[index]) == 3:
                    dic[index].append(countActor3)
                elif len(dic[index]) == 4:
                    dic[index][3] = countActor3

    return dic


## Converts the dictionary for dataframe, adds a column of indeces (for slider)
def dictConverter(dic):
    dicNew = {}
    indexList = []
    actorNameList = []
    timeStampList = []
    numWordsList = []
    numContentfulWordsList = []

    for i in range(len(dic)):
        index = i
        indexList.append(index)
        dicNew["OrderOfSpeech"] = indexList

        actorName = dic[i][0]
        if actorName == actor1:
            actorName = "Niklas Maak"
            actorNameList.append(actorName)
            dicNew["Actor"] = actorNameList
        elif actorName == actor2:
            actorName = "Tony Fadell"
            actorNameList.append(actorName)
            dicNew["Actor"] = actorNameList
        elif actorName == actor3:
            actorName = "Rem Koolhaas"
            actorNameList.append(actorName)
            dicNew["Actor"] = actorNameList

        timeStamp = dic[i][1]
        timeStampList.append(timeStamp)
        dicNew["Time"] = timeStampList

        numWordsByActor = dic[i][2]
        numWordsList.append(numWordsByActor)
        dicNew["NumberOfWords"] = numWordsList

        numContentfulWordsByActor = dic[i][3]
        numContentfulWordsList.append(numContentfulWordsByActor)
        dicNew["NumberOfContentfulWords"] = numContentfulWordsList

    return dicNew


## Function to create nonStopWordListsByActor
## Creates a list for each actor of the nonstop words used
def makeNonStopWordListsByActor(words):
    wordList1 = []
    wordList2 = []
    wordList3 = []
    actor1_On = False
    actor2_On = False
    actor3_On = False

    for word in words:
        ## Capturing actors' name in the corpus
        if word == actor1:
            actor1_On = True
            actor2_On = False
            actor3_On = False
        elif word == actor2:
            actor1_On = False
            actor2_On = True
            actor3_On = False
        elif word == actor3:
            actor1_On = False
            actor2_On = False
            actor3_On = True

        ## Words in actors' phrases
        if actor1_On == True and word != actor1 and word not in stopWords:
            wordList1.append(word)
        elif actor2_On == True and word != actor2 and word not in stopWords:
            wordList2.append(word)
        elif actor3_On == True and word != actor3 and word not in stopWords:
            wordList3.append(word)

    return wordList1, wordList2, wordList3


## Function to create stopWordListsByActor
## Creates a list for each actor of the stop words used
def makeStopWordListsByActor(words):
    wordList1 = []
    wordList2 = []
    wordList3 = []
    actor1_On = False
    actor2_On = False
    actor3_On = False

    for word in words:
        ## Capturing actors' name in the corpus
        if word == actor1:
            actor1_On = True
            actor2_On = False
            actor3_On = False
        elif word == actor2:
            actor1_On = False
            actor2_On = True
            actor3_On = False
        elif word == actor3:
            actor1_On = False
            actor2_On = False
            actor3_On = True

        ## Words in actors' phrases
        if actor1_On == True and word != actor1 and word in stopWords:
            wordList1.append(word)
        elif actor2_On == True and word != actor2 and word in stopWords:
            wordList2.append(word)
        elif actor3_On == True and word != actor3 and word in stopWords:
            wordList3.append(word)

    return wordList1, wordList2, wordList3


## Function to create wordListsByActor
## Creates a list for each actor of all the words used
def makeWordListsByActor(words):
    wordList1 = []
    wordList2 = []
    wordList3 = []
    actor1_On = False
    actor2_On = False
    actor3_On = False

    for word in words:
        ## Capturing actors' name in the corpus
        if word == actor1:
            actor1_On = True
            actor2_On = False
            actor3_On = False
        elif word == actor2:
            actor1_On = False
            actor2_On = True
            actor3_On = False
        elif word == actor3:
            actor1_On = False
            actor2_On = False
            actor3_On = True

        ## Words in actors' phrases
        if actor1_On == True and word != actor1:
            wordList1.append(word)
        elif actor2_On == True and word != actor2:
            wordList2.append(word)
        elif actor3_On == True and word != actor3:
            wordList3.append(word)

    return wordList1, wordList2, wordList3

## Function to create wordListsByActor
## Creates a list for each actor of all the words used
def makeDiscpWordListsByActor(words):
    wordList1 = []
    wordList2 = []
    wordList3 = []
    actor1_On = False
    actor2_On = False
    actor3_On = False

    for word in words:
        ## Capturing actors' name in the corpus
        if word == actor1:
            actor1_On = True
            actor2_On = False
            actor3_On = False
        elif word == actor2:
            actor1_On = False
            actor2_On = True
            actor3_On = False
        elif word == actor3:
            actor1_On = False
            actor2_On = False
            actor3_On = True

        ## Words in actors' phrases
        if actor1_On == True:
            if word in nonDoubDisciplinary \
                or word in disciplinary_1 \
                or word in disciplinary_2 :
                wordList1.append(word)
        elif actor2_On == True:
            if word in nonDoubDisciplinary \
                or word in disciplinary_1 \
                or word in disciplinary_2 :
                wordList2.append(word)
        elif actor3_On == True:
            if word in nonDoubDisciplinary \
                or word in disciplinary_1 \
                or word in disciplinary_2 :
                wordList3.append(word)

    return wordList1, wordList2, wordList3


## Function to measure the lengths of nonStopWordListsByActor
def lengthMeasurer(lst):
    return len(lst[0]), len(lst[1]), len(lst[2])


## Function to create a dictonary for each actor that contains {word: number of occurrence}
## These three dictionaries are later used to create the dictForJSON
def findWordFrequencyByActor(lst):
    dictWordCount = {}

    for word in lst:
        if word in dictWordCount:
            dictWordCount[word] += 1
        else:
            dictWordCount[word] = 1

    return dictWordCount

def countDisciplinaryWordsByActor(lst):
    countDiscp1 = 0
    countDiscp2 = 0
    countIntDiscp = 0
    countNone = 0
    listCounted = []

    for word in lst:
        if word in disciplinary_1 and word not in listCounted:
             countDiscp1 += 1
             listCounted.append(word)
        elif word in disciplinary_2 and word not in listCounted:
             countDiscp2 += 1
             listCounted.append(word)
        elif word in nonDoubDisciplinary and word not in listCounted:
             countIntDiscp += 1
             listCounted.append(word)
        else:
            if word not in listCounted:
                countNone += 1
                listCounted.append(word)

    return countDiscp1, countDiscp2, countIntDiscp, countNone 

def filterDict(dic, num):
    newDict = {}

    for word in dic:
        if dic[word] > num:
            newDict[word] = dic[word]

    return newDict


## Function to create the dictonary from the actor wordFrequency dictionaries
## This dictionary gets converted to JSON
## to create all actors and all nonstop words network
# def createDictForJson(dic, dic1, dic2):
#     dictForJson = {}
#     listOfNodes = []
#     listOfLinks = []
#     listOfNodes1 = []
#     listOfLinks1 = []
#     listOfNodes2 = []
#     listOfLinks2 = []

#     listOfNodes.append({"id": "Maak", "group": 1})

#     for key in dic:
#         dictOfEachNode = {}
#         dictOfEachNode["id"] = key
#         dictOfEachNode["group"] = 2
#         listOfNodes.append(dictOfEachNode)

#         dictOfEachLink = {}
#         dictOfEachLink["source"] = "Maak"
#         dictOfEachLink["target"] = key
#         dictOfEachLink["value"] = dic[key]
#         listOfLinks.append(dictOfEachLink)

#     dictForJson["nodes"] = listOfNodes
#     dictForJson["links"] = listOfLinks

#     listOfNodes.append({"id": "Fadell", "group": 1})

#     for key in dic1:
#         dictOfEachNode = {}
#         dictOfEachNode["id"] = key
#         dictOfEachNode["group"] = 2
#         if dictOfEachNode not in dictForJson["nodes"]:
#             listOfNodes1.append(dictOfEachNode)

#         dictOfEachLink = {}
#         dictOfEachLink["source"] = "Fadell"
#         dictOfEachLink["target"] = key
#         dictOfEachLink["value"] = dic1[key]
#         listOfLinks1.append(dictOfEachLink)

#     dictForJson["nodes"] += listOfNodes1
#     dictForJson["links"] += listOfLinks1

#     listOfNodes.append({"id": "Koolhaas", "group": 1})

#     for key in dic2:
#         dictOfEachNode = {}
#         dictOfEachNode["id"] = key
#         dictOfEachNode["group"] = 2
#         if dictOfEachNode not in dictForJson["nodes"]:
#             listOfNodes2.append(dictOfEachNode)

#         dictOfEachLink = {}
#         dictOfEachLink["source"] = "Koolhaas"
#         dictOfEachLink["target"] = key
#         dictOfEachLink["value"] = dic2[key]
#         listOfLinks2.append(dictOfEachLink)

#     dictForJson["nodes"] += listOfNodes2
#     dictForJson["links"] += listOfLinks2

#     return dictForJson


def createDictForJson(dic, dic1, dic2):
    dictForJson = {}
    listOfNodes = []
    listOfLinks = []
    listOfNodes1 = []
    listOfLinks1 = []
    listOfNodes2 = []
    listOfLinks2 = []

    listOfNodes.append({"id": "Goldberger", "group": 1, "colVal": 5})

    for key in dic:
        dictOfEachNode = {}
        dictOfEachNode["id"] = key
        dictOfEachNode["group"] = 2

        if key in disciplinary_1:
            dictOfEachNode["colVal"] = 1
        elif key in disciplinary_2:
            dictOfEachNode["colVal"] = 2
        elif key in nonDoubDisciplinary:
            dictOfEachNode["colVal"] = 3
        else:
            dictOfEachNode["colVal"] = 4
        
        listOfNodes.append(dictOfEachNode)

        dictOfEachLink = {}
        dictOfEachLink["source"] = "Goldberger"
        dictOfEachLink["target"] = key
        dictOfEachLink["value"] = dic[key]
        listOfLinks.append(dictOfEachLink)

    dictForJson["nodes"] = listOfNodes
    dictForJson["links"] = listOfLinks

    listOfNodes.append({"id": "Fadell", "group": 1, "colVal": 5})

    for key in dic1:
        dictOfEachNode = {}
        dictOfEachNode["id"] = key
        dictOfEachNode["group"] = 2

        if key in disciplinary_1:
            dictOfEachNode["colVal"] = 1
        elif key in disciplinary_2:
            dictOfEachNode["colVal"] = 2
        elif key in nonDoubDisciplinary:
            dictOfEachNode["colVal"] = 3
        else:
            dictOfEachNode["colVal"] = 4

        if dictOfEachNode not in dictForJson["nodes"]:
            listOfNodes1.append(dictOfEachNode)

        dictOfEachLink = {}
        dictOfEachLink["source"] = "Fadell"
        dictOfEachLink["target"] = key
        dictOfEachLink["value"] = dic1[key]
        listOfLinks1.append(dictOfEachLink)

    dictForJson["nodes"] += listOfNodes1
    dictForJson["links"] += listOfLinks1

    listOfNodes.append({"id": "Koolhaas", "group": 1, "colVal": 5})

    for key in dic2:
        dictOfEachNode = {}
        dictOfEachNode["id"] = key
        dictOfEachNode["group"] = 2

        if key in disciplinary_1:
            dictOfEachNode["colVal"] = 1
        elif key in disciplinary_2:
            dictOfEachNode["colVal"] = 2
        elif key in nonDoubDisciplinary:
            dictOfEachNode["colVal"] = 3
        else:
            dictOfEachNode["colVal"] = 4

        if dictOfEachNode not in dictForJson["nodes"]:
            listOfNodes2.append(dictOfEachNode)

        dictOfEachLink = {}
        dictOfEachLink["source"] = "Koolhaas"
        dictOfEachLink["target"] = key
        dictOfEachLink["value"] = dic2[key]
        listOfLinks2.append(dictOfEachLink)

    dictForJson["nodes"] += listOfNodes2
    dictForJson["links"] += listOfLinks2

    return dictForJson


# Function to create the dictonary from the actor wordFrequency dictionaries
## This dictionary gets converted to JSON
## to create actor pairs and all stop words
def createDictForJson4_MF(dic, dic1):
    dictForJson = {}
    listOfNodes = []
    listOfLinks = []
    listOfNodes1 = []
    listOfLinks1 = []

    listOfNodes.append({"id": "Maak", "group": 1})

    for key in dic:
        dictOfEachNode = {}
        dictOfEachNode["id"] = key
        dictOfEachNode["group"] = 2
        listOfNodes.append(dictOfEachNode)

        dictOfEachLink = {}
        dictOfEachLink["source"] = "Maak"
        dictOfEachLink["target"] = key
        dictOfEachLink["value"] = dic[key]
        listOfLinks.append(dictOfEachLink)

    dictForJson["nodes"] = listOfNodes
    dictForJson["links"] = listOfLinks

    listOfNodes.append({"id": "Fadell", "group": 1})

    for key in dic1:
        dictOfEachNode = {}
        dictOfEachNode["id"] = key
        dictOfEachNode["group"] = 2
        if dictOfEachNode not in dictForJson["nodes"]:
            listOfNodes1.append(dictOfEachNode)

        dictOfEachLink = {}
        dictOfEachLink["source"] = "Fadell"
        dictOfEachLink["target"] = key
        dictOfEachLink["value"] = dic1[key]
        listOfLinks1.append(dictOfEachLink)

    dictForJson["nodes"] += listOfNodes1
    dictForJson["links"] += listOfLinks1

    return dictForJson


def createDictForJson4_MK(dic, dic1):
    dictForJson = {}
    listOfNodes = []
    listOfLinks = []
    listOfNodes1 = []
    listOfLinks1 = []

    listOfNodes.append({"id": "Maak", "group": 1})

    for key in dic:
        dictOfEachNode = {}
        dictOfEachNode["id"] = key
        dictOfEachNode["group"] = 2
        listOfNodes.append(dictOfEachNode)

        dictOfEachLink = {}
        dictOfEachLink["source"] = "Maak"
        dictOfEachLink["target"] = key
        dictOfEachLink["value"] = dic[key]
        listOfLinks.append(dictOfEachLink)

    dictForJson["nodes"] = listOfNodes
    dictForJson["links"] = listOfLinks

    listOfNodes.append({"id": "Koolhaas", "group": 1})

    for key in dic1:
        dictOfEachNode = {}
        dictOfEachNode["id"] = key
        dictOfEachNode["group"] = 2
        if dictOfEachNode not in dictForJson["nodes"]:
            listOfNodes1.append(dictOfEachNode)

        dictOfEachLink = {}
        dictOfEachLink["source"] = "Koolhaas"
        dictOfEachLink["target"] = key
        dictOfEachLink["value"] = dic1[key]
        listOfLinks1.append(dictOfEachLink)

    dictForJson["nodes"] += listOfNodes1
    dictForJson["links"] += listOfLinks1

    return dictForJson


def createDictForJson4_FK(dic, dic1):
    dictForJson = {}
    listOfNodes = []
    listOfLinks = []
    listOfNodes1 = []
    listOfLinks1 = []

    listOfNodes.append({"id": "Fadell", "group": 1})

    for key in dic:
        dictOfEachNode = {}
        dictOfEachNode["id"] = key
        dictOfEachNode["group"] = 2
        listOfNodes.append(dictOfEachNode)

        dictOfEachLink = {}
        dictOfEachLink["source"] = "Fadell"
        dictOfEachLink["target"] = key
        dictOfEachLink["value"] = dic[key]
        listOfLinks.append(dictOfEachLink)

    dictForJson["nodes"] = listOfNodes
    dictForJson["links"] = listOfLinks

    listOfNodes.append({"id": "Koolhaas", "group": 1})

    for key in dic1:
        dictOfEachNode = {}
        dictOfEachNode["id"] = key
        dictOfEachNode["group"] = 2
        if dictOfEachNode not in dictForJson["nodes"]:
            listOfNodes1.append(dictOfEachNode)

        dictOfEachLink = {}
        dictOfEachLink["source"] = "Koolhaas"
        dictOfEachLink["target"] = key
        dictOfEachLink["value"] = dic1[key]
        listOfLinks1.append(dictOfEachLink)

    dictForJson["nodes"] += listOfNodes1
    dictForJson["links"] += listOfLinks1

    return dictForJson


## Functions to create the dictonary from the actor allWordFrequency dictionaries
## This dictionary gets converted to JSON
## to create for each actor and his nonstop and stopwords network
def createDictForJson3_Actor1(dic):
    dictForJson = {}
    listOfNodes = []
    listOfLinks = []
    listOfNodes1 = []
    listOfLinks1 = []
    listOfNodes2 = []
    listOfLinks2 = []

    listOfNodes.append({"id": "Maak", "group": 1, "colVal": 6})

    for key in dic:
        dictOfEachNode = {}
        dictOfEachNode["id"] = key
        if key not in stopWords:
            dictOfEachNode["group"] = 2
            
            if key in disciplinary_1:
                dictOfEachNode["colVal"] = 1
            elif key in disciplinary_2:
                dictOfEachNode["colVal"] = 2
            elif key in nonDoubDisciplinary:
                dictOfEachNode["colVal"] = 3
            else:
                dictOfEachNode["colVal"] = 4
            
        elif key in stopWords:
            dictOfEachNode["group"] = 3
            dictOfEachNode["colVal"] = 5

        listOfNodes.append(dictOfEachNode)

        dictOfEachLink = {}
        dictOfEachLink["source"] = "Maak"
        dictOfEachLink["target"] = key
        dictOfEachLink["value"] = dic[key]
        listOfLinks.append(dictOfEachLink)

    dictForJson["nodes"] = listOfNodes
    dictForJson["links"] = listOfLinks

    return dictForJson

def createDictForJson3_Actor2(dic):
    dictForJson = {}
    listOfNodes = []
    listOfLinks = []
    listOfNodes1 = []
    listOfLinks1 = []
    listOfNodes2 = []
    listOfLinks2 = []

    listOfNodes.append({"id": "Fadell", "group": 1, "colVal": 6})

    for key in dic:
        dictOfEachNode = {}
        dictOfEachNode["id"] = key
        if key not in stopWords:
            dictOfEachNode["group"] = 2

            if key in disciplinary_1:
                dictOfEachNode["colVal"] = 1
            elif key in disciplinary_2:
                dictOfEachNode["colVal"] = 2
            elif key in nonDoubDisciplinary:
                dictOfEachNode["colVal"] = 3
            else:
                dictOfEachNode["colVal"] = 4

        elif key in stopWords:
            dictOfEachNode["group"] = 3
            dictOfEachNode["colVal"] = 5

        listOfNodes.append(dictOfEachNode)

        dictOfEachLink = {}
        dictOfEachLink["source"] = "Fadell"
        dictOfEachLink["target"] = key
        dictOfEachLink["value"] = dic[key]
        listOfLinks.append(dictOfEachLink)

    dictForJson["nodes"] = listOfNodes
    dictForJson["links"] = listOfLinks

    return dictForJson


def createDictForJson3_Actor3(dic):
    dictForJson = {}
    listOfNodes = []
    listOfLinks = []
    listOfNodes1 = []
    listOfLinks1 = []
    listOfNodes2 = []
    listOfLinks2 = []

    listOfNodes.append({"id": "Koolhaas", "group": 1, "colVal": 6})

    for key in dic:
        dictOfEachNode = {}
        dictOfEachNode["id"] = key
        if key not in stopWords:
            dictOfEachNode["group"] = 2

            if key in disciplinary_1:
                dictOfEachNode["colVal"] = 1
            elif key in disciplinary_2:
                dictOfEachNode["colVal"] = 2
            elif key in nonDoubDisciplinary:
                dictOfEachNode["colVal"] = 3
            else:
                dictOfEachNode["colVal"] = 4

        elif key in stopWords:
            dictOfEachNode["group"] = 3
            dictOfEachNode["colVal"] = 5

        listOfNodes.append(dictOfEachNode)

        dictOfEachLink = {}
        dictOfEachLink["source"] = "Koolhaas"
        dictOfEachLink["target"] = key
        dictOfEachLink["value"] = dic[key]
        listOfLinks.append(dictOfEachLink)

    dictForJson["nodes"] = listOfNodes
    dictForJson["links"] = listOfLinks

    return dictForJson


def createDictForJson2(dic):  
    listOfSubDicts = []

    for key in dic:
        subDict = {}
        if dic[key][0] == "Niklas_Maak":
            subDict["Actor"] = "Niklas Maak"
            subDict["Time"] =dic[key][1]
            subDict["Value"] = 1
            subDict["NumberOfWords"] = dic[key][2]
            subDict["NumberOfContentfulWords"] = dic[key][3]
            subDict["NumberOfNonContentfulWords"] = dic[key][2] - dic[key][3] 
        elif dic[key][0] == "Tony_Fadell":
            subDict["Actor"] = "Tony Fadell"
            subDict["Time"] =dic[key][1]
            subDict["Value"] = 2
            subDict["NumberOfWords"] = dic[key][2]
            subDict["NumberOfContentfulWords"] = dic[key][3]
            subDict["NumberOfNonContentfulWords"] = dic[key][2] - dic[key][3] 
        elif dic[key][0] == "Rem_Koolhaas":
            subDict["Actor"] = "Rem Koolhaas" 
            subDict["Time"] =dic[key][1]
            subDict["Value"] = 3
            subDict["NumberOfWords"] = dic[key][2]
            subDict["NumberOfContentfulWords"] = dic[key][3]
            subDict["NumberOfNonContentfulWords"] = dic[key][2] - dic[key][3] 
        
        listOfSubDicts.append(subDict)

    return listOfSubDicts 


## Function to create a dictonary for each actor that contains {word: number of occurrence}
## These three dictionaries are later used to create the dictForJSON
def findExchangedWordFrequencyByActor(lst1, lst2):
    resultList = []
    wordExchangedList = []
    wordExchangedCount = 0

    #print(lst1)
    #print(set(lst1))

    for word1 in lst1:
        for word2 in lst2:
        
            if word1 == word2 and \
                 word1 not in wordExchangedList and \
                     word1.isnumeric() == False:
                     wordExchangedList.append(word1)
                     totalUse = lst1.count(word1) + lst2.count(word2)
                     wordExchangedCount += totalUse
    
    resultList.append(wordExchangedList)
    resultList.append(len(wordExchangedList))
    resultList.append(wordExchangedCount)
               
    return resultList

def findExchangedDisciplinaryWordFrequencyByActor(lst1, lst2):
    resultList = []
    wordExchangedList = []
    wordExchangedCount = 0

    #print(lst1)
    #print(set(lst1))

    for word1 in lst1:
        for word2 in lst2:
            if word1 in disciplinary_1 \
               or word1 in disciplinary_2 \
               or word1 in nonDoubDisciplinary:
                if word1 == word2 and \
                    word1 not in wordExchangedList and \
                        word1.isnumeric() == False:
                        wordExchangedList.append(word1)
                        totalUse = lst1.count(word1) + lst2.count(word2)
                        wordExchangedCount += totalUse
    
    resultList.append(wordExchangedList)
    resultList.append(len(wordExchangedList))
    resultList.append(wordExchangedCount)
               
    return resultList


def createDictForJson10(lst1, lst2, lst3):
    dictForJson = {}
    listOfNodes = []
    listOfLinks = []
    #listOfNodes1 = []
    listOfLinks1 = []
    #listOfNodes2 = []
    listOfLinks2 = []

    listOfNodes.append({"id": "Goldberger", "group": 1})
    listOfNodes.append({"id": "Fadell", "group": 1})
    listOfNodes.append({"id": "Koolhaas", "group": 1})

    dictOfEachLink = {}
    dictOfEachLink["source"] = "Goldberger"
    dictOfEachLink["target"] = "Fadell"
    dictOfEachLink["value"] = lst1[1]
    dictOfEachLink["valueTimes"] = lst1[2]
    #dictOfEachLink["time"] = 8
    listOfLinks.append(dictOfEachLink)

    dictOfEachLink = {}
    dictOfEachLink["source"] = "Goldberger"
    dictOfEachLink["target"] = "Koolhaas"
    dictOfEachLink["value"] = lst2[1]
    dictOfEachLink["valueTimes"] = lst2[2]
    #dictOfEachLink["time"] = 8
    listOfLinks.append(dictOfEachLink)

    dictOfEachLink = {}
    dictOfEachLink["source"] = "Fadell"
    dictOfEachLink["target"] = "Koolhaas"
    dictOfEachLink["value"] = lst3[1]
    dictOfEachLink["valueTimes"] = lst3[2]
    #dictOfEachLink["time"] = 8
    listOfLinks.append(dictOfEachLink)

    dictForJson["nodes"] = listOfNodes
    dictForJson["links"] = listOfLinks

    return dictForJson

def mergeDictsForJson(dic1, dic2, dic3, dic4):  #dic5, dic6)
    mergedDictForJson = {}

    mergedDictForJson["nodes"] = dic1["nodes"]

    for i in range(len(dic1["links"])):
        dic1["links"][i]["time"] = 8
    for i in range(len(dic2["links"])):
        dic2["links"][i]["time"] = 16
    for i in range(len(dic3["links"])):
        dic3["links"][i]["time"] = 24
    for i in range(len(dic4["links"])):
        dic4["links"][i]["time"] = 32
    # for i in range(len(dic5["links"])):
    #     dic5["links"][i]["time"] = 40
    # for i in range(len(dic6["links"])):
    #     dic6["links"][i]["time"] = 48
    
    mergedDictForJson["links"] = dic1["links"]
    mergedDictForJson["links"] += (dic2["links"])
    mergedDictForJson["links"] += (dic3["links"])
    mergedDictForJson["links"] += (dic4["links"])
    # mergedDictForJson["links"] += (dic5["links"])
    # mergedDictForJson["links"] += (dic6["links"])

    return mergedDictForJson




##################################################################
## Calling the functions that create dictionaries and JSONs
##################################################################

## Returns list of words (wordsNoPunctNoStamp)
wordsNoPunctNoStamp = removeStamps(raw)
#print(wordsNoPunctNoStamp)
#print("BREAK")

## Returns actorInfo = {index: [actorName], ...}
actorInfo = addActors(wordsNoPunctNoStamp)
#print(actorInfo)
#print("BREAK")

## Returns actorInfo = {index: [actorName, timeStamp], ...}
dic_V1 = addTimeStamps(raw, actorInfo)
#print(dic_V1)
#print("BREAK")

## Returns actorInfo = {index: [actorName, timeStamp, numWords], ...}
dic_V2 = addNumWordsByActor(wordsNoPunctNoStamp, dic_V1)
#print(dic_V2)
#print("BREAK")

## Returns actorInfo = {index: [actorName, timeStamp, numWords, \
# numContentfulWords], ...}
dic_V3 = addNumContentfulWordsByActor(wordsNoPunctNoStamp, dic_V2)
# print(dic_V3)
# print("BREAK")


### Taking the actorInfo = {index: [actorName, timeStamp, numWords, numContentfulWords], ...} 
### and creating / saving a JSON with the same data
### This JSON is for heatmap (matrix) and bar charts 
# b = createDictForJson2(dic_V3)
# print(b)
# print("BREAK")

# json_object_b = json.dumps(b, indent = 1)
# print(json_object_b)

# with open("sample12.json", "w") as outfile:
#     json.dump(b, outfile)


##########################################################################
### These are for all the nonstop words
### Taking a list of three listsOfNonStopWordListsbyActor 
### and creating a wordFrequencyDict for each actor
### and creating / saving a JSON from wordFrequencyDict(s) of three actors
### This JSON is for actor-word network (graphs)
listOfNonStopWordListsbyActor = makeNonStopWordListsByActor(wordsNoPunctNoStamp)
# print(listOfNonStopWordListsbyActor)
# print("BREAK")
# print(lengthMeasurer(listOfNonStopWordListsbyActor))
# print("BREAK")

count_M = countDisciplinaryWordsByActor(listOfNonStopWordListsbyActor[0])
# print(count_M)
# print("BREAK")

count_F = countDisciplinaryWordsByActor(listOfNonStopWordListsbyActor[1])
# print(count_F)
# print("BREAK")

count_K = countDisciplinaryWordsByActor(listOfNonStopWordListsbyActor[2])
# print(count_K)
# print("BREAK")


## Disciplinary words
listOfDisciplinaryWordListsbyActor = makeDiscpWordListsByActor(wordsNoPunctNoStamp)
# print(listOfDisciplinaryWordListsbyActor)
# print("BREAK")
# print(lengthMeasurer(listOfDisciplinaryWordListsbyActor))
# print("BREAK")

wordDisciplinaryFrequencyDict_Maak = findWordFrequencyByActor(listOfDisciplinaryWordListsbyActor[0])
# print(wordDisciplinaryFrequencyDict_Maak)
# print("BREAK")
wordDisciplinaryFrequencyDict_Fadell = findWordFrequencyByActor(listOfDisciplinaryWordListsbyActor[1])
# print(wordDisciplinaryFrequencyDict_Fadell)
# print("BREAK")
wordDisciplinaryFrequencyDict_Koolhaas = findWordFrequencyByActor(listOfDisciplinaryWordListsbyActor[2])
# print(wordDisciplinaryFrequencyDict_Koolhaas)
# print("BREAK")

# print(filterDict(wordDisciplinaryFrequencyDict_Maak, 3))
# print("BREAK")
# print(filterDict(wordDisciplinaryFrequencyDict_Fadell, 3))
# print("BREAK")
# print(filterDict(wordDisciplinaryFrequencyDict_Koolhaas, 3))
# print("BREAK")


## First 8 minutes
listOfNonStopWordListsWithTimebyActor_8 = makeNonStopWordListsByActor(wordsNoPunct_8)
# print(listOfNonStopWordListsWithTimebyActor_8)
# print("BREAK")
# print(lengthMeasurer(listOfNonStopWordListsWithTimebyActor_8))
# print("BREAK")

# Between Maak and Fadell
a_8 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_8[0], listOfNonStopWordListsWithTimebyActor_8[1])
# print(a_8)
# print("BREAK")

# Between Maak and Koolhaas
aa_8 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_8[0], listOfNonStopWordListsWithTimebyActor_8[2])
# print(aa_8)
# print("BREAK")

# Between Fadell and Koolhaas
aaa_8 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_8[1], listOfNonStopWordListsWithTimebyActor_8[2])
# print(aaa_8)
# print("BREAK")

dict_8 = createDictForJson10(a_8, aa_8, aaa_8)
# print(dict_8)
# print("BREAK")


## Disciplinary and interdisciplinary words
# Between Maak and Fadell
b_8 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_8[0], listOfNonStopWordListsWithTimebyActor_8[1])
# print(b_8)
# print("BREAK")

# Between Maak and Koolhaas
bb_8 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_8[0], listOfNonStopWordListsWithTimebyActor_8[2])
# print(bb_8)
# print("BREAK")

# Between Fadell and Koolhaas
bbb_8 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_8[1], listOfNonStopWordListsWithTimebyActor_8[2])
# print(bbb_8)
# print("BREAK")

dict_88 = createDictForJson10(b_8, bb_8, bbb_8)
# print(dict_88)
# print("BREAK")


## First 16 minutes
listOfNonStopWordListsWithTimebyActor_16 = makeNonStopWordListsByActor(wordsNoPunct_16)
# print(listOfNonStopWordListsWithTimebyActor_16)
# print("BREAK")
# print(lengthMeasurer(listOfNonStopWordListsWithTimebyActor_16))
# print("BREAK")

# Between Maak and Fadell
a_16 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_16[0], listOfNonStopWordListsWithTimebyActor_16[1])
# print(a_16)
# print("BREAK")

# Between Maak and Koolhaas
aa_16 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_16[0], listOfNonStopWordListsWithTimebyActor_16[2])
# print(aa_16)
# print("BREAK")

# Between Fadell and Koolhaas
aaa_16 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_16[1], listOfNonStopWordListsWithTimebyActor_16[2])
# print(aaa_16)
# print("BREAK")

dict_9 = createDictForJson10(a_16, aa_16, aaa_16)
# print(dict_9)
# print("BREAK")


## Disciplinary and interdisciplinary words
# Between Maak and Fadell
b_16 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_16[0], listOfNonStopWordListsWithTimebyActor_16[1])
# print(b_16)
# print("BREAK")

# Between Maak and Koolhaas
bb_16 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_16[0], listOfNonStopWordListsWithTimebyActor_16[2])
# print(bb_16)
# print("BREAK")

# Between Fadell and Koolhaas
bbb_16 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_16[1], listOfNonStopWordListsWithTimebyActor_16[2])
# print(bbb_16)
# print("BREAK")

dict_99 = createDictForJson10(b_16, bb_16, bbb_16)
# print(dict_99)
# print("BREAK")



## First 24 minutes
listOfNonStopWordListsWithTimebyActor_24 = makeNonStopWordListsByActor(wordsNoPunct_24)
# print(listOfNonStopWordListsWithTimebyActor_24)
# print("BREAK")
# print(lengthMeasurer(listOfNonStopWordListsWithTimebyActor_24))
# print("BREAK")

# Between Maak and Fadell
a_24 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_24[0], listOfNonStopWordListsWithTimebyActor_24[1])
# print(a_24)
# print("BREAK")

# Between Maak and Koolhaas
aa_24 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_24[0], listOfNonStopWordListsWithTimebyActor_24[2])
# print(aa_24)
# print("BREAK")

# Between Fadell and Koolhaas
aaa_24 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_24[1], listOfNonStopWordListsWithTimebyActor_24[2])
# print(aaa_24)
# print("BREAK")

dict_10 = createDictForJson10(a_24, aa_24, aaa_24)
# print(dict_10)
# print("BREAK")


## Disciplinary and interdisciplinary words
# Between Maak and Fadell
b_24 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_24[0], listOfNonStopWordListsWithTimebyActor_24[1])
# print(b_24)
# print("BREAK")

# Between Maak and Koolhaas
bb_24 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_24[0], listOfNonStopWordListsWithTimebyActor_24[2])
# print(bb_24)
# print("BREAK")

# Between Fadell and Koolhaas
bbb_24 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_24[1], listOfNonStopWordListsWithTimebyActor_24[2])
# print(bbb_24)
# print("BREAK")

dict_1010 = createDictForJson10(b_24, bb_24, bbb_24)
# print(dict_1010)
# print("BREAK")


## First 32 minutes
listOfNonStopWordListsWithTimebyActor_32 = makeNonStopWordListsByActor(wordsNoPunct_32)
# print(listOfNonStopWordListsWithTimebyActor_32)
# print("BREAK")
# print(lengthMeasurer(listOfNonStopWordListsWithTimebyActor_32))
# print("BREAK")

# Between Maak and Fadell
a_32 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_32[0], listOfNonStopWordListsWithTimebyActor_32[1])
# print(a_32)
# print("BREAK")

# Between Maak and Koolhaas
aa_32 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_32[0], listOfNonStopWordListsWithTimebyActor_32[2])
# print(aa_32)
# print("BREAK")

# Between Fadell and Koolhaas
aaa_32 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_32[1], listOfNonStopWordListsWithTimebyActor_32[2])
# print(aaa_32)
# print("BREAK")

dict_11 = createDictForJson10(a_32, aa_32, aaa_32)
# print(dict_11)
# print("BREAK")


## Disciplinary and interdisciplinary words
# Between Maak and Fadell
b_32 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_32[0], listOfNonStopWordListsWithTimebyActor_32[1])
# print(b_32)
# print("BREAK")

# Between Maak and Koolhaas
bb_32 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_32[0], listOfNonStopWordListsWithTimebyActor_32[2])
# print(bb_32)
# print("BREAK")

# Between Fadell and Koolhaas
bbb_32 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_32[1], listOfNonStopWordListsWithTimebyActor_32[2])
# print(bbb_32)
# print("BREAK")

dict_1111 = createDictForJson10(b_32, bb_32, bbb_32)
# print(dict_1111)
# print("BREAK")


## First 40 minutes
# listOfNonStopWordListsWithTimebyActor_40 = makeNonStopWordListsByActor(wordsNoPunct_40)
# print(listOfNonStopWordListsWithTimebyActor_40)
# print("BREAK")
# print(lengthMeasurer(listOfNonStopWordListsWithTimebyActor_40))
# print("BREAK")

# Between Maak and Fadell
# a_40 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_40[0], listOfNonStopWordListsWithTimebyActor_40[1])
# print(a_40)
# print("BREAK")

# # Between Maak and Koolhaas
# aa_40 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_40[0], listOfNonStopWordListsWithTimebyActor_40[2])
# print(aa_40)
# print("BREAK")

# # Between Fadell and Koolhaas
# aaa_40 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_40[1], listOfNonStopWordListsWithTimebyActor_40[2])
# print(aaa_40)
# print("BREAK")

# dict_12 = createDictForJson10(a_40, aa_40, aaa_40)
# print(dict_12)
# print("BREAK")


## Disciplinary and interdisciplinary words
# Between Maak and Fadell
# b_40 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_40[0], listOfNonStopWordListsWithTimebyActor_40[1])
# print(b_40)
# print("BREAK")

# # Between Maak and Koolhaas
# bb_40 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_40[0], listOfNonStopWordListsWithTimebyActor_40[2])
# print(bb_40)
# print("BREAK")

# # Between Fadell and Koolhaas
# bbb_40 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_40[1], listOfNonStopWordListsWithTimebyActor_40[2])
# print(bbb_40)
# print("BREAK")

# dict_1212 = createDictForJson10(b_40, bb_40, bbb_40)
# print(dict_1212)
# print("BREAK")


## First 48 minutes (at the end)
# listOfNonStopWordListsWithTimebyActor_48 = makeNonStopWordListsByActor(wordsNoPunct)
# print(listOfNonStopWordListsWithTimebyActor_48)
# print("BREAK")
# print(lengthMeasurer(listOfNonStopWordListsWithTimebyActor_48))
# print("BREAK")

# Between Maak and Fadell
# a_48 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_48[0], listOfNonStopWordListsWithTimebyActor_48[1])
# print(a_48)
# print("BREAK")

# Between Maak and Koolhaas
# aa_48 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_48[0], listOfNonStopWordListsWithTimebyActor_48[2])
# print(aa_48)
# print("BREAK")

# Between Fadell and Koolhaas
# aaa_48 = findExchangedWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_48[1], listOfNonStopWordListsWithTimebyActor_48[2])
# print(aaa_48)
# print("BREAK")

# dict_13 = createDictForJson10(a_48, aa_48, aaa_48)
# print(dict_13)
# print("BREAK")


## Disciplinary and interdisciplinary words
# Between Maak and Fadell
# b_48 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_48[0], listOfNonStopWordListsWithTimebyActor_48[1])
# print(b_48)
# print("BREAK")

# Between Maak and Koolhaas
# bb_48 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_48[0], listOfNonStopWordListsWithTimebyActor_48[2])
# print(bb_48)
# print("BREAK")

# Between Fadell and Koolhaas
# bbb_48 = findExchangedDisciplinaryWordFrequencyByActor(listOfNonStopWordListsWithTimebyActor_48[1], listOfNonStopWordListsWithTimebyActor_48[2])
# print(bbb_48)
# print("BREAK")

# dict_1313 = createDictForJson10(b_48, bb_48, bbb_48)
# print(dict_1313)
# print("BREAK")


dictForFinalNetwork = mergeDictsForJson(dict_8, dict_9, dict_10, dict_11) #dict_12, dict_13)
# print(dictForFinalNetwork)
# print("BREAK")

# json_object_aa = json.dumps(dictForFinalNetwork, indent = 1)
# print(json_object_aa)

# with open("sample200.json", "w") as outfile:
#     json.dump(dictForFinalNetwork, outfile)


dictForFinalNetwork_b = mergeDictsForJson(dict_88, dict_99, dict_1010, dict_1111) #dict_1212, dict_1313)
print(dictForFinalNetwork_b)
print("BREAK")

# json_object_bb = json.dumps(dictForFinalNetwork_b, indent = 1)
# print(json_object_bb)

# with open("sample210.json", "w") as outfile:
#     json.dump(dictForFinalNetwork_b, outfile)



wordFrequencyDict_Maak = findWordFrequencyByActor(listOfNonStopWordListsbyActor[0])
# print(wordFrequencyDict_Maak)
# print("BREAK")
wordFrequencyDict_Fadell = findWordFrequencyByActor(listOfNonStopWordListsbyActor[1])
# print(wordFrequencyDict_Fadell)
# print("BREAK")
wordFrequencyDict_Koolhaas = findWordFrequencyByActor(listOfNonStopWordListsbyActor[2])
# print(wordFrequencyDict_Koolhaas)
# print("BREAK")

# print(filterDict(wordFrequencyDict_Maak, 10))
# print(filterDict(wordFrequencyDict_Fadell, 10))
# print(filterDict(wordFrequencyDict_Koolhaas, 10))

a = createDictForJson(wordFrequencyDict_Maak, wordFrequencyDict_Fadell, wordFrequencyDict_Koolhaas)
# print(a)
# print("BREAK")

# json_object_a = json.dumps(a, indent = 1)
# print(json_object_a)

# with open("sample555.json", "w") as outfile:
#     json.dump(a, outfile)


##########################################################################
### These are for all the stop words
### Taking a list of three listsOfStopWordListsbyActor 
### and creating a wordFrequencyDict for each actor
### and creating / saving a JSON from wordFrequencyDict(s) of three actors
### This JSON is for actor-word network (graphs)
listOfStopWordListsbyActor = makeStopWordListsByActor(wordsNoPunctNoStamp)
# print(listOfStopWordListsbyActor)
# print("BREAK")
# print(lengthMeasurer(listOfStopWordListsbyActor))
# print("BREAK")

stopWordFrequencyDict_Maak = findWordFrequencyByActor(listOfStopWordListsbyActor[0])
# print(stopWordFrequencyDict_Maak)
# print("BREAK")
stopWordFrequencyDict_Fadell = findWordFrequencyByActor(listOfStopWordListsbyActor[1])
# print(stopWordFrequencyDict_Fadell)
# print("BREAK")
stopWordFrequencyDict_Koolhaas = findWordFrequencyByActor(listOfStopWordListsbyActor[2])
# print(stopWordFrequencyDict_Koolhaas)
# print("BREAK")

z = createDictForJson(stopWordFrequencyDict_Maak, stopWordFrequencyDict_Fadell, stopWordFrequencyDict_Koolhaas)
# print(z)
# print("BREAK")

# json_object_z = json.dumps(z, indent = 1)
# print(json_object_z)

# with open("sample16_MFK.json", "w") as outfile:
#     json.dump(z, outfile)

u = createDictForJson4_MF(stopWordFrequencyDict_Maak, stopWordFrequencyDict_Fadell)
# print(u)
# print("BREAK")

# json_object_u = json.dumps(u, indent = 1)
# print(json_object_u)

# with open("sample16_MF.json", "w") as outfile:
#     json.dump(u, outfile)

t = createDictForJson4_MK(stopWordFrequencyDict_Maak, stopWordFrequencyDict_Koolhaas)
# print(t)
# print("BREAK")

# json_object_t = json.dumps(t, indent = 1)
# print(json_object_t)

# with open("sample16_MK.json", "w") as outfile:
#     json.dump(t, outfile)

s = createDictForJson4_FK(stopWordFrequencyDict_Fadell, stopWordFrequencyDict_Koolhaas)
# print(s)
# print("BREAK")

# json_object_s = json.dumps(s, indent = 1)
# print(json_object_s)

# with open("sample16_FK.json", "w") as outfile:
#     json.dump(s, outfile)




##########################################################################
### These are for all the words
### Taking a list of three listsOfWordListsbyActor 
### and creating a allWordFrequencyDict for each actor
### and creating / saving a JSON from allWordFrequencyDict(s) of three actors
### This JSON is for actor-word network (graphs)
listOfWordListsbyActor = makeWordListsByActor(wordsNoPunctNoStamp)
# print(listOfWordListsbyActor)
# print("BREAK")
# print(lengthMeasurer(listOfWordListsbyActor))
# print("BREAK")

allWordFrequencyDict_Maak = findWordFrequencyByActor(listOfWordListsbyActor[0])
# print(allWordFrequencyDict_Maak)
# print("BREAK")
allWordFrequencyDict_Fadell = findWordFrequencyByActor(listOfWordListsbyActor[1])
# print(allWordFrequencyDict_Fadell)
# print("BREAK")
allWordFrequencyDict_Koolhaas = findWordFrequencyByActor(listOfWordListsbyActor[2])
# print(allWordFrequencyDict_Koolhaas)
# print("BREAK")

c = createDictForJson3_Actor1(allWordFrequencyDict_Maak)
# print(c)
# print("BREAK")

# json_object_c = json.dumps(c, indent = 1)
# print(json_object_c)

# with open("sample6_M.json", "w") as outfile:
#     json.dump(c, outfile)

d = createDictForJson3_Actor2(allWordFrequencyDict_Fadell)
# print(d)
# print("BREAK")

# json_object_d = json.dumps(d, indent = 1)
# print(json_object_d)

# with open("sample6_F.json", "w") as outfile:
#     json.dump(d, outfile)

e = createDictForJson3_Actor3(allWordFrequencyDict_Koolhaas)
# print(e)
# print("BREAK")

# json_object_e = json.dumps(e, indent = 1)
# print(json_object_e)

# with open("sample66_K.json", "w") as outfile:
#     json.dump(e, outfile)




##################################################################
## Creating the dataframe 1 (from the dictionary)
##################################################################

## dictConverter also adds the column of indeces (important!)
dic_Final = dictConverter(dic_V3)
# print(dic_Final)
# print("BREAK")

# df1 = pd.DataFrame(dic_Final)
# print(df1)

