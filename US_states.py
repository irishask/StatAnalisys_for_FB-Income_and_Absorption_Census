import pandas as pd

class US_States:
    def __init__(self, df_census_states):
        self.us_state_abbrev_dict= {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'District of Columbia': 'DC',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Northern Mariana Islands':'MP',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Palau': 'PW',
            'Pennsylvania': 'PA',
            'Puerto Rico': 'PR',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virgin Islands': 'VI',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY',
        }
        self.df_us_state_abbr = self.Create_df_US_states()
        self.df_census_states_abbr = self.Create_df_Census_states(df_census_states)
        #print(self)

    def __repr__(self):
        mystr = f"US State_abbreviations and State_codes are:\n\{str(self.df_census_states_abbr)} \n" + "-" * 100
        return (mystr)

    def Create_df_US_states(self):
        #Create a dataframe from a dictionary by index:
        df_us_state_abbr = pd.DataFrame.from_dict(self.us_state_abbrev_dict, orient='index', columns=['State_abbr'])
        # Reset index to make from it a regular column. New index will be a default index (=0,1,...).
        df_us_state_abbr.reset_index(inplace=True)
        #Rename column "index" to "State":
        df_us_state_abbr = df_us_state_abbr.rename(columns={"index": "State"})
        #print (f"df_us_state_abbr:\n{df_us_state_abbr}")
        return(df_us_state_abbr)


    def Create_df_Census_states(self, df_census_states):
        # Inner Join by column='State':
        df_Census_states_with_abbr = pd.merge(df_census_states, self.df_us_state_abbr, on='State', how='inner')
        #print (f"df_census_states_with_abbrev:\n{df_Census_states_with_abbr}")
        return (df_Census_states_with_abbr)


















