# Preprocess data app api
## Why preprocess data
According to [this](https://learn.g2.com/data-preprocessing#:~:text=By%20preprocessing%20data%2C%20we%20make,to%20human%20error%20or%20bugs.) article by preprocessing data, we make it easier to interpret and use. This process eliminates inconsistencies or duplicates in data, which can otherwise negatively affect a model’s accuracy. Data preprocessing also ensures that there aren’t any incorrect or missing values due to human error or bugs.
## What is it
Data mining project containing 3 major services
- Interpolation
- Outlier detection
- Imbalanced data classification 
## How to use
To run this service after fork the repository, first build a image from dockerfile then run it. These steps commands are like following:
```batch
:: to build image
docker-compose build
:: to run it on 8000 port
docker-compose up 
```
Then you have access to this services on port `8000`

To see API Swagger documentation access `<domain>:8000/swagger`. If you're running it localy `<domain>` is `localhost`.
