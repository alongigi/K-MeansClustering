import matplotlib.pyplot as plt
import plotly.plotly as py

from sklearn.cluster import KMeans

"""
Responsible for the Kmeans idea as taught in class.
:Param {df} the the frame of the program
:Param {n_clusters} The number of clusters
:Param {n_init} Num of runs.
"""


def KMean(df, n_clusters, n_init):
    km = KMeans(n_clusters=int(n_clusters), n_init=int(n_init))
    km.fit(df)
    df['Clustering'] = km.fit_predict(df)


"""
Responsible for saving the results
extracting the cluster column data from the data frame

:Param {df} the the frame of the program
:Param {path} Path of the folder.
"""


def save_result(df, path):
    clustering = df['Clustering']
    df1 = df[['Social support']]
    df2 = df[['Generosity']]
    t = plt.scatter(df1, df2, c=clustering)
    plt.colorbar(t)
    plt.xlabel('Social support')
    plt.ylabel('Generosity')
    plt.title('Scatter')
    plt.legend()
    plt.savefig(path + 'Scatter.png')

    py.sign_in(username="avi123456789", api_key="JRT8ZyGZ3fIUwGH8AIl5")
    df.reset_index(inplace=True)
    data = [dict(
        type='choropleth',
        locations=df['country'],
        z=clustering,
        locationmode='country names',
        colorscale=[[0, "rgb(5, 10, 172)"], [0.35, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"],
                    [0.6, "rgb(90, 120, 245)"], [0.7, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]],
        autocolorscale=False,
        reversescale=True,
        marker=dict(
            line=dict(
                color='rgb(180,180,180)',
                width=0.5
            )),
        colorbar=dict(
            autotick=False,
            title='cluster'),
    )]
    layout = dict(title='Horopleth Map', geo=dict(showframe=False, showcoastlines=False, projection=dict(type='Mercator')))
    fig = dict(data=data, layout=layout)
    py.iplot(fig, validate=False, filename='world-map')
    py.image.save_as(fig, filename=path + 'HoroplethMap.png')
