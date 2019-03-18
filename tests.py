%run algorithms/countours.py # run functions from  separate file: countours.py in directory algorithms
%%writefile tests.py

import pandas as pd
import seaborn as sns
from sklearn.metrics import r2_score

def analyze(inputdir, fn): 
    """Returns dataframe (columns: image, expected, result, diff) and coefficient of determination value.
    inputdir - directory with photo and csv file with columns: image,expected
    fn - your algorithm which counts cells"""
    
    comparison = pd.read_csv(f"{inputdir}/test.csv")
    comparison["result"] = comparison["image"].apply(lambda path: fn(f"{inputdir}/{path}")) # implements your counting algorythm for each image
    comparison["diff"] = comparison["result"]-comparison["expected"] # counts difference between expected and result
    r2 = r2_score(comparison["expected"], comparison["result"]) # returns R^2 (coefficient of determination) regression score function
    print("Coefficient of determination: " + str(r2)) # 1.0 is the best score
    return comparison # comparison is dataframe

# tip: how to prepare your function to testing - example using Monika's algorythm:
# def countours(filepath):
#     return _countours(filepath, 60, 10, imshow=True)


#print(analyze(folder_path, counting_algorythm)) # in this place you have to write folder_name and counting_algorythm's name
#sns.catplot(x="image", y="diff", data=result, height=8, aspect=2) # plot- if dot is in 0 on y axis - it means that algorytm counted True value


