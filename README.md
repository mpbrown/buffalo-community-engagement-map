# Buffalo Community Engagement Workshop
This site lets people explore community engagement opportunities around Buffalo, NY. 

## Project Background
Every spring and fall, I host a civic engagement workshop with the University at Buffalo Office of Scholarships and Fellowships SPARK program. The workshop is designed to help first year students discover ways to get involved in the Buffalo community and help them establish those connections.

Due to the COVID-19 pandemic cancelling the in-person workshop, I adapted the activities to an online format that students could participate in from any web browser.

![GitHub release (latest by date)](https://img.shields.io/github/v/release/mpbrown/buffalo-community-engagement-map)
![GitHub](https://img.shields.io/github/license/mpbrown/buffalo-community-engagement-map)

## Development

### Tech Stack
- Python 3 with Django
- Heroku CI deployment
- Celery for async emails
- Vue 3 for UI

### Requirements
Make sure these are installed on your machine.
- [Python 3](https://www.python.org/downloads/)
- [RabbitMQ](https://www.rabbitmq.com/download.html) - for async emailing

### Instructions

#### Clone repository and open terminal in project's root directory.
```
$ PATH\TO\REPO\buffalo-community-engagement-map>
```

#### Setup environment
```
pip install pipenv
```
Install [pipenv](https://github.com/pypa/pipenv) to manage Python virtual environment and dependencies. [Learn more about pipenv.](https://realpython.com/pipenv-guide/)

```
pipenv sync
```
Create a Python virtual environment using pipenv and install dependencies based on the Pipfile.lock


#### Start local server
```
pipenv run manage.py runserver
```

#### Visit local server
Open server in browser at [http://localhost:8000/](http://localhost:8000/)


## License

The project is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
