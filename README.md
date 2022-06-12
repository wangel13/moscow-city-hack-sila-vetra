# Moscow City Hack: Check fake tech news

## Setup

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
  "text": "Big news text to test"
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