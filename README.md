# Hacker News sample application

![ссылка на фото](hacker-1.jpg)
1. First we need to copy the project
```
git clone https://github.com/Beki95/Hacker_News.git
```
___
2. Step 2 you need to create a file in the root of the project __.env__ example is the __env_example__ file

___
3. Step 3 go to the directory and enter the following command in the terminal

```
docker-compose -f docker-compose.base.yml build
```
___
4. Now, after creating the image, we just need to run our containers

```
docker-compose -f docker-compose.base.yml up
```
### to see the result, go to http://localhost/

<p align="right">
    <a href="https://imanaliev.postman.co/workspace/Team-Workspace~0f69d200-e47e-4099-8e03-80db1c1f696f/collection/15331219-8b43ce72-7bf7-4aa9-bcb5-1558c6812c88"><img src="https://run.pstmn.io/button.svg"></a>
</p>

