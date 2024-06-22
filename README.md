# STAR WARS API :star

## How to run

> If the name of your main file is app.py or wsgi you can add the next code in that file:
 
```python

if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
```

And then use the next command to run your server

```bash

$ python3 app.py

```
> If you are using the [python-dotenv library](https://github.com/theskumar/python-dotenv?tab=readme-ov-file#command-line-interface) the you should create a `.env` or a `.flaskenv` file to include the environment variables and then run your server using the command

```bash

$ flask run

``` 
