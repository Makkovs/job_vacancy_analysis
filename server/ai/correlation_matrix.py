def correlation_matrix (values):
    skills_df = values.drop(columns=["qualification", "experience"])
    skills_df = skills_df.loc[:, ~skills_df.columns.str.startswith("country")]
    correlation_matrix = skills_df.corr()

    return correlation_matrix