# gpx2csv
A simple gpx route parser

I use this script to parse running routes for visualizations

This script will parse any .gpx and output a csv file with the following attributes:
  - Time (year-month-day hour:minute:second)
  - Longitude coordinates
  - Latitude coordinates
  - Elevation
  - Speed (mph)
  
Example csv:

input: print(pd.read_csv('/path/to/file.csv'))

output:
          time        lon        lat  elevation     speed
0     07:34:01 -77.348626  38.559601  73.151627  7.112458
1     07:34:03 -77.348619  38.559550  72.167885  7.204938
2     07:34:03 -77.348618  38.559544  72.043190  7.208056
3     07:34:04 -77.348613  38.559515  71.484299  7.286870
4     07:34:05 -77.348609  38.559486  70.920830  7.382260
...        ...        ...        ...        ...       ...
7294  09:36:13 -77.349965  38.561323  64.685814  0.000000
7295  09:36:14 -77.349965  38.561323  64.685814  0.000000
7296  09:36:15 -77.349965  38.561323  64.685814  0.000000
7297  09:36:16 -77.349965  38.561323  64.685814  0.000000
7298  09:36:17 -77.349965  38.561323  64.685814  0.000000

[7299 rows x 5 columns]
