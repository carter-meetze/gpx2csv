from xml.dom import minidom
from datetime import datetime, timedelta
import csv


def gpx2csv(gpx_path):

    try:
        xml = minidom.parse(gpx_path)
        print('gpx file parsed')
    except:
        print('gpx file not parsed')

    try:
        coord = xml.getElementsByTagName('trkpt')
        lon = [x.attributes['lon'].value for x in coord]
        lat = [x.attributes['lat'].value for x in coord]
        print('coordinates: done')
    except:
        print('coordinates: failed')
        pass

    try:
        elevation = [x.firstChild.nodeValue for x in xml.getElementsByTagName('ele')]
        print('elevation: done')
    except:
        print('elevation: failed')
        pass

    try:
        speed = [(float(x.firstChild.nodeValue) * 2.23694) for x in xml.getElementsByTagName('speed')]
        print('speed: done')
    except:
        print('speed: failed')
        pass

    try:
        time_raw = [x.firstChild.nodeValue for x in xml.getElementsByTagName('time')]
        time = []
        for x in time_raw:
            datetime_object = datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ')
            time_value = (datetime_object - timedelta(hours=5)).time()
            time.append(time_value)
        time.pop(0)
        print('time: done')
    except:
        print('time: failed')

    try:
        rows = zip(time, lon, lat, elevation, speed)

        csv_title = 'route_' + str(time[0]) + '.csv'
        with open(csv_title, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['time', 'lon', 'lat', 'elevation', 'speed'])
            for row in rows:
                csvwriter.writerow(row)
        print('csv: done')
        csv_file = 'file created: ' + csv_title
    except:
        print('csv: failed')
        csv_file = 'file not created'

    return print(csv_file)
