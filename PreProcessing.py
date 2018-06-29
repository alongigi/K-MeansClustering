"""
    Filling the missing values (NA) with mean.
    df - Data Frame
"""
def fillMissingValuesWithMean(df):
    df_without_missing_values = df.fillna(df.mean())
    return df_without_missing_values



"""
Returns the mean of specific feature
df - Data Frame
feature_name - The mean of the feature
"""
def getFeatureMean(df, feature_name):
    return df[feature_name].mean()


"""
Returns the STD of specific feature
df - Data Frame
feature_name - The STD of the feature
"""
def getFeatureSTD(df, feature_name):
    return df[feature_name].std()

def normalize(df):
    "Makes a copy of the data frame."
    result = df.copy()
    "For each feature in we normalize the data, except for those feature who are not numeric."
    for feature_name in df.columns:
        try:
            mean = getFeatureMean(df, feature_name)
            std = getFeatureSTD(df, feature_name)

            "Inserting to the feature the normalized value."
            result[feature_name] = (df[feature_name] - mean) / std
        except:
            "Exception is thrown when the feature is not a value, for example country."
            continue
    return result





def kibuz_data(df):
    df = df.groupby("country").mean()
    df.reset_index(inplace=True)
    return df

def getNumberOfRows(df, feature):
    return df[feature].count()
