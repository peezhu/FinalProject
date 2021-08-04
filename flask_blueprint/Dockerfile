FROM python:3.8

EXPOSE 5000

WORKDIR /flask_blueprint

COPY /flask_blueprint/requirement.txt /flask_blueprint

RUN pip install  -r requirement.txt --upgrade pip

COPY . /flask_blueprint

CMD python flask_blueprint/__init__.py