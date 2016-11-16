import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

#TVN24
url_TVN24 = 'http://dcs-188-64-85-94.atmcdn.pl/streams/o2/tvnplayer/nlive/tvn24/live.livx'
li_TVN24 = xbmcgui.ListItem('TVN 24', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url_TVN24, listitem=li_TVN24)

#TVPINFO
url_TVPINFO = 'http://46.28.242.9/token/video/live/12274096/20161116/2967709000/0c96b298-e5be-4b08-bdbd-34b22b37ab56/tvpinfo.isml/tvpinfo.m3u8'
li_TVPINFO = xbmcgui.ListItem('TVP INFO', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url_TVPINFO, listitem=li_TVPINFO)

#ESKATV
url_ESKATV = 'http://stream.smcloud.net/live/eskatv/playlist.m3u8'
li_ESKATV = xbmcgui.ListItem('ESKATV', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url_ESKATV, listitem=li_ESKATV)

#Polsat Sport
url_POLSATSPORT = 'http://dcs-188-64-85-94.atmcdn.pl/streams/mm/multimedia/live/polsat_sport/live.livx'
li_POLSATSPORT = xbmcgui.ListItem('Polsat Sport', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url_POLSATSPORT, listitem=li_POLSATSPORT)

xbmcplugin.endOfDirectory(addon_handle)
