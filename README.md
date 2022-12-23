# Lenme Demo

This is my submission for the Lenme assignment

## Installation

Install the project with pip

```bash
    pip install requirements.txt
```

## API Reference

#### user add Loan

```http
  POST /user/addLoan/${userName}/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `userName` | `string` | **Required**. name of user who adds a loan |

Json Body for Request:- 
``` json
{
"amount":5000,
"loan_period":6 
}
```

#### investor add offer

```http
  POST investor/addOffer/${investorName}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `investorName`      | `string` | **Required**. name of investor to add a Offer |

Json Body for Request :- 
```json
{
"loan_id": <int>,
"interest": <int>
}
```
#### user get all offers

```http
  GET user/allOffers/${userName}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `userName`      | `string` | **Required**. name of user who requested a loan |

Sample Json Response :-
```json 
{
"Offers": [
{
"ID": 6,
"investor": "investor2",
"Interest": 15 }
]
}
```
#### user accept offer

```http
  Get user/acceptOffer/${userName}/{offerId}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `userName`      | `string` | **Required**. name of user who requested a loan |
| `offerId`      | `int` | **Required**. ID of the offer on the user's Loan |

Sample Json Response:-

```json
{
"Success": "Offer Accepted!"
}
```
#### user pay month installment

```http
  Get user/payMonth/${userName}/${month}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `userName`      | `string` | **Required**. name of user who requested a loan |
| `month`      | `int` | **Required**. month of the installment that the user wants to pay |

ps: month is only added for simulation purpose i could make user pay installment of the current month only

Sample Json Response:- 
``` json
{
"Success": "Paid installment for month 1 with amount 896"
}
```
#### user pay all installments

```http
  Get user/payAll/${userName}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `userName`      | `string` | **Required**. name of user who requested a loan |

Sample Json Response:- {
"Error": "No installments Available and Loan Status is now COMPLETED"
}

## Notes

- some methods should be in reality post methods but since i didn't implement payment system so i used get methods to
  make it easier since i don't have any data to post to the server
- The interest rate is calculated with stable rate using simple interest equation

```js
    A = P(1 + rt)
```

## Authors

- [@OmarAtef10](https://github.com/OmarAtef10)

Email :- omar.atef.2001@gmail.com