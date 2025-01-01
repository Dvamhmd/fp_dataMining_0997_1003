import streamlit as st
from web_function import predict

def app(df, x, y):

    st.title("Halaman Prediksi")

    col1, col2, col3 = st.columns(3)

    with col1:
        bp = st.text_input ("Input Nilai Blood Pressure (bp) :")
    with col1:
        sg = st.text_input ("Input Nilai Spesific Gravity (bp) :")
    with col1:
        al = st.text_input ("Input Nilai Albumin (al) :")
    with col1:
        su = st.text_input ("Input Nilai Sugar (su) :")
    with col1:
        rbc = st.text_input ("Input Nilai Red Blood Cells (rbc) :")
    with col1:
        pc = st.text_input ("Input Nilai Pus Cell (pc) :")
    with col1:
        pcc = st.text_input ("Input Nilai Pus Cell Clumps (pcc) :")
    with col1:
        ba = st.text_input ("Input Nilai Bacteria (ba) :")
    with col2:
        bgr = st.text_input ("Input Nilai Blood Glucose (bgr) :")
    with col2:
        bu = st.text_input ("Input Nilai Blood Urea (bu) :")
    with col2:
        sc = st.text_input ("Input Nilai Serum Creatinine (sc) :")
    with col2:
        sod = st.text_input ("Input Nilai Sodium (sod) :")
    with col2:
        pot = st.text_input ("Input Nilai Potassium (pot) :")
    with col2:
        hemo = st.text_input ("Input Nilai Hemoglobin (hemo) :")
    with col2:
        pcv = st.text_input ("Input Nilai Packed Cell Volume (pcv) :")
    with col2:
        wc = st.text_input ("Input Nilai White Cell Count (wc) :")
    with col3:
        rc = st.text_input ("Input Nilai Red Blood Cell Count (rc) :")
    with col3:
        htn = st.text_input ("Input Nilai Hypertension (htn) :")
    with col3:
        dm = st.text_input ("Input Nilai Diabetes Melitus (dm) :")
    with col3:
        cad = st.text_input ("Input Nilai Coronary Disease (cad) :")
    with col3:
        appet = st.text_input ("Input Nilai Appetite (appet) :")
    with col3:
        pe = st.text_input ("Input Nilai Pedal Edema (pe) :")
    with col3:
        ane = st.text_input ("Input Nilai Anemia (ane) :")

    features = [bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]

    #tombol prediksi
    if st.button("Prediksi"):
        prediction, score = predict(x, y, features)
        score = score
        st.info("Prediksi Sukses...")

        if (prediction == 1):
            st.warning("Orang tersebut rentan terkena penyakit ginjal")
        else:
            st.success("Orang tersebut relatif aman dari penyakit ginjal")

        st.write("Tingkat Akurasi Model : ", (score*100),"%")