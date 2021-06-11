# Bitcoin trading strategy based on Investors Sentiment

##Project Description

#### Objective
Study whether several measures of investor sentiment in the Bitcoin market
could predict the returns of this market. Also compare the performance of different Machine learning
models (for now : two of which are Random Forest) in predicting cryptocurrency returns.

#### Status
1. Dataset collected from various source to get the sentiment data
2. Processed the  textual data using Sentiment analysis method : [Chen et al](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3398423)
3. Random decison tree methods are used to predict market return based on sentiment data.
4. A simple buy and sell trading startegy developed : Refer trading strategy section.
To do : try complex algorithms like XGBoost, RNN etc.

Note: The idea for this project is from *(provide the source link) and some of his code has been used for 
the development. You can find proper acknowledgment in the code scripts. And please refer the readme files in the 
consecutive folders/packages to understand how to run the codes.

About the dataset.

Please refer the readme file in repo-root/data/README.md
The original dataset stored in repo_root/data/02_processed/final_dataset.csv files contains the following entries.



1. Data Collection : 

Please check repo_root/src/data/README.md
