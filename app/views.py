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
            return jsonify({"error":"no"})

        else:
            return jsonify({"error":palAce})

