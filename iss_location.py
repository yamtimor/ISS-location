import requests
import gmplot

url = 'https://api.wheretheiss.at/v1/satellites/25544'
res = requests.get(url)
iss_json = res.json()


def main():
    """
    Connect to Wheretheiss API and plot the attractions on a map.
    """

    # The lat and lng of the attraction
    attractions_lats = iss_json['latitude']
    attractions_lngs = iss_json['longitude']

    gmap1 = gmplot.GoogleMapPlotter(attractions_lats, attractions_lngs, 1)

    attractions_lats, attractions_lngs = zip(*[(iss_json['latitude'], iss_json['longitude'])])

    gmap1.scatter(attractions_lats, attractions_lngs, color='#3B0B39', size=40, marker=False)

    gmap1.scatter(attractions_lats, attractions_lngs, 'cornflowerblue', edge_width = 3.0)

    gmap1.draw('map.html')

if __name__ == "__main__":
    main()
