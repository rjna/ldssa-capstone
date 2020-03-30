from sklearn.base import TransformerMixin, ClassifierMixin
import pandas as pd
import numpy as np

class NumericalDataCleaning(TransformerMixin):
    
    def transform(self, X, *_):
        X_new = X.copy()
        X_new['SubjectAge'] = X_new['SubjectAge'].replace([1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 
                                                           10., 11.], X_new['SubjectAge'].median())
        X_new = X_new.drop(columns=['ResidentIndicator'])
        return X_new
    
    def fit(self, *_):
        return self


class CategoricalDataCleaning(TransformerMixin):
    
    def transform(self, X, *_):
        X_new = X.copy()
        X_new.InterventionLocationName = X_new.InterventionLocationName.str.lower() 
        X_new.InterventionLocationName = X_new.InterventionLocationName.fillna('unknown') 
        X_new.StatuteReason = X_new.StatuteReason.fillna('Other/Error')
        X_new.SearchAuthorizationCode = X_new.SearchAuthorizationCode.fillna('N') 
        X_new.InterventionReasonCode = X_new.InterventionReasonCode.fillna('U') 
        X_new.InterventionReasonCode = X_new.InterventionReasonCode.replace('no', 'U')
        X_new.ReportingOfficerIdentificationID = X_new.ReportingOfficerIdentificationID.fillna('unknown')
        X_new['Department Name'] = X_new['Department Name'].replace('Mohegan Tribal', 'Mohegan Tribal Police') #não foi
        X_new['Department Name'] = X_new['Department Name'].replace('Mashantucket Pequot', 'Mashantucket Pequot Police')#não foi
        X_new = X_new.drop(columns=['SubjectSexCode', 'SubjectEthnicityCode', 'SubjectRaceCode'])
        return X_new
    
    def fit(self, *_):
        return self


class CreateCyclicalFeatures(TransformerMixin):
    
    def transform(self, X, *_):
        X_new = X.copy()
        X_new['InterventionDateTime'] = pd.to_datetime(X_new['InterventionDateTime'], format='%m/%d/%Y %I:%M:%S %p')
        X_new['InterventionDateYear'] = X_new['InterventionDateTime'].dt.year
        X_new['InterventionDateMonth'] = X_new['InterventionDateTime'].dt.month
        X_new['InterventionDateMonth_sin'] = np.sin((2. * X_new['InterventionDateMonth'] *  np.pi / 12))
        X_new['InterventionDateMonth_cos'] = np.cos((2. * X_new['InterventionDateMonth'] *  np.pi / 12))        
        X_new['InterventionDateDay'] = X_new['InterventionDateTime'].dt.day
        X_new['InterventionDateDay_sin'] = np.sin((2. * X_new['InterventionDateDay'] *  np.pi / 31))
        X_new['InterventionDateDay_cos'] = np.cos((2. * X_new['InterventionDateDay'] *  np.pi / 31))
        X_new['InterventionDateHour'] = X_new['InterventionDateTime'].dt.hour
        X_new['InterventionDateHour_sin'] = np.sin((2. * X_new['InterventionDateHour'] *  np.pi / 23))
        X_new['InterventionDateHour_cos'] = np.cos((2. * X_new['InterventionDateHour'] *  np.pi / 23)) 
        return X_new.drop(['InterventionDateTime', 'InterventionDateMonth', 'InterventionDateDay', 'InterventionDateHour'], axis=1)
    
    def fit(self, *_):
        return self


class Test(TransformerMixin):
    
    def transform(self, X, *_):
        X_new = X.copy()
        print(len(X_new.columns))
        return X_new
    
    def fit(self, *_):
        return self