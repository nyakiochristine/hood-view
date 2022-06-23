# Hoodview

>[Christine Nyakio](https://github.com/nyakiochristine)  
  
## Description  

This project allows users to post their hood, hospitals and businesses around their neighbourhood

##HomePage
![Screenshot from 2022-06-23 01-13-39](https://user-images.githubusercontent.com/98151711/175166943-8fc9911b-2970-42fd-b84d-cb3a79a4ef93.png)

## Live Link  
  
## User Story  
  
* A user can view different neighbourhoods  
* A user can post their neighbourhood
* A user can join or leave a different neighbourhood  
* Search for businesses  
* A user can write a post for other users to see
* A user can view their profile page.
* A user can add a business name that is near the neigbourhood
  
## Setup and Installation  

To get the project .......  

<https://github.com/nyakiochristine/hoodview.git>

### Navigate into the folder and install requirements  

 ```bash
 cd hood pip install -r requirements.txt 
 ```

#### Install and activate Virtual  

```bash
- python3 -m venv virtual - source virtual/bin/activate
```

##### Install Dependencies  

```bash
 pip install -r requirements.txt 
```

##### Setup Database  

  SetUp your database User,Password, Host then make migrate  

 ```bash
python manage.py makemigrations watch
 ```

 Now Migrate

```bash
python manage.py migrate 
```

##### Run the application

bash
python manage.py runserver

##### Testing the application  

```bash
 python manage.py test 

Open the application on your browser `127.0.0.1:8000`.  
  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  

## Known Bugs

* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information

If you have any question or contributions, please email me at [chrissywangi254@gmail.com]  
  
## License

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/nyakiochristine/Picture-Globe/blob/master/LICENSE)  
* Copyright (c) 2019 **KrisTech**
