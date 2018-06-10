import matplotlib.pyplot as plt
#import plotly.plotly as py

from sklearn.cluster import KMeans

def KMean(df, n_clusters, n_init):
    km = KMeans(n_clusters=int(n_clusters), n_init=int(n_init))
    km.fit(df)
    return km.fit_predict(df)

def show_result(df, x):
    for i in range(0, len(x)):
        print("{} : {}".format(df.index[i], x[i]))
    df1 = df[['Social support']]
    df2 = df[['Generosity']]
    t = plt.scatter(df1, df2, c=x)
    plt.colorbar(t)
    plt.xlabel('Social support')
    plt.ylabel('Generosity')
    plt.title('Generosity depending on social support')
    plt.legend()

    #py.sign_in(username="elichoen", api_key="GwoAb5aLpuUsAlZSdOXb")

    #data = [dict(type='choropleth', locations=df['country'], z=df['Cluster'], locationmode='country names', colorscale=[[0, "rgb(5, 10, 172)"], [0.35, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"], [0.6, "rgb(90, 120, 245)"], [0.7, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]], autocolorscale=False, reversescale=True,
    #    marker=dict( line=dict( color='rgb(180,180,180)', width=0.5)), colorbar=dict(autotick=False, title='KMeans Clustering'),)]
    #layout = dict(title='KMeans Clustering', geo=dict(showframe=False, showcoastlines=False, projection=dict(type='Mercator')))
    #fig = dict(data=data, layout=layout)
    #py.iplot(fig, validate=False, filename='world-map')
    #py.image.save_as(fig, filename='KMeansWorldMap.png')

    plt.show()