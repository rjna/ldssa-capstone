# Transformers overview

NumericalDataCleaning -> does the cleaning of the numerical data. In this case, it replaces some of the age’s values by the median (I assumed that any driver under 12 years old would be a data imputation problem) and drops the ResidentIndicator column.  
CategoricalDataCleaning -> does the cleaning of the categorical data. In this case, it fills nulls with some reasonable values, drops some columns and replaces some department names that were incorrect.  
CreateCyclicalFeatures -> creates time related features from the timestamp feature.  
Test -> does some printing just for debugging purposes.
