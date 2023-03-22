from flask import Flask
import pymysql
import pymysql.cursors 
connection = pymysql.connect(
    host="10.100.33.60",
    user="mwilliams",
    password="220467419",
    database="mwilliams_socialmedia",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)