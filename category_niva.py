import pandas as pd


otchet_df = pd.read_excel("otchet.xlsx",sheet_name='otchet')

otchet_d= otchet_df["НАЗВАНИЕ"].str.split(' ')


for prec in range(len(otchet_d)):
    otchet_d[prec] = otchet_d[prec][0]
    otchet_d[prec] = otchet_d[prec].lower()
    # prec = prec[0]

print(otchet_d)

otchet_df["shit"] = otchet_d

otchet_df =otchet_df.groupby(['shit']).count()
print(len(otchet_df))

otchet_df.to_excel("output.xlsx")

