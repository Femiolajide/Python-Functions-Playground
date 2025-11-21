import streamlit as st 
import pyperclip as pp
import pandas as pd
from variety import derive_words, num_to_words as nw

import re 

st.write("""### **derive_words**


Hi, I have packaged the :orange[derive_words] function in a more user-friendly interface for you to try out.

---
         
You can even solve this word puzzle with it 

         
         """)

txt_entered = st.text_input(
    label="**Type the group of alphabets you want to form English words from:**",
placeholder="Type English alphabeths ONLY!",
help="e.g type 'atme'",

)
if txt_entered:
    if re.search(r"[^A-Za-z]",txt_entered):
        entry_err = ValueError("**Error:**  Only alphabets between a and z are allowed")
        st.error(entry_err)
    else:
        min_l = st.number_input(
            label="**How many letters do you want in your new word?**",
        min_value=0,
        placeholder="Type an integer ONLY!",
        max_value=len(txt_entered),
        # step=1,
        value=None
        )
        if min_l:
            try:
                derive_words(txt_entered,min_l)
            except ValueError:
                val_err = ValueError("Please type a valid number of letters")
                st.error(val_err)
            else:
                if derive_words(txt_entered,min_l):
                    st.write(
                        f"#### These are the {nw(min_l)}-letter words derivable from :blue-background[*{txt_entered}*]"
                    )
                    for x in derive_words(txt_entered,min_l):
                        st.success(x)
                else:
                    st.write(f"#### No English word can be formed from :blue-background[*{txt_entered}*]")

