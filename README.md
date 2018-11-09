# Project 1: Logs Analysis

The project is the first project in Udacity's Full Stack Developer Nano-degree program.
It's a reporting tool that uses the news database to answers the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Getting Started

To get this project up and running, please follow up the instructions bellow.

### Required Database Views

1. articles_visits view represents the number of visits of each article represented by the article slug, and it's used to answer the first and second questions.
```
CREATE VIEW articles_visits AS SELECT SUBSTRING(path,10) AS slug, COUNT(*) AS visits FROM log GROUP BY path;
```
2. requests_status view represents each day with the number of total requests and failed requests. It's used to answer the third question.
```
CREATE VIEW requests_status AS SELECT time::date AS date, COUNT(CASE WHEN status NOT LIKE '200%' THEN 1 END) AS num_of_erros, COUNT(*) AS num_of_requests FROM log GROUP BY date;
```

### Prerequisites

Download and install the following software:
1. Python3: https://www.python.org/downloads/
2. Vagrant: https://www.vagrantup.com/downloads.html
3. Virtual Machine: https://www.virtualbox.org/wiki/Downloads
4. FSND virtual machine: https://github.com/udacity/fullstack-nanodegree-vm

## Running the project

In your terminal, navigate to vagrant directory and use the commands bellow:
```
vagrant up
vagrant ssh
cd /vagrant
git clone https://github.com/Noufst/ud-logs-analysis.git
```

In the same terminal window, run the following command:
```
cd News
python3 news.py
```

### Coding style test

The code follows pycodestyle style code.
To test the project against pycodestyle, please follow the instructions in: https://github.com/PyCQA/pycodestyle

## Author

* **Nouf Saleh** - [Noufst](https://github.com/Noufst)
