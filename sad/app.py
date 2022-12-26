# @Email:  contact@pythonandvba.comAVG
# @Website:  https://pythonandvba.com
# @YouTube:  https://youtube.com/c/CodingIsFun
# @Project:  Sales Dashboard w/ Streamlit



import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="RATA RATA PENYELESAIAN PENDIDIKAN DI INDONESIA", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
@st.cache
def get_data_from_sma():
    dfa = pd.read_excel(
        io="TingkatPenyelesaianPendidikanProvince.xlsx",
        engine="openpyxl",
        sheet_name="SMA",
        skiprows=0,
        usecols="A:I",
        nrows=35,
    )
    return dfa

def get_data_from_sd():
    dfd = pd.read_excel(
        io="TingkatPenyelesaianPendidikanProvince.xlsx",
        engine="openpyxl",
        sheet_name="SD",
        skiprows=0,
        usecols="A:I",
        nrows=35,
    )
    return dfd

def get_data_from_smp():
    dfp = pd.read_excel(
        io="TingkatPenyelesaianPendidikanProvince.xlsx",
        engine="openpyxl",
        sheet_name="SMP",
        skiprows=0,
        usecols="A:I",
        nrows=35,
    )
    return dfp
    

dfa = get_data_from_sma()
dfd = get_data_from_sd()
dfp = get_data_from_smp()


# ---- MAINPAGE ----
st.title(":bar_chart: RATA RATA PENYELESAIAN PENDIDIKAN DI INDONESIA")
st.markdown("##")

st.markdown("""---""")

# SMA

sma = dfa.groupby(by=["PROVINCE"]).sum()[["AVG"]].sort_values(by="AVG")

sma_s = px.line(
    sma,
    x="AVG",
    y=sma.index,
    orientation="h",
    title="<b>RATA-RATA SMA</b>",
    color_discrete_sequence=["#0083B8"] * len(sma),
    template="plotly_white",
)
sma_s.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# RATA SMP

smp = dfp.groupby(by=["PROVINCE"]).sum()[["AVG"]].sort_values(by="AVG")
smp_s = px.line(
    smp,
    x="AVG",
    y=smp.index,
    orientation="h",
    title="<b>RATA-RATA smp</b>",
    color_discrete_sequence=["#0083B8"] * len(smp),
    template="plotly_white",
)
smp_s.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# RATA SD


sd = dfd.groupby(by=["PROVINCE"]).sum()[["AVG"]].sort_values(by="AVG")
sd_s = px.line(
    sd,
    x="AVG",
    y=sd.index,
    orientation="h",
    title="<b>RATA-RATA SD</b>",
    color_discrete_sequence=["#0083B8"] * len(sd),
    template="plotly_white",
)
sd_s.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# st.sidebar.header("Please Filter Here:")
# city = st.sidebar.selectbox(
#     "Select the City:",
#     ('SD','SMP','SMA')
# )

st.plotly_chart(sd_s, use_container_width=True)
st.plotly_chart(smp_s, use_container_width=True)
st.plotly_chart(sma_s, use_container_width=True)




# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
