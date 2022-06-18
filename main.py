import streamlit as st
from tools import cList, expandContractions, clean_txt, import_pickle

#WRITE CODE HERE
clf = import_pickle("./new_models/RandomForestClassifier_model.pkl")

st.title("RIVISTA.")
txt = st.text_area("What's on your mind?")

count_vect = import_pickle("./new_models/vectorizer.pkl")
transformed_txt = count_vect.transform(clean_txt([txt]))

if st.button("Send"):
    try:
        score = clf.predict(transformed_txt)
        if score[0] == 0:
            st.write(f"Class: Not Depressed")
        else:
            st.write(f"Class: Depressed :(")
            
        st.write("Confidence: {:.2f}%".format(clf.predict_proba(count_vect.transform(clean_txt([txt])))[0, score][0] * 100))
    except Exception as e:
        st.write("Please fill in the blank!")
else:
    pass
