from app import app
from flask import Flask, render_template, url_for, request, jsonify
import string
import json
from app.funciones import palabrasAceptadas

@app.route('/')
def home():
    return render_template('formulario.html')




@app.route('/verificar', methods=["GET", "POST"])
def verificar():
   if request.method == "POST":
        form=dict(request.form)
        palAce=palabrasAceptadas(form)
        if palAce=="":
            palAce="no"

        
        logs = open("logs.txt","a")
        
        
        logs.writelines(str(form)+"\n")
        logs.writelines(palAce+"\n\n\n\n\n\n")
        logs.close()
        
        
        return jsonify({"error":palAce})

