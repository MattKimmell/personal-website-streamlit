import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import json

# run.py
if __name__ == "__main__":
    app.run()


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":high_brightness:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding_whatido = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/mining.jpg")
img_lottie_animation = Image.open("images/taro.jpg")

with open("images/new-bitcoin-touch.json", 'r') as json_f:
    header_json = json.load(json_f)
lottie_coding_header = header_json

# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hi, I am Matthew Kimmell :wave:")
        st.title("Your Friendly Neighborhood Bitcoin Pal")
        st.write(
            "Welcome to humble abode, it's not much, but if you stick around long enough, I promise to teach you something new :bulb:"
        )
        st.write("[Twitter](https://twitter.com/MatthewKimmell)")
    with right_column:
        st_lottie(lottie_coding_header, height=350, key="bitcoin")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I make videos and write for people that:
            - are interested in learning about Bitcoin
            - enjoy storytelling through charts and graphs
            - want to perform meaningful and impactful analyses by themselves
            - don't have time for the deeper research

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel](https://www.youtube.com/channel/UCV00jVwqZ_cyP-yygLtWFjA)")
    with right_column:
        st_lottie(lottie_coding_whatido, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Taro: A New Asset Issuance Protocol on Bitcoin")
        st.write(
            """
            Learn all about Taro!
            This new proposal enables new types of asset issuance and spending on the Bitcoin and Lightning Networks. Want to learn about it?
            """
        )
        st.markdown("[Read Here](https://coinshares.com/research/taro-a-new-asset-issuance-protocol-on-bitcoin)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("The Bitcoin Mining Network")
        st.write(
            """
            Curious about Bitcoin's energy consumption and environmental impact?
            In this report, I'm going to show the results of a model that calculates just that. We highlight the patterns and trends of Bitcoin Mining, its power draw and carbon emissions by country and region, check it out!
            """
        )
        st.markdown("[Read Here](https://coinshares.com/research/bitcoin-mining-network-2022)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/mattkimmellyt@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
