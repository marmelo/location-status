#!/usr/bin/env python
import rumps
import json
import urllib2


class LocationStatus(rumps.App):
    
    def __init__(self):
        super(LocationStatus, self).__init__("Location", "--")
        rumps.Timer(self.update, 5).start()
    
    def update(self, timer):
        data = self.ipinfo()
        self.title = data['country_code'] if data else "--"
        
    def ipinfo(self):
        try:
            data = urllib2.urlopen("http://www.telize.com/geoip").read()
            return json.loads(data)
        except Exception:
            return None

LocationStatus().run()
