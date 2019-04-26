# Rx-Adherence-app

App to help patients track their adherence to prescription drug usage protocols, and allow for doctors to recieve this information.

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
