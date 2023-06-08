from flask import Flask, render_template, request
import json
import os

from transformers import MarianMTModel, MarianTokenizer
import torch
import warnings
warnings.filterwarnings("ignore")


app = Flask(__name__)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/translate', methods=["POST"])
def translateText():

    if request.method == "POST":

        inputLang = request.form["inputLang"]
        outputLang = request.form["outputLang"]
        inputText = request.form["inputText"]

        if inputLang == "select":
            res = {"error": "Select input language"}
            return json.dumps(res)
        
        if outputLang == "select":
            res = {"error": "Select output language"}
            return json.dumps(res)


        if outputLang == inputLang:
           res = {
            "translated_text":  inputText
            }
           return json.dumps(res)

        # if inputLang == "hi" and outputLang != "en": 
        #     res = {"error": "Work in process.."}
        #     return json.dumps(res)
        
        # if outputLang == "hi" and inputLang != "en": 
        #     res = {"error": "Work in process.."}
        #     return json.dumps(res)

 
        src_text = [inputText]
        
        model_name = "Helsinki-NLP/opus-mt-"+str(inputLang)+"-"+str(outputLang)

        tokenizer = MarianTokenizer.from_pretrained(model_name)

        model = MarianMTModel.from_pretrained(model_name)

        translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

        output = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

        res = {
            "translated_text": output[0]
        }

    else:
        res = {"error": "Method is not valid"}

    return json.dumps(res)

if __name__ == '__main__':
    app.run(debug=True)
    