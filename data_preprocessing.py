import joblib
import numpy as np
import pandas as pd
import os

dirname = os.path.dirname(__file__)

pca_1 = joblib.load(os.path.join(dirname, "model/pca_1.joblib"))
pca_2 = joblib.load(os.path.join(dirname, "model/pca_2.joblib"))
# Load encoders
encoder_path_Application_mode = os.path.join(dirname, 'model/encoder_Application_mode.joblib')
encoder_path_Course = os.path.join(dirname, 'model/encoder_Course.joblib')
encoder_path_Daytime_evening_attendance = os.path.join(dirname, 'model/encoder_Daytime_evening_attendance.joblib')
encoder_path_Debtor = os.path.join(dirname, 'model/encoder_Debtor.joblib')
encoder_path_Displaced = os.path.join(dirname, 'model/encoder_Displaced.joblib')
encoder_path_Educational_special_needs = os.path.join(dirname, 'model/encoder_Educational_special_needs.joblib')
encoder_path_Fathers_occupation = os.path.join(dirname, 'model/encoder_Fathers_occupation.joblib')
encoder_path_Fathers_qualification = os.path.join(dirname, 'model/encoder_Fathers_qualification.joblib')
encoder_path_Gender = os.path.join(dirname, 'model/encoder_Gender.joblib')
encoder_path_International = os.path.join(dirname, 'model/encoder_International.joblib')
encoder_path_Marital_status = os.path.join(dirname, 'model/encoder_Marital_status.joblib')
encoder_path_Mothers_occupation = os.path.join(dirname, 'model/encoder_Mothers_occupation.joblib')
encoder_path_Nacionality = os.path.join(dirname, 'model/encoder_Nacionality.joblib')
encoder_path_Previous_qualification = os.path.join(dirname, 'model/encoder_Previous_qualification.joblib')
encoder_path_Scholarship_holder = os.path.join(dirname, 'model/encoder_Scholarship_holder.joblib')
encoder_path_Tuition_fees_up_to_date = os.path.join(dirname, 'model/encoder_Tuition_fees_up_to_date.joblib')

encoder_Application_mode = joblib.load(encoder_path_Application_mode)
encoder_Course = joblib.load(encoder_path_Course)
encoder_Daytime_evening_attendance = joblib.load(encoder_path_Daytime_evening_attendance)
encoder_Debtor = joblib.load(encoder_path_Debtor)
encoder_Displaced = joblib.load(encoder_path_Displaced)
encoder_Educational_special_needs = joblib.load(encoder_path_Educational_special_needs)
encoder_Fathers_occupation = joblib.load(encoder_path_Fathers_occupation)
encoder_Fathers_qualification = joblib.load(encoder_path_Fathers_qualification)
encoder_Gender = joblib.load(encoder_path_Gender)
encoder_International = joblib.load(encoder_path_International)
encoder_Marital_status = joblib.load(encoder_path_Marital_status)
encoder_Mothers_occupation = joblib.load(encoder_path_Mothers_occupation)
encoder_Nacionality = joblib.load(encoder_path_Nacionality)
encoder_Previous_qualification = joblib.load(encoder_path_Previous_qualification)
encoder_Scholarship_holder = joblib.load(encoder_path_Scholarship_holder)
encoder_Tuition_fees_up_to_date = joblib.load(encoder_path_Tuition_fees_up_to_date)

# Load scalers
scaler_path_application_order = os.path.join(dirname, 'model/scaler_Application_order.joblib')
scaler_path_admission_grade = os.path.join(dirname, 'model/scaler_Admission_grade.joblib')
scaler_path_age_at_enrollment = os.path.join(dirname, 'model/scaler_Age_at_enrollment.joblib')
scaler_path_Curricular_units_1st_sem_approved = os.path.join(dirname, 'model/scaler_Curricular_units_1st_sem_approved.joblib')
scaler_path_Curricular_units_1st_sem_enrolled = os.path.join(dirname, 'model/scaler_Curricular_units_1st_sem_enrolled.joblib')
scaler_path_Curricular_units_1st_sem_evaluations = os.path.join(dirname, 'model/scaler_Curricular_units_1st_sem_evaluations.joblib')
scaler_path_Curricular_units_1st_sem_grade = os.path.join(dirname, 'model/scaler_Curricular_units_1st_sem_grade.joblib')
scaler_path_Curricular_units_2nd_sem_approved = os.path.join(dirname, 'model/scaler_Curricular_units_2nd_sem_approved.joblib')
scaler_path_Curricular_units_2nd_sem_enrolled = os.path.join(dirname, 'model/scaler_Curricular_units_2nd_sem_enrolled.joblib')
scaler_path_Curricular_units_2nd_sem_evaluations = os.path.join(dirname, 'model/scaler_Curricular_units_2nd_sem_evaluations.joblib')
scaler_path_Curricular_units_2nd_sem_grade = os.path.join(dirname, 'model/scaler_Curricular_units_2nd_sem_grade.joblib')
scaler_path_GDP = os.path.join(dirname, 'model/scaler_GDP.joblib')
scaler_path_Inflation_rate = os.path.join(dirname, 'model/scaler_Inflation_rate.joblib')
scaler_path_Previous_qualification_grade = os.path.join(dirname, 'model/scaler_Previous_qualification_grade.joblib')
scaler_path_Unemployment_rate = os.path.join(dirname, 'model/scaler_Unemployment_rate.joblib')

scaler_Admission_grade = joblib.load(scaler_path_admission_grade)
scaler_Age_at_enrollment = joblib.load(scaler_path_age_at_enrollment)
scaler_Application_order = joblib.load(scaler_path_application_order)
scaler_Curricular_units_1st_sem_approved = joblib.load(scaler_path_Curricular_units_1st_sem_approved)
scaler_Curricular_units_1st_sem_enrolled = joblib.load(scaler_path_Curricular_units_1st_sem_enrolled)
scaler_Curricular_units_1st_sem_evaluations = joblib.load(scaler_path_Curricular_units_1st_sem_evaluations)
scaler_Curricular_units_1st_sem_grade = joblib.load(scaler_path_Curricular_units_1st_sem_grade)
scaler_Curricular_units_2nd_sem_approved = joblib.load(scaler_path_Curricular_units_2nd_sem_approved)
scaler_Curricular_units_2nd_sem_enrolled = joblib.load(scaler_path_Curricular_units_2nd_sem_enrolled)
scaler_Curricular_units_2nd_sem_evaluations = joblib.load(scaler_path_Curricular_units_2nd_sem_evaluations)
scaler_Curricular_units_2nd_sem_grade = joblib.load(scaler_path_Curricular_units_2nd_sem_grade)
scaler_GDP = joblib.load(scaler_path_GDP)
scaler_Inflation_rate = joblib.load(scaler_path_Inflation_rate)
scaler_Previous_qualification_grade = joblib.load(scaler_path_Previous_qualification_grade)
scaler_Unemployment_rate = joblib.load(scaler_path_Unemployment_rate)

pca_numerical_columns_1 = [
  "Curricular_units_1st_sem_enrolled",
  "Curricular_units_1st_sem_evaluations",
  "Curricular_units_1st_sem_approved",
  "Curricular_units_1st_sem_grade",
  "Curricular_units_2nd_sem_enrolled",
  "Curricular_units_2nd_sem_evaluations",
  "Curricular_units_2nd_sem_approved",
  "Curricular_units_2nd_sem_grade",
]

pca_numerical_columns_2 = [
  "Admission_grade",
  "GDP",
  "Age_at_enrollment",
  "Previous_qualification_grade"
]


def data_preprocessing(data):
    """Preprocessing data
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction 
        
    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()
    
    df["Application_mode"] = data["Application_mode"]
    df["Course"] = data["Course"]
    df["Daytime_evening_attendance"] = data["Daytime_evening_attendance"]
    df["Debtor"] = data["Debtor"]
    df["Displaced"] = data["Displaced"]
    df["Educational_special_needs"] = data["Educational_special_needs"]
    df["Fathers_occupation"] = data["Fathers_occupation"]
    df["Fathers_qualification"] = data["Fathers_qualification"]
    df["Gender"] = data["Gender"]
    df["International"] = data["International"]
    df["Marital_status"] = data["Marital_status"]
    df["Mothers_occupation"] = data["Mothers_occupation"]
    df["Mothers_qualification"] = data["Mothers_qualification"]
    df["Nacionality"] = data["Nacionality"]
    df["Previous_qualification"] = data["Previous_qualification"]
    df["Scholarship_holder"] = data["Scholarship_holder"]
    df["Tuition_fees_up_to_date"] = data["Tuition_fees_up_to_date"]

    df["Application_order"] = scaler_Application_order.transform(np.asarray(data["Application_order"]).reshape(-1,1))[0]
    df["Unemployment_rate"] = scaler_Unemployment_rate.transform(np.asarray(data["Unemployment_rate"]).reshape(-1,1))[0]
    df["Inflation_rate"] = scaler_Inflation_rate.transform(np.asarray(data["Inflation_rate"]).reshape(-1,1))[0]

    data["Curricular_units_1st_sem_enrolled"] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_evaluations"] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(data["Curricular_units_1st_sem_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_approved"] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_enrolled"] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data["Curricular_units_2nd_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_evaluations"] = scaler_Curricular_units_2nd_sem_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_approved"] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data["Curricular_units_2nd_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1,1))[0]


    df[["pc1_1", "pc1_2"]] = pca_1.transform(data[pca_numerical_columns_1])
    
    # PCA 2
    data["Admission_grade"] = scaler_Admission_grade.transform(np.asarray(data["Admission_grade"]).reshape(-1,1))[0]
    data["GDP"] = scaler_GDP.transform(np.asarray(data["GDP"]).reshape(-1,1))[0]
    data["Age_at_enrollment"] = scaler_Age_at_enrollment.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1,1))[0]
    data["Previous_qualification_grade"] = scaler_Previous_qualification_grade.transform(np.asarray(data["Previous_qualification_grade"]).reshape(-1,1))[0]

    df[["pc2_1", "pc2_2"]] = pca_2.transform(data[pca_numerical_columns_2])
    
    return df