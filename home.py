import numpy as пр
import pandas as pa
import pickle
import streamlit as st

model = pickle.load(open(r'fetal_health1.pkl','rb'))

def main():
    st.title('Fetal Health Prediction')
    st.write('Enter the following parameters to predict the fetal health:')

    prolongued_decelerations = st.number_input('Prolongued Decelerations')
    abnormal_short_term_variability = st.number_input('Abnormal Short Term Variability')
    percentage_of_time_with_abnormal_long_term_variability = st.number_input('Percentage of Time with Abnormal Long Term Variability')
    histogram_variance = st.number_input('Histogram Variance')
    histogram_median = st.number_input('Histogram Median')
    mean_value_of_long_term_variability = st.number_input('Mean Value of Long Term Variability')
    histogram_mode = st.number_input('Histogram Mode')
    accelerations = st.number_input('Accelerations')

    if st.button('Predict'):
        x = [[prolongued_decelerations, abnormal_short_term_variability, percentage_of_time_with_abnormal_long_term_variability, histogram_variance, histogram_median, mean_value_of_long_term_variability, histogram_mode, accelerations]]
        output = model.predict(x)
        out = ['Normal', 'Pathological', 'Suspect']
        prediction = out[int(output[0])]

        st.success(f'The predicted fetal health is: {prediction}')

if __name__ == "__main__":
    main()
