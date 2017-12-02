import http.client, urllib.request, urllib.parse, urllib.error, base64, json

def imageCaption(imagePath):
    subscription_key =' 7ec1f8ac4b214fdcb94af87b30902578'
    uri_base = 'westcentralus.api.cognitive.microsoft.com'

    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    params = urllib.parse.urlencode({
        'visualFeatures': 'Categories,Description,Color',
        'language': 'en',
    })

    body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/1/12/Broadway_and_Times_Square_by_night.jpg'}"

    try:
        conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()

        parsed = json.loads(data)
        print ("Response:")
        print (json.dumps(parsed, sort_keys=True, indent=2))
        conn.close()

    except Exception as e:
        print('Error:')
        print(e)
        return None

imageCaption('??')
