import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.tree import export_graphviz
import streamlit as st
from web_function import train_model

def app(df, x, y):
    warnings.filterwarnings('ignore')

    st.title("Visualisasi Prediksi Batu Ginjal")

    # Train the model
    model, score = train_model(x, y)

    # Plot Confusion Matrix
    if st.checkbox("Plot Confusion Matrix"):
        y_pred = model.predict(x)  # Predict on training data
        cm = confusion_matrix(y, y_pred)

        # Create figure and axes
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=model.classes_, yticklabels=model.classes_, ax=ax)
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')
        ax.set_title('Confusion Matrix')

        # Display the plot in Streamlit
        st.pyplot(fig)

    # Plot Decision Tree
    if st.checkbox("Plot Decision Tree"):
        dot_data = export_graphviz(
            decision_tree=model, max_depth=3, out_file=None, filled=True, rounded=True,
            feature_names=x.columns, class_names=['nockd', 'ckd']
        )
        st.graphviz_chart(dot_data)
