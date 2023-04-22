# Chat App Using Flask-SocketIO
This is a chat application, implemented using Flask-SocketIO, javascript and postgres SQL

## Features

- User authentication with Flask-Login
- Real-time messaging with Flask-SocketIO
- PostgreSQL integration for storing user data and messages

## Requirements

- Python 3.x


## Installation

1. Clone the repository:
git clone https://github.com/JamesOmare/Flask_Chat_Application.git
2. Change directory to the cloned project:
cd Flask_Chat_Application
4. Create a PostgreSQL database and table by running the following commands:
psql -c "CREATE DATABASE chat_app;"
psql -d chat_app -f schema.sq
5. Set the `DATABASE_URL` environment variable in the `.env` file:
DATABASE_URL=postgresql://user:password@localhost/chat_app
6. Run the application:
## Usage

Open your web browser and go to `http://localhost:5000`. You will be redirected to the login page. If you don't have an account, click on the `Register` button to create a new account.

After logging in, you will be redirected to the chat page where you can send and receive messages with other users in real-time.

## Live site
The live site is deployed at heroku: "https://jamesfeed-chat.herokuapp.com"

## Contributing

Contributions are always welcome! If you would like to contribute to this project, please open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.