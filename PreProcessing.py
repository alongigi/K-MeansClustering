import pandas as pd

df = pd.read_excel('data.xlsx')

"""
    Filling the missing values (NA) with mean.

    df - Data Frame
"""


def fillMissingValuesWithMean(df):
    df_without_missing_values = df.fillna(df.mean())
    return df_without_missing_values


df = fillMissingValuesWithMean(df)

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


"""
Normilizes the data frame by mean and value -> (value - mean) / STD

df - Data Frame.
"""


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


def kibuzData(df):
    # The keys of the dictionary will be the countries names, and their values will contain sum for each feature
    # for example if the sum of the feature 'Life Ladder' will be 2000 then in index 4 for example in the value array
    # will be 2000.
    # Moreover, the first index will contain the number of instances of the same country
    # For example, if the country 'Israel' appeared three time in the original df the in index 0 will be the number 3.
    data_frame_data = {}

    number_of_rows = getNumberOfRows(df, "country") - 1
    # Contains the names of all features
    feature_names = list(df.columns.values)

    # Running index which represent the current row in the dataframe
    current_row = 0

    # The purpose of this while is to collect each data for each country and put it in the 'data_frame_data' as value,
    # except for year data
    while current_row < number_of_rows:
        current_country_name = df["country"][current_row]

        # Creates a new array if the country name is not exists in the keys
        if not current_country_name in data_frame_data:
            data_frame_data[current_country_name] = [0] * (len(feature_names) - 1)

        # updating the number of instances of specific country.
        data_frame_data[current_country_name][0] += 1

        feature_index = 1
        for feature_name in feature_names:
            if feature_name in ['country', 'year']:
                continue

            data_frame_data[current_country_name][feature_index] += df[feature_name][current_row]
            feature_index += 1

        current_row += 1

    return create_new_data_frame(data_frame_data, feature_names)


def create_new_data_frame(data_frame_data, feature_names):
    """
    Responsible for making a new data frame based on the given data and feature names

    :param data_frame_data:
    :param feature_names:
    :return:
    """

    # Will contain many hash tables. Each of the hash table will represent a row in the new data frame.
    new_data_frame_array = []

    for feature in data_frame_data:
        new_data_frame_row_data = data_frame_data[feature]
        for i in range(len(new_data_frame_row_data)):
            # The first index consist the number of instances, something which need to be passed because we will
            # use it to calculate the country's features average.
            if i == 0:
                continue
            new_data_frame_row_data[i] = new_data_frame_row_data[i] / new_data_frame_row_data[0]
        new_data_frame_row_data[0] = feature

        current_row = 0
        # Represents a new row in the new data frame.
        new_data_frame_row = {}
        for current_feature in feature_names:
            if current_feature == "year":
                continue

            new_data_frame_row[current_feature] = new_data_frame_row_data[current_row]
            current_row += 1

        new_data_frame_array.append(new_data_frame_row)

    # Creating a new data frame based on the calculated data before
    new_df = pd.DataFrame(new_data_frame_array)

    return new_df


def getNumberOfRows(df, feature):
    return df[feature].count()


new_df = kibuzData(df)
print new_df
# print(kibuzData(df))
