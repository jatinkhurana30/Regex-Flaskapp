from alpine:latest

RUN apk add --no-cache python3-dev \
	&& pip3 install --upgrade pip
	
WORKDIR /regex

COPY . /regex

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python3"]
CMD ["app.py"]