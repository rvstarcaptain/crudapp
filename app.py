from flask import Flask, jsonify, request
from flask_restplus import Resource, Api, fields
import pymysql
from database import mydb, cur

app = Flask(__name__)
api = Api(app,version="1.0",title="CRUD Operation",description="A Small Crud app where you can create record, delete record, get the record and update the specific record")

# create model for swagger api:
Student_Model = api.model(
    "Student",
    {
        "student_name":fields.String,
        "email_id":fields.String,
        "course":fields.String,
        "hod_name":fields.String,
        "year":fields.Integer,
        "city":fields.String,
        "state":fields.String
    }
)
@api.route("/crud/")
class Crud(Resource):
    def get(self):
        try:
            print("you are in get call:")
            query = "select * from students"
            # result = cur.execute(query)
            # print("result : ",result)
            cur.execute(query)
            result = cur.fetchall()
            
            response = {}
            response["msg"] = "Records found successfully"
            response["success"] = "True"
            response["data"] = result
            return response, 200
        except Exception as e:
            response["msg"] = "Record Doesn't found"
            response["success"] = "False"
            response["data"] = "Null"
            return response, 400

    @api.expect(Student_Model, validate=True)
    def post(self):
        try:
            print("You are in post call")
            data = request.get_json()
            name = data.get("student_name")
            email = data.get("email_id")
            course = data.get("course")
            hod_name = data.get("hod_name")
            year = data.get("year")
            city = data.get("city")
            state = data.get("state")
            query = """
                    insert into students(
                        student_name,
                        email_id,
                        course,
                        hod_name,
                        year,
                        city,
                        state
                    )
                    values(%s,%s,%s,%s,%s,%s,%s)
                    """
            stu_data = (name,email,course,hod_name,year,city,state)
            cur.execute(query,stu_data)
            mydb.commit()
            response = {}
            response["msg"] = "Student addedd successfully"
            response["success"] = "True"
            return response, 200       
        except Exception as e: 
            response = {}
            response["msg"] = "Failed to added student"
            response["success"] = "False"
            return response, 400

@api.route("/specific/<int:id>/")
class Crud_by_id(Resource):
    def get(self,id):
        try:
            query = "select * from students where roll_no = %s"
            result = cur.execute(query,id)
            response = {}
            response["msg"] = "Record get successfully"
            response["success"] = "True"
            response["data"] = result
            return response, 200
        except Exception as e:
            response = {}
            response["msg"] = f"Failed to get record on {id} this roll number"
            response["success"] = "False"
            return response, 400

    @api.expect(Student_Model, validate=True)
    def put(self,id):
        try: 
            if id in mydb:
                print("available")

            data = request.get_json()
            name = data.get("student_name")
            email = data.get("email_id")
            course = data.get("course")
            hod_name = data.get("hod_name")
            year = data.get("year")
            city = data.get("city")
            state = data.get("state")

            query_update = """
                        update students set
                        student_name = %s,
                        email_id = %s,
                        course = %s,
                        hod_name = %s,
                        year = %s,
                        city = %s,
                        state = %s
                        where roll_no = %s
                        """
            update_value = (name,email,course,hod_name,year,city,state,id)            
            cur.execute(query_update,update_value)
            mydb.commit()
            response = {}
            response["msg"] = "Record updated successfully"
            response["success"] = "True"
            return response, 200            
        except Exception as e:
            response = {}
            response["msg"] = "Record not found on specific id"
            response["success"] = "False"
            return response, 400

    def delete(self,id):
        try:
            query = "delete from students where roll_no = %s"
            cur.execute(query,id)
            mydb.commit()
            response = {}
            response["msg"] = "Record deleted successfully"
            response["success"] = "True"
            return response, 200            
        except Exception as e:
            response = {}
            response["msg"] = "Record not found on specific id"
            response["success"] = "False"
            return response, 400

if __name__ == "__main__":
    app.run(debug=True)