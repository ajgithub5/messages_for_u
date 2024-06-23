import streamlit as st


st.header("This space is a portion of my Heart 💓")

messages = {
        "Default": "Smile please!!!  Sadaa sa muh mt banana..!!!",
        "Message 1": "Good Morning sweetheart!!! I hope you had a great sleep. So get up and take bath first..",
        "Message 2": "I missed you very much my love!!! So never think I don't miss you. I always remember you.",
        "Message 3": "Your smile is my favorite expression, with those dracula teeths that lifts my spirits.",
        "Message 4": "Keep laughing as it is my favourite melody, that symphony always gives me a kick.",
        "Message 5": "Sometimes I feel I want to dance with you my wife on a slow romantic music. Though I don't know but I want to.",
        "Message 6": "Since the day we have met we are in long distance. I am dying to live with you. Love you. Fight with you,and again love you.",
        "Message 7": "Can't wait more to have bubble bath with you with a glass of wine. I just dream for it.",
        "Message 8": "I always think when will I get to eat food prepared by you. I feel bad sometimes for not able to njoy dishes cooked by you.",
        "Message 9": "Thanks for defending me from Sagar Matte for commenting on his car. It really made me happy you being defensive about me.",
        "Message 10": "I always wish God to bless you with lots off happiness, success and healthy life. You being happy will make me happy.",
        "Message 11": "I am sorry for being angry on you at times. But don't think I have stopped loving you. Its just I am angry. Give me time I will come to you.",
        "Message 12": "Yes... It is true. I love you a lott. And I will always!!!",   
    }

selected_message = st.selectbox("Select a message from the dropdown with a smile.", list(messages.keys()))
if selected_message:
        st.balloons()
        st.text(messages[selected_message])





