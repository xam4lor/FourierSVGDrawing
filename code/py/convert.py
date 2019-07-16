from math import *
import os



# MAX VECTOR VALUES
MAX_VALUE = 200


# OPEN RAW DATAS FILE
f = open("path.svg", "r")
contents = f.read()
f.close()
contentsArr = contents.split("class=\"cls-2\" points=\"")[1].split("\"/></svg>")[0]




# CONVERT TO SVG DATAS
contentsSpl = contentsArr.split(" ")


# GET MAX VALUE
max = 0
for i in range(0, len(contentsSpl)):
    if float(contentsSpl[i]) > max:
        max = float(contentsSpl[i])


# MAP ALL VALUES
for i in range(0, len(contentsSpl)):
    contentsSpl[i] = (float(contentsSpl[i]) / max) * MAX_VALUE




# ROTATE BY -90 DEGRES
theta = -3.14159 / 2
pair = False
for i in range(0, len(contentsSpl) - 1):
    if pair == True:
        x = float(contentsSpl[  i  ])
        y = float(contentsSpl[i + 1])
        xNew =  x * cos(theta) + y * sin(theta)
        yNew = -x * sin(theta) + y * cos(theta)

        contentsSpl[  i  ] = xNew
        contentsSpl[i + 1] = yNew

        pair = False
    else:
        pair = True



# CREATE END STRING
textReturn = "let drawing = [\n"

pair = False
for i in range(0, len(contentsSpl) - 1):
    if pair == True:
        textReturn += "    {x: " + str(contentsSpl[i]) + ", y: " + str(contentsSpl[i + 1]) + "},\n"
        pair = False
    else:
        pair = True

textReturn += "];"


# OUTPUT TO DATAS FILE
f2 = open("code/datas.js", "w")
f2.write(textReturn)
f2.close()


# SUCCESS
print("SUCCESS converting SVG file to JS file")
