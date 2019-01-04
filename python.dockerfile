FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY database_class.py entry_window.py export_window.py left_frame.py main_driver.py main_window.py right_frame.py ./

CMD [ "python", "./main_driver.py" ]