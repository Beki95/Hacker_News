# Hacker News sample application

![ссылка на фото](hacker-1.jpg)
1. First we need to copy the project
```
git clone origin https://github.com/Beki95/Hacker_News.git
```
___
2. Step 2 you need to create a file in the root of the project .an example is the ___env_example___ file

___
3. Step 3 go to the directory and enter the following command in the terminal

```
docker-compose -f docker-compose.base.yml build
```
___
4. Now, after assembling the containers, we just need to launch our project

```
docker-compose -f docker-compose.base.yml up
```







