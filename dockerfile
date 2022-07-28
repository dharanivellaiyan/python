FROM python
WORKDIR /root/myapp
COPY add.py ./
CMD ["python","./add.py"]
