# Python script to interact with Jenkins server api
Sample script to connect and run various queries and jobs in Jenkins

## Installation
create virtualenv using any method you'd like [virtualenv](https://pypi.org/project/virtualenv/), [direnv](https://direnv.net/), [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
pip install -r requirements.txt
```

## Modify folder
In text editor add file .env .
add the following text in .env file and save:  

USER= xxx  

PASS= yyy

where you will add your Jenkins (xxx)username and (yyy)password.
## Modify file
review various commented function calls and uncomment the ones you need.
## Usage

```python
python connect_api.py

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
