import streamlit  as st

st.title("hello world")
st.header("hello world")
st.subheader("hello world")
st.write("hello world")

st.markdown("# Hi")
st.markdown("## Hi")
st.markdown("### Hi")
st.markdown("#### Hi")
st.markdown("##### Hi")

st.success("!success")
st.info("info!")
st.warning("!!warning")
st.error("error")
st.exception(ZeroDivisionError("division not possible"))
st.help(ZeroDivisionError)
st.write("range(1,10)")
st.write(range(1,10))
st.write("1+2+2")
st.write(1+2+2)
st.code('''for i in range(0,10): 
               print(i)
        ''')

st.checkbox("male")
if(st.checkbox('female')):
    st.write("you have no brain")

st.radio('select :',("check","uncheck"))

st.subheader("select box")
st.selectbox("select any one",
             ("apple","banana","cherry"),index=0)

multiselectbox  = st.multiselect("select multiple items",
               ("7","10","11"))

st.write("you have selected",len(multiselectbox),multiselectbox)

st.subheader("button")
st.button("click me")

st.subheader("slider")
st.slider("select the volume",1,100,step=1)

st.subheader("text input")
st.text_input("input here")
st.text_input("type password", type="password")

st.text_area("write something about yourself",height=20)
st.number_input("enter your age")
st.time_input("enter time")
st.date_input("enter date")