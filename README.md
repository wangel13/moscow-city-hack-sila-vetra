# Moscow City Hack: Check fake tech news

## Setup
1. Clone repo
2. Run:
```commandline
pip3 install -r requirements.txt
```
3. Create /etc/systemd/system/backend.service
```
[Unit]
After=network.target
StartLimitIntervalSec=0
[Service]
Type=simple
Restart=always
RestartSec=1
User=root
WorkingDirectory=/root/moscow-city-hack-sila-vetra/
ExecStart=/root/moscow-city-hack-sila-vetra/start_api.sh

[Install]
WantedBy=multi-user.target
```
and /etc/systemd/system/frontend.service
```
[Unit]
After=network.target
StartLimitIntervalSec=0
[Service]
Type=simple
Restart=always
RestartSec=1
User=root
WorkingDirectory=/root/moscow-city-hack-sila-vetra/
ExecStart=/root/moscow-city-hack-sila-vetra/start_web.sh

[Install]
WantedBy=multi-user.target
```
4. Then execute
```commandline
systemctl daemon-reload
systemctl enable backend
systemctl enable frontend
systemctl start backend
systemctl start frontend
```

## Start

Run server and frontend:

```
./start_api.sh
./start_web.sh
```

## Api

### Check news for fake

`POST`: `http://localhost:5000/check`

`body`:

```
{
  // text to check
  "text": "Big news text to test",
  // tolerance
  "k": 12
}
```

### Response

```
{
  "news": [
    {
      // id on mos.ru
      "id": 105631073,
      // distance from check text to this text, less is good
      "distance": 12,
      // link to text
      "link": "https://www.mos.ru/news/item/105631073/"
    },
    ...
  ]
}
```