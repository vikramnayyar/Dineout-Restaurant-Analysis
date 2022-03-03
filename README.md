# Dineout Restaurant Analysis

## Demo
The analysis is depicted in link ________________________________ 

## Introduction
An analysis is done on https://www.dineout.co.in/. Thus, entire Indian Dineout restaurants are analyzed. Extracting several vital informations, more than **20** visualizations are very suitably plotted.     

The notebook evaluates regional performance and customer behaviour. 

## Dataset
The dataset comprises of actual information obtained from https://www.dineout.co.in/. This consists of diverse restaurants from **12** states and **22** major cities and numerous localities. 

The dataset was acquired using **web scraping** with BeautifulSoup. It has **7533** rows with **8** features.   

## Problem Statement
With smaller staff, capital and costing requirements, the restaurant business is on a consistent rise. Ratings, cuisines, cost and location all are vital to determine a restaurant's success. 

Nevertheless, awareness of these features is very challenging. Several online platforms provide restaurant reviews and ratings, but; various types of information like cuisine preferences, locality performance etc. remain unidentified. As; awareness of customer behaviour is essential, identifying a successful restaurant business becomes challenging. 

Therefore, a proper restaurant analysis is necessary to disclose the coverted insights of restaurant business. Thus, such a project is vital for restarant business. 

## Goal
This work was performed as a personal project. The motivation was to obtain exhaustive analysis of Indian restaurant business. Regional performance and customer behaviour of all Indian Dineout restaurants is obtained. About 9 types of comprehensive analysis are obtained. 

## System Environment
![](https://forthebadge.com/images/badges/made-with-python.svg)



[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width=200>](https://pandas.pydata.org/)     [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/512px-NumPy_logo_2020.svg.png" width=200>](https://numpy.org/)     [<img target="_blank" src="https://www.fullstackpython.com/img/logos/scipy.png" width=200>](https://www.scipy.org/)                    


## Directory Structure

```bash
├── app                              # Application files
|  ├── app.py                        # Application script
├── config                           # Configuration files
|  ├── config.yaml                   # Configuration file  
├── data                             # Data files ()   
|  ├── bank.csv                      # Bank customer dataset 
|  ├── clean_data.csv                # Cleaned dataset 
|  ├── prepared_data.csv             # Prepared dataset 
|  ├── train_set.csv                 # Train data
|  ├── test_set.csv                  # Test data
|  ├── train_label.csv               # Train labels
|  ├── test_set.csv                  # Test labels
├── log                              # Log files
|  ├── get_data.log                  # "get_data.py" script logs
|  ├── data_analysis.log             # "data_analysis.py" script logs
|  ├── prepare_data.log              # "prepare_data.py" script logs 
|  ├── split_data.log                # "split_data.py" script logs 
|  ├── model_data.log                # "model_data.py" script logs 
├── model                            # Model Files
|  ├── model.pkl                     # Saved model
├── src                              # Main project scripts 
|  ├── get_data.py                   # Dataset acquistion and cleaning script
|  ├── get_data_util.py              # script declaring utility functions for get_data.py 
|  ├── data_analysis.py              # Dataset analysis and visualization script
|  ├── data_anlaysis_util.py         # script declaring utility functions for data_analysis.py 
|  ├── prepare_data.py               # Dataset preperation script
|  ├── prepare_data_util.py          # script declaring utility functions for prepare_data.py 
|  ├── split_data.py                 # Dataset splitting script  
|  ├── split_data_util.py            # script declaring utility functions for split_data.py 
|  ├── model_data.py                 # Dataset modelling script
|  ├── model_data_util.py            # script declaring utility functions for model_data.py 
|  ├── utility.py                       # script declaring general utility functions  
├── visualizations                   # Dataset visualizations
|  ├── age_vs_deposit.png            # Age vs deposit figure
|  ├── bal_vs_deposit.png            # Balance vs deposit figure
|  ├── education_vs_deposit.png      # Education vs deposit figure
|  ├── job_vs_deposit.png            # Job vs deposit figure 
|  ├── marital_vs_deposit.png        # Marital vs deposit figure
|  ├── dataset_balance.png           # Dataset balance figure
|  ├── correlation_heatmap.png       # Correalation heatmap of features
|  ├── feature_importance.png        # Feature importance of best model
|  ├── cm_etc.png                    # Confusion matrix of ExtraTreesClassifier
|  ├── cm_gbc.png                    # Confusion matrix of GradientBoostClassifier
|  ├── cm_lgbm.png                   # Confusion matrix of LightGBMClassifier
|  ├── cm_rfc.png                    # Confusion matrix of RandomForestClassifier
|  ├── cm_xgb.png                    # Confusion matrix of XGBClassifier  
|  ├── cm_cbc.png                    # Confusion matrix of CatBoostClassifier
|  ├── cm_optimized_cbc.png          # Confusion matrix of optimized CatBoostClassifier
├── requirements.txt                 # Required libraries
├── Procfile                         # Required for Heroku deployment 
├── setup.sh                         # Required for Heroku deployment
├── LICENSE                          # License
├── README.md                        # Repository description

```

## Installing Dependencies
Foremost running the project, installing the dependencies is essential. 
* Ensure Python 3.8.8 or later is installed in the system. 
* All required libraries are listed in "requirements.txt". These are easily installed; by running the following command in project directory
```bash
pip install -r requirements.txt
```

## Run Project
As discussed in **Technical Aspect** section, "src" and “app” directory possess the main scripts. 

Running the following command in the "src" directory executes the entire project  
```bash
python3 run_project.py
```
Alternatively, a project script can be individually executed using the general script 
```bash
python3 script.py
```
Here “script.py” represents any python script. 

Exceptionally, application file "app.py" runs using command 
```bash
streamlit run app/app.py
```
**Note:** To run any project script, directory location must be correct.
   
