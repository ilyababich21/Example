import time
from pathlib import Path
import statsmodels.api as sm
import numpy as np
import pandas as pd
import sqlalchemy
from Tools.scripts.dutree import display
from matplotlib import pyplot as plt
# from matplotlib.dates import da
from numpy import float64, int64

# from datab import engine, Sensors_ifc
#
# db_session = sqlalchemy.orm.sessionmaker(bind=engine)
# session = db_session()
#
#
# dataset = session.query(Sensors_ifc).all()
# # dataset = session.query(Sensors_ifc).filter(Sensors_ifc.id_dat ==1,Sensors_ifc.crep_id ==1).all()
# # dataset = session.query(Sensors_ifc).filter(Sensors_ifc.id_dat ==1).all()
# count=0
# # for elem in dataset:
# #     count+=1
# #     print(elem.value,"     ",count  )
# data = {
#         # "id": [elem.id for elem in dataset],
#         "id_dat":[elem.id_dat for elem in dataset],
#     "value":[int(elem.value) for elem in dataset],
#     "crep_id":[elem.crep_id for elem in dataset],
#
# }
#
#
# df = pd.DataFrame(data)
# print("BMI: \n mean={:.2f}, \n median={:.2f}, \n std={:.2f}".format(np.mean(bmi), np.median(bmi),
# np.std(bmi)))

# print(df["value"])
# print(len(df["value"]))


# np.random.seed(123)
# df.to_csv('data.csv', index=False,mode="w")


# df.to_excel('data2.xlsx', sheet_name='Sheet1', index=False)
# print(df.shape)
# print(df.groupby(["id_dat","crep_id"]).agg({'value':['mean','median', 'max']}).reset_index())

#
if __name__ == "__main__":
    # pData = [0.0] * 25
    # pData.append(0)
    # print(pData)
    # df = pd.read_csv('data1.csv')
    # print(df)
    # prec= df['value']
    # print(list(prec))
    # print(df)
    # # df.plot(x='id_dat',y = 'value')
    # m=df[df['id_dat']==1]
    # d=m[m['crep_id']==1]
    # # print(m)
    # # d['value']=d['value'].astype(int)
    # # d['value']=d['value'].astype()
    # # fig, ax = plt.subplots()
    # plt.figure(figsize=[16,9])
    #
    # # d['create_date'] = pd.to_datetime(d['create_date'])
    # # print(d['create_date'])
    # sls = pd.DataFrame(d,columns=['value','create_date'])
    # sls['create_date']=  pd.to_datetime(sls['create_date'])
    # print(sls)
    # sales = pd.Series(d['value'], index=d['create_date'],)
    # print(sales)
    # plt.plot(sls['create_date'],sls['value'])
    # # plt.gcf().autofmt_xdate()
    # # myFmt = mdates.DateFormatter('%H:%M')
    # # plt.gca().xaxis.set_major_formatter(myFmt)
    #
    # plt.show()
    #

    data_dir = Path("CSV_History")
    df = pd.concat([pd.read_csv(f) for f in data_dir.glob("*.csv")], ignore_index=True)
    df['create_date']= df['create_date'].apply(lambda x: x.split(".")[0])
    df = df[(df['id_dat'] == 1) & (df['crep_id'] == 1)]
    print(df)
    df['create_date']=pd.to_datetime(df['create_date'],format="%Y-%m-%d %H:%M:%S")
    print(df)
    df = df[(df['id_dat'] == 1) & (df['crep_id'] == 1)]


    df = df.groupby(["create_date"])['value'].mean().astype(int).reset_index()
    print(df)
    print("EBAL VAS V ROT")
    print(df.index,df.columns)
    df = pd.DataFrame(df).set_index(['create_date'])
    print(df)

    # # df = df[(df['id_dat']==1) & (df['crep_id']==1)]
    # df = pd.DataFrame(df,columns=['create_date','value'])
    # df.set_index(['create_date'],inplace=True)

    print(df)
    # ts = df[['value']]
    # df.plot()
    mod = sm.tsa.statespace.SARIMAX(df,
                                        order=(1, 0, 1),
                                        seasonal_order=(1, 1, 0, 30)
                                        )
    results=mod.fit()
    results.plot_diagnostics(figsize=(18, 8))
    predict = results.get_forecast(steps=20)
    # ts_p = predict.predicted_mean
    # ts_ci = predict.conf_int()

    # plt.plot(ts_p, label='prediction')
    # plt.plot(ts, color='red', label='actual')
    # plt.plot(df)
    #
    ax = df.plot(label='Текущие данные',figsize=(15, 12), title="Прогноз методом SARIMA")
    # results.fittedvalues.plot(ax=ax, style='--', color='red',label='Прогewfsvdbbdbноз')
    predict.predicted_mean.plot(ax=ax, style='--', color='green',label='Прогноз')
    ax.set_xlabel('Время')
    plt.legend()
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    plt.show()



    # plt.figure(figsize=(16, 10), dpi=80)
    # plt.plot(df['create_date'], df['value'],color='tab:red')
    # plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    # # plt.gca().spines["top"].set_alpha(0.0)
    # # plt.gca().spines["bottom"].set_alpha(0.3)
    # # plt.gca().spines["right"].set_alpha(0.0)
    # # plt.gca().spines["left"].set_alpha(0.3)
    # plt.show()






    # for chunk in pd.read_csv("data.csv",chunksize=1000):
    #     chunk.to_sql("sensors",engine,if_exists="append",index=False)
    # print(len(df['value']))

#
# cross_tab = pd.crosstab(df['id'], df['value'])
# # create a stacked bar chart
# cross_tab.plot(kind='bar', stacked=True)
# # add labels and title
# plt.xlabel('Education Level')
# plt.ylabel('Proportion')
# plt.title('Relationship between Education Level and Income Level')



# sales = pd.Series(df["value"], index=[elem for elem in range(len(df["value"]))])
# print(sales)
# plt.plot(sales.index,sales.values)



# plt.plot([ele for ele in range(len(df['value']))], df['value'])
# # show the plot
# plt.show()