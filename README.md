# API Documentation

## Rate Limiting

#### Daily Limit: Unlimited

- 50 request / minute
- 3 request / second

---

## Disclaimer

- This API is a free, open-source API. Use it responsibly!
- This API is not affiliated

### Endpoint Path :

```sh
 /cocktails
```

## Requests

| Request           | Description                                       |
| ----------------- | ------------------------------------------------- |
| /cocktails        | List of all cocktails                             |
| /cocktails/{id}   | Single cocktails with that specific and unique id |
| /cocktails/{name} | Single cocktails with that specific name          |

## Examples

- /cocktails - Returns all the Cocktails within the API
- /cocktails/3 - Returns the Cocktail with the id of 3
- /cocktails/Rum Sour - Return the Cocktail called Rum Sour
