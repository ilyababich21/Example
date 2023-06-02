# import csv
#
# data = [[1, 2, 3], ['a', 'b', 'c'], ['Python', 'Arduino', 'Programming']]
# with open('example.csv', 'w') as f:
#     w = csv.writer(f)
#     for row in data:
#         w.writerow(row)


# import csv
# with open('example.csv', 'r') as file:
#     r = csv.reader(file)
#     for row in r:
#         print(row)



# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# # Set the seed for reproducibility
# # np.random.seed(42)
# # # Create a datetime index with a frequency of 1 day for the year 2022
# # dates = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
# # # Create a pandas series of random values with the datetime index
# # daily_sales = pd.Series(np.random.randint(100, 1000, len(dates)), index=dates)
# # # Resample the series to monthly frequency and calculate the mean value for each month
# # monthly_sales_mean = daily_sales.resample('M').mean()
# # # Plot the monthly sales means
# # plt.plot(monthly_sales_mean)
# # plt.title('Monthly Sales Mean')
# # plt.xlabel('Month')
# # plt.ylabel('Sales Mean')
# # plt.show()
# df = pd.DataFrame(np.random.randn(10, 2), columns=['Column_A', 'Column_B'])
# # Creating a line plot
# df.plot()



#
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# np.random.seed(123)
# dealerships = ['A', 'B', 'C', 'D']
# makes = ['Toyota', 'Honda', 'Ford']
# models = ['Corolla', 'Civic', 'Fiesta']
# data = pd.DataFrame({
# 'dealership': np.random.choice(dealerships, size=100),
# 'make': np.random.choice(makes, size=100),
# 'model': np.random.choice(models, size=100),
# 'sales': np.random.randint(1, 50, size=100)
# })
# print(data)
# totals = data.groupby('dealership')['sales'].sum()
# totals.plot(kind='bar')
# plt.title('Total Sales by Dealership')
# plt.xlabel('Dealership')
# plt.ylabel('Total Sales')
# plt.show()
# by_make = data.groupby(['dealership', 'make'])['sales'].sum()
# # by_make = data.groupby(['dealership', 'make'])['sales'].sum().unstack()
# by_make.plot(kind='bar', stacked=True)
# plt.title('Sales by Make and Dealership')
# plt.xlabel('Dealership')
# plt.ylabel('Total Sales')
# plt.show()
# by_make_mean = data.groupby('make')['sales'].mean()
# by_make_mean.plot(kind='bar')
# plt.title('Average Sales by Make')
# plt.xlabel('Make')
# plt.ylabel('Average Sales')
# plt.show()
#
#
# import pandas as pd
# from wordcloud import WordCloud, STOPWORDS
# import matplotlib.pyplot as plt
# # Load data into dataframe
# df = pd.read_csv('restaurant_reviews.csv')
# # Clean text data
# df['review_text'] = df['review_text'].str.replace('[^\w\s]','')
# df['review_text'] = df['review_text'].str.replace('\d+','')
# df['review_text'] = df['review_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in
# (STOPWORDS)]))
# # Create word cloud
# wordcloud = WordCloud(max_words=100, width=800, height=400, colormap='Blues').generate(''.join(df['review_text']))# Display the cloud
# plt.figure(figsize=(12,6))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()



import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

import json
vk = open('result.json', 'r', encoding='utf8')
vk = json.load(vk)
stop_words = open('stop-ru.txt', 'r', encoding='utf8')
stop_words = stop_words.read()
stop_words = stop_words.split('\n')



mas = []

for i in range(len(vk['messages'])):

    try:
        mas.append(vk['messages'][i]['text'].split(' '))
    except:
        print("Ne udalos")
#
data = []
for i in mas:
    for j in range(len(i)):
        data.append(i[j].lower())

clear_data=[]
for i in data:
    if(i not in stop_words):
        clear_data.append(i)

big_string=''
for i in range(len(clear_data)):
    big_string+=(clear_data[i]+' ')


print(big_string)
#
# wordCloud = WordCloud(width = 10000, height = 10000, random_state=1, background_color='black', colormap='Set2', collocations=False).generate(big_string[:1000])
wordcloud = WordCloud(max_words=1000, width=800, height=1200, colormap='Blues').generate(big_string)


# plt.figure(figsize=(5,5))
# plt.imshow(wordCloud)
plt.figure(figsize=(24,12))
# plt.imshow(wordcloud, interpolation='bilinear')
plt.imshow(wordcloud, )
plt.axis('off')
plt.show()

#
# import pandas as pd
# from wordcloud import WordCloud, STOPWORDS
# import matplotlib.pyplot as plt
# # Load data into dataframe
# df = pd.read_csv('restaurant_reviews.csv')
# # Clean text data
# print(df)
# df['Reviewer'] = df['Reviewer'].str.replace('[^\w\s]','')
# df['Reviewer'] = df['Reviewer'].str.replace('\d+','')
# df['Reviewer'] = df['Reviewer'].apply(lambda x: ' '.join([word for word in str(x).split() if word not in
# (STOPWORDS)]))
# # Create word cloud
# print(''.join(df['Reviewer']))
# wordcloud = WordCloud(max_words=100, width=800, height=400, colormap='Blues').generate(''.join(df['Reviewer']))
# # Display the cloud
# plt.figure(figsize=(12,6))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()
