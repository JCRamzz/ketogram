
from clarifai.rest import ClarifaiApp


app = ClarifaiApp(api_key='4ca3a32fd0fc40eeb9bb314978689e3a')

def get_relevant_tags(image_url):
    response_data = app.tag_urls(urls=[image_url], model_id='bd367be194cf45149e75f01d59f77ba7')

    tag_urls = []
    for concept in response_data['outputs'][0]['data']['concepts']:
        tag_urls.append(concept['name'])
    str = "Hello from RowdyHacks\n"
    return str + ' \n'.join(tag_urls[0:3])



print get_relevant_tags('https://brendid.com/wp-content/uploads/2015/10/Pear-Recipes-7.jpg')
