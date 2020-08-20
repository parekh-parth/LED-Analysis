import rtsp

client = rtsp.Client(rtsp_server_uri = 'rtsp://admin:Cimcon123@199.199.51.203:554/mpeg/ch1/sub/av_stream')
test = client.read()
print(test)
client.close()
