import html
from flask import Flask, jsonify, request,render_template
from filter import Filter
from search import search
from storage import DBStorage

app = Flask(__name__,template_folder="templates")

search_template = """
     <form action="/" method="post">