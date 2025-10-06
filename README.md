Introduction
This project focuses on building a robust machine learning system to classify breast cancer tumors as malignant or benign based on diagnostic features. The goal is to provide an accurate and interpretable model that can assist in early cancer detection, potentially improving patient outcomes through timely intervention.

Project Overview
The workflow for this project is organized into several key stages:

1. Data Acquisition & Preparation
Dataset: The dataset was sourced from Kaggle containing diagnostic measurements of breast cell nuclei from digitized images.

Cleaning & Preprocessing:

Checked for missing values and ensured data completeness.

Standardized feature scales using StandardScaler to improve model training consistency.

Encoded labels into binary classes: Malignant (1) and Benign (0).

Split the data into training (80%) and test (20%) sets to ensure unbiased evaluation.

2. Exploratory Data Analysis (EDA)
Conducted descriptive statistics to understand feature distributions.

Created visualizations (pairplots, histograms, heatmaps) to identify correlations and patterns between features.

Observed strong relationships between cell shape, size, and texture with cancer classification.

3. Feature Engineering
Standardized the dataset using StandardScaler to ensure all features were on the same scale, which improves the performance of Model. The scaler was fitted only on the training data and the same transformation was applied to the test data to avoid data leakage.

4. Model Training & Evaluation
Single Model Evaluation: Trained a Logistic Regression model (random_state=42) using scaled training data. Predicted on the test set and evaluated performance using accuracy score and a classification report.

Multiple Model Comparison: Implemented and trained five classification algorithms — Logistic Regression, K-Nearest Neighbors (KNN), Support Vector Machine (SVM), Random Forest, and Gradient Boosting — to compare predictive performance. Measured accuracy and reviewed classification metrics for each model.

Confusion Matrix Visualization: Plotted confusion matrices for all five models to visualize misclassifications, with emphasis on detecting false negatives.

5. Model Training and Hyperparameter Tuning (SVM)
To achieve optimal model performance, a Support Vector Machine (SVM) classifier was trained and fine-tuned using GridSearchCV. The parameter grid explored different values for the regularization parameter C, the kernel type (linear and rbf), and the gamma parameter for the RBF kernel.

The grid search was run with 5-fold cross-validation, ensuring a balanced trade-off between bias and variance. The best hyperparameters were selected based on cross-validation accuracy, and the tuned model was then retrained on the entire training dataset using these optimal settings.

This approach ensured that the model was not only fitted for the current dataset but also generalized well for unseen data.

6. Model Evaluation and Performance Metrics
The tuned SVM model was evaluated on the test dataset using multiple performance metrics to provide a comprehensive view of its predictive capability.

Key metrics calculated included:

Accuracy – the proportion of correctly predicted observations out of all observations.

Precision, Recall, and F1-score – obtained from a classification report to assess the balance between correctly identifying positive cases and avoiding false positives.

Confusion Matrix – visualized to highlight the distribution of true positives, true negatives, false positives, and false negatives across the classes.

ROC Curve & AUC Score – the Receiver Operating Characteristic curve was plotted, and the Area Under the Curve (AUC) was calculated (0.9974), indicating excellent model discrimination capability.

This multi-metric evaluation confirmed that the SVM model achieved high accuracy and robustness, with exceptional class separation as demonstrated by the near-perfect AUC score
