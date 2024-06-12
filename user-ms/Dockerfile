# 
FROM python:3.10

# 
WORKDIR /app

# 
COPY ./requirements.txt ./requirements.txt

# 
RUN pip install -r ./requirements.txt

# 
COPY ./ ./

#
EXPOSE 50051

# 
CMD ["python3", "main.py"]