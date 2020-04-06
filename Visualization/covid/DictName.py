# This dictionary stores the matching pairs of names in the geopandas and in the Johns Hopkins dataset.
# Key names are country names from geopandas world['name'], value names are names from dataset column 'Country/Region'
# Note: There exist non-matching examples, needs future fix.
DictName = {
    
    'Central African Rep.': ['Central African Republic'],
    "Côte d'Ivoire": ["Cote d'Ivoire"],
    'Dominican Rep.' : ['Dominica'],
    'Eq. Guinea': ['Equatorial Guinea'],
    'eSwatini': ['Eswatini'],
    'South Korea': ['Korea, South'],
    'Taiwan': ['Taiwan*'],
    'United States of America': ['US'],

}