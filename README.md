# Youtube Data API 

# Requirements

- [Node.js 15.5+](https://nodejs.org/en/) or later
- [Python 3.7](https://www.python.org/downloads/) or later
- MacOS, Windows (including WSL), and Linux are supported
- npm (comes bundled with node.js) or [yarn](https://yarnpkg.com/getting-started/install)


# Steps to build starter files for project
## 1. Generate Django Starter Files

 ```pip
  django-admin startproject youtube_data_api
  ```
  
  This contains all the backend files for the project.


## 2. Generate React Starter Files

 ```pip
  npx create-react-app dashboard
  ```
  This contains all the frontend files for the project.


## 3. Create a django app in the youtube_data_api folder 
```pip
  python manage.py startapp videos
  ```


# Steps to run the project

## 1.Change the directory to youtube_data_api
```pip
cd youtube_data_api
```
## 2.Install the dependencies
```pip
pip install -r requirements.txt
```
## 3.Run the django project
```pip
python manage.py runserver
```
## 4.Open another terminal
## 5.Change the directory to dashboard
```js
cd dashboard
```
## 6.Install the dependencies
```js
npm i
```
## 7.Run the react app
```js
npm start
```


# Conclusion

Congratulations! You have made it till the end and have learnt how to implement Django and React with Youtube Data and Search API.
