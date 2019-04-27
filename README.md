# Rx-Adherence-app

App to help patients track their adherence to prescription drug usage protocols, and allow for doctors to recieve this information.

<img width="960" alt="Screen Shot 2019-04-26 at 6 44 22 PM" src="https://user-images.githubusercontent.com/10505524/56853474-95718880-68f6-11e9-8673-f7428e640d97.png">


## Local Installation

Clone this repo

```
git clone https://github.com/stevekm/Rx-Adherence-app.git
cd Rx-Adherence-app
```

Install dependencies

```
make conda-install
make frontend-install
```

Initialize app databases

```
make init
```

Import data into app databases (run this a few times)

```
make import
```

Run local Django server

```
make runserver
```

Start Vue.js server

```
make frontend-run
```

Example `curl` request to API:

```
$ curl http://127.0.0.1:8000/users/
{"1": "Bob", "2": "Mary", "3": "John", "4": "Jane"}
```
