import streamlit as st
import pandas as pd
from factor_analyzer import FactorAnalyzer
st.title("Факторный анализ")
st.sidebar.title("Параметры")
file = st.file_uploader("Исходные данные", ".csv")
if file is None:
    st.error("Выберите файл входных данных")
is_corr = st.sidebar.checkbox("Кореллеяционная матрица",
                             help = "Поставить этот флажок, если входные данные представлены в виде корелляционной матрицы")
n_factors = st.sidebar.slider("Количество факторов", 1, 10, 3, 1)
rotation = st.sidebar.selectbox("Метод вращения", 
                        {"varimax", "promax", "oblimin", "oblimax", "quartimin", "equamax"}, index = 1)
method = st.sidebar.selectbox("Метод анализа", {"minres", "ml", "principal"})
svd = st.sidebar.selectbox("Метод сингулярного разложения", 
                   {"lapack", "randomized"}, disabled=(method != "principal"))
smc = st.sidebar.checkbox("Использовать МКК", 
                          help = "Следует ли использовать квадрат множественной корреляции в качестве исходных предположений для факторного анализа")
upper_bound = st.sidebar.slider("Верхняя граница", 0.0, 10.0, 1.0, 0.0001)
lower_bound = st.sidebar.slider("Нижняя граница", 0.0, 10.0, 0.05, 0.0001)
impute = st.sidebar.selectbox("Заполнение", {"drop", "mean", "median"}, 
                              help = "Если в данных есть отсутствующие значения, либо используйте их удаление (‘drop’), либо замените их медианой столбца (‘median’) или средним значением столбца (‘mean’)")

#data = pd.read_csv("H:\\Мой диск\\Учёба\\НТвРПО\\test02.csv")
#analyzer = FactorAnalyzer(n_factors, rotation, method, smc, is_corr, {lower_bound, upper_bound}, impute, svd)
#analyzer.fit(data)

#def Run():
#    try:
#        data = pd.read_csv(file)
#        analyzer = FactorAnalyzer(n_factors, rotation, method, smc, is_corr, {lower_bound, upper_bound}, impute, svd)
#        analyzer.fit(data)
#        calculated = True
#        st.success("Матрицы заполнены");
#    except:
#        st.error("Что-то пошло не так")

def Get_Loads():
    calculated = False
    cont = st.empty()
    try:
        data = pd.read_csv(file)
        analyzer = FactorAnalyzer(n_factors, rotation, method, smc, is_corr, {lower_bound, upper_bound}, impute, svd)
        analyzer.fit(data)
        calculated = True
        st.success("Матрицы заполнены");
    except:
        st.error("Что-то пошло не так")
    if calculated:
        cont.empty()
        cont.dataframe(analyzer.loadings_)
        st.line_chart(analyzer.loadings_)

def Get_Corr():
    calculated = False
    cont = st.empty()
    try:
        data = pd.read_csv(file)
        analyzer = FactorAnalyzer(n_factors, rotation, method, smc, is_corr, {lower_bound, upper_bound}, impute, svd)
        analyzer.fit(data)
        calculated = True
        st.success("Матрицы заполнены");
    except:
        st.error("Что-то пошло не так")
    if calculated:
        cont.empty()
        cont.dataframe(analyzer.corr_)
        st.line_chart(analyzer.corr_)

def Get_uniq():
    calculated = False
    cont = st.empty()
    try:
        data = pd.read_csv(file)
        analyzer = FactorAnalyzer(n_factors, rotation, method, smc, is_corr, {lower_bound, upper_bound}, impute, svd)
        analyzer.fit(data)
        calculated = True
        st.success("Матрицы заполнены");
    except:
        st.error("Что-то пошло не так")
    if calculated:
        cont.empty()
        cont.dataframe(analyzer.get_uniquenesses())

def Get_Comm():
    calculated = False
    cont = st.empty()
    try:
        data = pd.read_csv(file)
        analyzer = FactorAnalyzer(n_factors, rotation, method, smc, is_corr, {lower_bound, upper_bound}, impute, svd)
        analyzer.fit(data)
        calculated = True
        st.success("Матрицы заполнены");
    except:
        st.error("Что-то пошло не так")
    if calculated:
        cont.empty()
        cont.dataframe(analyzer.get_communalities())

def Get_Eigens():
    calculated = False
    cont = st.empty()
    try:
        data = pd.read_csv(file)
        analyzer = FactorAnalyzer(n_factors, rotation, method, smc, is_corr, {lower_bound, upper_bound}, impute, svd)
        analyzer.fit(data)
        calculated = True
        st.success("Матрицы заполнены");
    except:
        st.error("Что-то пошло не так")
    if calculated:
        cont.empty()
        cont.dataframe(analyzer.get_eigenvalues())
        st.line_chart(analyzer.get_eigenvalues()[0])

def Get_Fvar():
    calculated = False
    cont = st.empty()
    
    try:
        data = pd.read_csv(file)
        analyzer = FactorAnalyzer(n_factors, rotation, method, smc, is_corr, {lower_bound, upper_bound}, impute, svd)
        analyzer.fit(data)
        calculated = True
        st.success("Матрицы заполнены");
    except:
        st.error("Что-то пошло не так")
    if calculated:
        cont.empty()
        frame = analyzer.get_factor_variance()
        cont.dataframe(frame)
        st.line_chart(frame)

button_columns = st.columns(3)
button_columns[0].button("Нагрузки", on_click = Get_Loads, disabled = file is None)
button_columns[1].button("Корреляции", on_click = Get_Corr, disabled = file is None)
button_columns[2].button("Выбросы", on_click = Get_uniq, 
                                disabled = file is None or ((rotation != "oblimin") and (rotation != "oblimax")))
button_columns[0].button("Общности", on_click = Get_Comm, disabled = file is None)
button_columns[1].button("Собственные значения", on_click = Get_Eigens, disabled = file is None)
button_columns[2].button("Дисперсия факторов", on_click = Get_Fvar, disabled = file is None)