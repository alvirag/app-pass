import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re

# Function to extract hashtags
def extract_hashtags(text, case_sensitive=True):
    regex_pattern = r'#\w+'
    if not case_sensitive:
        text = text.lower()
    return re.findall(regex_pattern, text)

# Function to create bar plot of top hashtags
def create_bar_plot(hashtag_counts, title, color='darkgrey'):
    fig, ax = plt.subplots(figsize=(10, 6))
    hashtag_counts.plot(kind='bar', color=color, ax=ax)
    ax.set_title(title)
    ax.set_xlabel('# Hashtag')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

# Streamlit app
def main():
    st.markdown("# Hashtag Analyzer")

    st.write("Welcome to the Hashtag Analyzer app! 🚀 " 
             "This app allows you to analyze hashtags from different datasets "
             "and visualize the top hashtags.")

    st.write("First, select a CSV file to analyze:")
    file_options = ['obamacare.csv', 'trumptweets.csv', 'got_tweets.csv']
    selected_file = st.selectbox('Select CSV file', file_options)

    case_sensitive = st.checkbox('Consider letter case')

    file_path = selected_file
    tweets = pd.read_csv(file_path)

    tweets['hashtags'] = tweets['text'].apply(lambda x: extract_hashtags(x, case_sensitive))

    hashtags_list = [item for sublist in tweets['hashtags'] for item in sublist]
    hashtag_counts = pd.Series(hashtags_list).value_counts()

    st.write("Now, select the number of top hashtags to display:")
    top_hashtags_range = st.slider('Select range for top hashtags', 5, 20, 10)
    top_hashtags = hashtag_counts.head(top_hashtags_range)

    # Color selection
    color_options = {
        'Persimmon': '#FF5733', 'Malachite': '#33FF57', 'Ultramarine Blue': '#3357FF', 
        'Neon Pink': '#FF33A1', 'Electric Violet': '#A133FF', 'Medium Aquamarine': '#33FFA1', 
        'Gold': '#FFD700', 'Blue Violet': '#8A2BE2', 'Dark Turquoise': '#00CED1', 
        'Orange Red': '#FF4500', 'Goldenrod': '#DAA520', 'Indigo': '#4B0082', 
        'Tomato': '#FF6347', 'Turquoise': '#40E0D0', 'Deep Pink': '#FF1493', 
        'Chartreuse': '#7FFF00', 'Hot Pink': '#FF69B4', 'Medium Spring Green': '#00FA9A', 
        'Dodger Blue': '#1E90FF', 'Coral': '#FF7F50'
    }
    selected_color_name = st.selectbox('Select color for the plot', list(color_options.keys()))
    selected_color = color_options[selected_color_name]

    create_bar_plot(top_hashtags, f'Top {top_hashtags_range} most common hashtags', color=selected_color)

if __name__ == "__main__":
    main()



