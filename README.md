# Preprocess data app api
## Why preprocess data
According to [this](https://learn.g2.com/data-preprocessing#:~:text=By%20preprocessing%20data%2C%20we%20make,to%20human%20error%20or%20bugs.) article by preprocessing data, we make it easier to interpret and use. This process eliminates inconsistencies or duplicates in data, which can otherwise negatively affect a model’s accuracy. Data preprocessing also ensures that there aren’t any incorrect or missing values due to human error or bugs.
## How to use
To run this service after fork the repository, first build a image from dockerfile then run it. These steps commands are like following:
```batch
:: to build image
docker-compose build
:: to run it on 8000 port
docker-compose up 
```
Then you have access to this services on port `8000`

To see API Swagger documentation access `<domain>:8000/swagger`. If you're running it locally `<domain>` is `localhost`.

To pull image from Docker hub do:
```
docker pull piron/preprocess-data-app-api:latest
```
For more info about docker image see [Docker hub repository](https://hub.docker.com/repository/docker/piron/preprocess-data-app-api/general)
## What is it
Data mining project containing 3 major services
- [Interpolation](https://en.wikipedia.org/wiki/Interpolation)
- [Outlier detection](https://en.wikipedia.org/wiki/Anomaly_detection)
- [Imbalanced data classification](https://machinelearningmastery.com/what-is-imbalanced-classification/)

### Interpolation
Two method of interpolation implemented
- [Linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation)
- [Cubic spline interpolation](https://en.wikipedia.org/wiki/Spline_interpolation)

### Outlier detection
Two method of outlier detection implemented
- [Z-Score](https://www.geeksforgeeks.org/z-score-for-outlier-detection-python/)
- [IQR distance from median](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/box-whisker-plots/a/identifying-outliers-iqr-rule)

### Imbalance data classification
Three method imbalance data classification implemented to balance data classification
- [Undersampling](https://machinelearningmastery.com/random-oversampling-and-undersampling-for-imbalanced-classification/)
- [Oversampling](https://machinelearningmastery.com/random-oversampling-and-undersampling-for-imbalanced-classification/)
- [SMOTE method](https://machinelearningmastery.com/smote-oversampling-for-imbalanced-classification/)
