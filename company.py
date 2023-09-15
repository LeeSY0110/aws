from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'company'


@app.route("/")
def StudViewCompany():
    status = "Approved"

    fetch_company_sql = "SELECT * FROM company WHERE status = %s"
    cursor = db_conn.cursor()

    try:
        cursor.execute(fetch_company_sql, (status))
        companyRecords = cursor.fetchall()
    
        return render_template('StudViewCompany.html', company=companyRecords)    

    except Exception as e:
        return str(e)      

    finally:
        cursor.close()




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
