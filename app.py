import streamlit as st
import pandas as pd
st.set_page_config(page_title="ET CH", layout="wide")
st.title("⚡ ET CH - CHAÑARES")
st.caption("Bahía Blanca | 132/33/13.2kV")

fechas=["Nov 24","Ene 25","Ago 25","Nov 25","Feb 26","Ago 26"]
t1=[81984,82529,83162,83600,84456,85289]
t2=[71183,71500,72010,72450,72980,73293]

c1,c2,c3,c4=st.columns(4)
c1.metric("T1CH RBC","85.289","+833")
c2.metric("T2CH RBC","73.293","+313")
c3.metric("SF6","3.1 bar","OK")
c4.metric("Estado","OPERATIVA","")

tab1,tab2,tab3=st.tabs(["Resumen IA","DAC/PFI","SSAA"])
with tab1:
    st.success("ET CH operativa sin alarmas. T1/T2 en paralelo, SF6 3.1bar, TRIPs estables. SSAA MANUAL T1XCH. Cargador 110Vcc reparado 14/08/25. DAC hab en 4 alim 480A reverse. PFI a ACOP 300ms.")
    st.line_chart(pd.DataFrame({"T1CH":t1,"T2CH":t2}, index=fechas))
with tab2:
    st.warning("DAC: 9CUYO1, 9GUAS1, 9POZO1, 3PTOA1 - I3> 480A Reverse")
    st.error("PFI: 300ms a 1A045 ACOP - Llave SERVICIO/MANT")
with tab3:
    st.info("TGSACA MANUAL T1XCH | 110Vcc 120V 4A | 48Vcc 4-8A | Arranque Negro: T2CH+BBS+ND+LCA+ACOP+3ETAN1 cerrados")
