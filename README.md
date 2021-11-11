# AsynchronousAPI

For cloning: git clone https://github.com/Shrutikiragi/AsynchronousAPI

To Run docker:

docker-compose up

Get method URL:
http://localhost:5000/lang - To get all records
http://localhost:5000/lang/<String Search> - To get all records with search conditions

Post method:
http://localhost:5000/lang - Add new Record
Body: {'name': <Input Value>}

Put method:

https://localhost:5000/lang/<String update> - To update one of the record.
Body: {'name': <Input Value>}

https://localhost:5000/updateall - To update all the records.
Body: {'name': <Input Value>}


To run pytest:
pytest -vv
