import http.client
def sendMsg(mobile, message):
    message = message.replace(" ", "%20")
    print("http://server1.vmm.education/VMMCloudMessaging/AWS_SMS_Sender?username=" + 'smstester123' + "&password="
                 + 'QBSAH60R' + "&message=" + message + "&phone_numbers=" + mobile)
    conn = http.client.HTTPConnection("server1.vmm.education")
    conn.request("GET",
                 "http://server1.vmm.education/VMMCloudMessaging/AWS_SMS_Sender?username=" + 'smstester123' + "&password="
                 + 'QBSAH60R' + "&message=" + message + "&phone_numbers=" + mobile)

    # url = "http://server1.vmm.education/VMMCloudMessaging/AWS_SMS_Sender?username=" + 'smstester123' + "&password="
    #              + 'QBSAH60R' + "&message=" + message + "&phone_numbers=" + mobile
    response = conn.getresponse()
    if response == 200:
        print(response.headers)
        return True
    else:
        return False


sendMsg(mobile='8847684874', message="This is Demo Msg")
