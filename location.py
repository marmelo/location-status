#!/usr/bin/env python
import rumps
import json
import urllib2


class LocationStatus(rumps.App):
    
    def __init__(self):
        super(LocationStatus, self).__init__("Location", "--")
        
        self.info_ip = rumps.MenuItem('Not Available')
        self.info_isp = rumps.MenuItem('Not Available')
        self.info_location = rumps.MenuItem('Not Available')
        
        self.menu = [
            self.info_ip,
            self.info_isp,
            self.info_location,
            None
        ]
        
        rumps.Timer(self.update, 30).start()
    
    def update(self, timer):
        data = self.ipinfo()
        
        if data:
            self.title = data['country_code']
            self.info_ip.title = data['ip']
            self.info_isp.title = data['isp']
            self.info_location.title = "%s, %s" % (data['city'], data['country'])
        else:
            self.title = "--"
            self.info_ip.title = "Not Available"
            self.info_isp.title = "Not Available"
            self.info_location.title = "Not Available"
    
    def ipinfo(self):
        try:
            data = urllib2.urlopen("http://www.telize.com/geoip").read()
            return json.loads(data)
        except Exception:
            return None

LocationStatus().run()
