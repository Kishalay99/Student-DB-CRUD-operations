# Student-DB-CRUD-operations
This project is made using Falcon web framework.
The project does basic CRUD operations on a student relational database made on mysql.
Backend language used is python ie. used to build an API that handles the requests fired from ajax at the front end.

To run the project, follow the following instructions:
1. Clone the repo to your local machine.
2. Run the server file using the following command (make sure you have gunicorn installed on your machine) at /CRUD/
   gunicorn server:api
3. Open the /CRUD/public/home.html on chrome browser (other browsers might not support due to different CORS header                requirements).
4. Now you can perform all CRUD operations on the Student DB from the UI.
