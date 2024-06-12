
<img src="https://s1.ezgif.com/tmp/ezgif-1-b7a6619cc9.gif" width="100%"/>


# Fast API + MS Pack

This is a full solustion of implement the fast api project with multiple micro-service, with the various feature.


## Features

- One gateway to handle all the MS.
- Easy and readable structure.
- JWT authentication inbuild.
- Global DB logging.
- Inbuild dummy API's.


## Demo UI

![demo ui](https://i.postimg.cc/MZ4sXk7G/image.png)


## API Reference

#### Login

```http
  POST /auth/login
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Email or username |
| `password` | `string` | **Required**. Password |

#### Register

```http
  POST /auth/register
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. Email address |
| `password` | `string` | **Required**. Password |

#### Get Logged in user

```http
  GET /user/me
```

#### Add multiple address

```http
  POST /address
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `street` | `string` | **Required**. |
| `city` | `string` | **Required**. |
| `state` | `string` | **Required**. 2 degit state |
| `zip` | `integer` | **Required**. |

## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  sudo apt install docker.io
  sudo apt install docker-compose
  sudo apt install make
```

Start the server

```bash
  make up
```

Now you can able to access the docs page using the below URL

- [http://localhost:8000/docs](http://localhost:8000/docs)

Also you can access the php-myadmin using the below URL

- [http://localhost:8001](http://localhost:8001)

## Authors

- [@abbackend](https://www.github.com/abbackend)


