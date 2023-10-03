# **Supervised Learning and Credit Risk**

## **Overview of Project**
The following analysis is aimed at applying techniques to deal with class
imbalance in binary (and even multi class) classification problems. The first
approach is to use resampling techniques such as oversampling, undersampling,
and a combination of both in conjunction with a logistic regression model from
scikit-learn. The second approach is to use ensemble learning models that have
resampling techniques built in from the Imbalanced Learn library. The goal is to
determine which approaches, if any, yield useful models for predicting credit
risk.

The context for the project is assessing credit risk for loan approvals. The
dataset is a credit card credit dataset from LendingClub. The dataset is not
included in this repository due to size.

The main analysis files are
*[credit_risk_resampling.ipynb](https://github.com/cdpeters/credit-risk-supervised-ML-sklearn/blob/main/credit_risk_resampling.ipynb)* for resampling
techniques combined with the scikit-learn logistic regression classifier and
*[credit_risk_ensemble.ipynb](https://github.com/cdpeters/credit-risk-supervised-ML-sklearn/blob/main/credit_risk_ensemble.ipynb)* for balanced random
forest and easy ensemble AdaBoost classifiers.

### **Results**
The results of the following resampling methods and ensemble models are shown in
the sections below. The target variable is loan status which has the two labels
of low risk and high risk. Note that the balanced accuracy scores are not
straightforward accuracy scores (number of predictions correct over total
predictions) and are reported here are the average of recall obtained for each
class. Additionally, within the context of credit risk, the worse situation is
when an account is misidentified as low risk and is actually high risk thus
recall for the high risk class will be most important here.

***Resampling Methods:***

1. Random Oversampling
1. SMOTE Oversampling
1. Cluster Centroids Undersampling
1. SMOTEENN Combination (Over/Under) Sampling

***Ensemble Models:***

1. Balanced Random Forest Model
1. Easy Ensemble AdaBoost Model


#### **Random Oversampling**
The following accuracy and classification report are the result of using the
`RandomOverSampler` class with a `LogisticRegression` classifier.

<div align="center">
    <img src="assets/images/credit_supervised/random_oversampling_accuracy.svg"
         alt="random oversampling accuracy" />
</div>

* The balanced accuracy is 0.65 for random oversampling which is less than
  ideal.

<div align="center">
    <img src="assets/images/credit_supervised/random_oversampling.svg"
         alt="random oversampling" />
</div>

* The precision for the high risk class is low at 0.01 but it isn't as crucial
  since this means that there are a lot of accounts identified as high risk that
  actually are not high risk. The precision for low risk is 1.00.
* However, in terms of recall, the high risk category has a 0.63 which should
  not be acceptable. The recall for low risk is also low at 0.67.

#### **SMOTE Oversampling**
The following accuracy and classification report are the result of using the
`SMOTE` class (sampling strategy set to `auto`) with a `LogisticRegression`
classifier.

<div align="center">
    <img src="assets/images/credit_supervised/SMOTE_oversampling_accuracy.svg"
         alt="smote oversampling accuracy" />
</div>

* The balanced accuracy for SMOTE oversampling has actually decreased from the
  random oversampling to 0.63.

<div align="center">
    <img src="assets/images/credit_supervised/SMOTE_oversampling.svg"
         alt="smote oversampling" />
</div>

* The precision remains the same for both classes at 0.01 and 1.00 for high risk
  and low risk respectively.
* The recall for high risk is 0.60 which is a decrease from random oversampling.
  The recall for low risk also dropped slightly to 0.66.

#### **Cluster Centroids Undersampling**
The following accuracy and classification report are the result of using the
`ClusterCentroids` class with a `LogisticRegression` classifier.

<div align="center">
    <img src="assets/images/credit_supervised/cluster_centroids_undersampling_accuracy.svg"
         alt="cluster centroids undersampling accuracy" />
</div>

* The balanced accuracy for cluster centroids undersampling is 0.53 which is a
  significant drop from the previous two methods.

<div align="center">
    <img src="assets/images/credit_supervised/cluster_centroids_undersampling.svg"
         alt="cluster centroids undersampling" />
</div>

* The precision for both classes is unchanged from the previous two sampling
  techniques.
* The recall for high risk at 0.61 is a slight increase compared to SMOTE
  however the recall for low risk is now much lower at 0.45.

#### **SMOTEENN Combination Sampling**
The following accuracy and classification report are the result of using the
`SMOTEENN` class with a `LogisticRegression` classifier.

<div align="center">
    <img src="assets/images/credit_supervised/SMOTEENN_combo_sampling_accuracy.svg"
         alt="smoteenn combination sampling accuracy" />
</div>

* The balanced accuracy for the SMOTEENN sampling approach is 0.63, much the
  same as the oversampling techniques above.

<div align="center">
    <img src="assets/images/credit_supervised/SMOTEENN_combo_sampling.svg"
         alt="smoteenn combination sampling" />
</div>

* The precision for both classes is the same as all the previous methods (0.01
  for high risk and 1.00 for low risk).
* The recall for high risk sees improvement at 0.70 for this combination
  sampling technique. This remains less than ideal as we are still missing on
  identifying 30% of actual high risk credit accounts. The recall for low risk
  is 0.55, lower than the oversampling methods, higher than the undersampling
  method.


#### **Balanced Random Forest**
The following accuracy and classification report are the result of using the
`BalancedRandomForestClassifier` class with number of estimators set to 100.

<div align="center">
    <img src="assets/images/credit_supervised/balanced_random_forest_accuracy.svg"
         alt="balanced random forest accuracy" />
</div>

* The balanced accuracy for the balanced random forest model is 0.80 which is a
  strong improvement from the approaches above.

<div align="center">
    <img src="assets/images/credit_supervised/balanced_random_forest.svg"
         alt="balanced random forest" />
</div>

* Precision for high risk has changed slightly to 0.04, precision for low risk
  remains the same as previous methods.
* Recall for high risk is 0.69 which is similar to the recall for SMOTEENN for
  high risk. Recall for low risk is much improved to 0.91.

#### **Easy Ensemble AdaBoost**
The following accuracy and classification report are the result of using the
`BalancedRandomForestClassifier` class with number of estimators set to 100.

<div align="center">
    <img src="assets/images/credit_supervised/easy_ensemble_adaboost_accuracy.svg"
         alt="easy ensemble AdaBoost accuracy" />
</div>

* The balanced accuracy for the easy ensemble AdaBoost model is 0.92, the
  highest out of all methods used in the project.

<div align="center">
    <img src="assets/images/credit_supervised/easy_ensemble_adaboost.svg"
         alt="easy ensemble AdaBoost" />
</div>

* The precision for high risk has increased slightly to 0.07. The precision for
  low risk remains the same as every previous method.
* Here, recall for high risk has shown the greatest improvement compared to all
  other methods at 0.90. We are now only missing on 10% of actual high risk
  loans (see recommendation in summary section). The recall for low risk is
  0.94, similar to the result from the balanced random forest model.

### **Summary**
In conclusion, each of the resampling methods yielded low recall overall and
very little improvements in this metric in comparison to each other. Because
high recall for the high risk class is a requirement in order to avoid
misidentifying high risk accounts as low risk, the resampling techniques with
logistic regression would not be recommended to be used to assess credit risk in
this situation.

Furthermore, the ensemble models overall did better in terms of the balanced
accuracy and recall metrics as compared to the resampling with logistic
regression approach. Specifically, the easy ensemble AdaBoost model performed
the best with recall values for both classes right around 0.90. That being said,
if missing on 10% of accounts that should actually be labeled high risk is
acceptable, then this model would be the recommendation. If this is not
acceptable, then none of the models in this project would be recommended for
this credit risk assessment situation. Improvements should then be sought
elsewhere to improve high risk recall (different model, other refinements,
etc.).
