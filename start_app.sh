echo Creating MySQL image...
sudo docker build -f mysql_db.dockerfile -t address .
echo Starting MySQL Docker Container...
sudo docker run --rm -d --name address_book_container -e MYSQL_ROOT_PASSWORD=my-secret-pw address
echo Initializing MySQL Data and starting database..
sleep 24s
echo Starting Python App!
python main_driver.py
echo Stopping Docker Container...
sudo docker stop address_book_container

