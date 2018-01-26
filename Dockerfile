FROM python:3

ADD main.py /
ADD graph.py /
ADD question1.py /
ADD question2.py /
ADD question3.py /
ADD rsc/ /rsc/

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]