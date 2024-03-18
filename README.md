This app consist of building a web app using machine learning to predict a product quality.

# The workflow

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

# How to run?
### STEPS:

Clone the repository

```bash
#https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
https://github.com/tiornasoro/Wine-Quality
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venvnq1 python=3.10 -y
```

```bash
conda activate venvnq1
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/tiornasoro/Wine-Quality.mlflow \
MLFLOW_TRACKING_USERNAME=tiornasoro \
MLFLOW_TRACKING_PASSWORD=0c525db70d33a67d2b96c3a98f7f04bead7b895e \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/tiornasoro/Wine-Quality.mlflow 

export MLFLOW_TRACKING_USERNAME=tiornasoro 

export MLFLOW_TRACKING_PASSWORD=0c525db70d33a67d2b96c3a98f7f04bead7b895e

```
