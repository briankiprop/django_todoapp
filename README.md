<h2><b>An overview/steps for django_todoapp</b></h2>

<h4>1. Activate environment<h4>
        cd path/to/the/folder/
        <h4><font color='red'>2. Start Projectt</font><h4>
        >django-admin startproject myDoApp
<h4>3. Start App<h4>
        >python manage.py startapp doapp
<h4>4. Start Standard Sqlite<h4>
        <p style="color:green;"> >python manage.py migrate</p>
<h4>5. Create Administator Account 👤<h4>
        <p style="color:green;">  >python manage.py createsuperuser </p>
<h4>6. Create Templates<h4>
![Screenshot](base.jpeg)
![base template](https://user-images.githubusercontent.com/58941334/71898773-2f1e5480-316b-11ea-973d-6fc0bf39f6b7.PNG)
![index template](https://user-images.githubusercontent.com/58941334/71898066-65f36b00-3169-11ea-8ddb-f077d15a343f.PNG)
<h4>7. craete views<h4>
        ![views](https://user-images.githubusercontent.com/58941334/71898543-a8697780-316a-11ea-9be7-3bd2aca68fec.PNG)
<h4>8. Add urls of the views<h4>
        ![urls](https://user-images.githubusercontent.com/58941334/71898978-bec40300-316b-11ea-92e8-5ec1f8ba871a.PNG)
<h4>9. Websettings<h4>
        ![settings-add app](https://user-images.githubusercontent.com/58941334/71898605-cafb9080-316a-11ea-9bce-f20148564853.PNG)
<h4>10. Handling the app on local host<h4>
        <p style="color:green;"> 
        > python manage.py migrate
        > python manage.py makemigrations
        > python manage.py runserver
        </p>
 <h4>From the clone should look like this 👇</h4>
     ![final](https://user-images.githubusercontent.com/58941334/71900092-2418f380-316e-11ea-889c-42fda62f58b9.PNG)   
        
<h3> Here is my final output after adding bootsrap and some css 👇</h3>
![final-output](https://user-images.githubusercontent.com/58941334/71899934-d603f000-316d-11ea-8af1-eb9e5d500fd8.PNG)
