# Installation guide

## 1. Ensure python is installed

if not run the following command `sudo apt-get install python3 python3-pip`

## 2. Download the client and server scripts

for this step i will assume the files are downloaded to the following directory
`/home/user/Downloads`but it may be different for your case

## 3. Create the service file

Navigate to `/etc/systemd/system` and create a file name `AS_service.service`

inside the file paste the following contents

```
[Unit]
Description=My Python Server
After=network.target

[Service]
ExecStart=/usr/bin/python3 //home/user/Downloads/server.py
WorkingDirectory=/home/user/Downloads
Restart=always
User=your_user
Group=your_group
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target

```

remember to fill `your_user` and `your_group` correctly

## 4. Reload daemon

run the following command to reload all daemons thereby picking up the newly 

`sudo systemctl daemon reload`

## 5. Start and enable the service

run the following commands to ensure the service starts on boot

```
sudo systemctl start my_python_server.service
sudo systemctl enable my_python_server.service
```
## 6. Verify the status of the service

run `sudo systemctl status AS_service.service` and confirm that it is active(running)

now you have a background process listening for client requests

## 7. Run the client file

use the command `python3 client.py`

## 8. Generating private keys

`openssl genpkey -algorithm RSA -out server.key`

## 9. Generating a Certificate Signing Request (CSR)

`openssl req -new -key server.key -out server.csr`

## 10. Generate a Self-Signed Certificate:

`openssl req -x509 -key server.key -in server.csr -out server.crt -days 365`