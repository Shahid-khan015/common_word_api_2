import cloudinary
import cloudinary.uploader
import cloudinary.api

from flask import Flask , jsonify

app =Flask(__name__)

cloud_name='dcysfg3hs'

cloudinary.config(
    cloud_name=cloud_name,
    api_key='697854878477966',
    api_secret='MTxCpMxyUx5i6ZlxEqS-MEaZuQ0'

)

@app.route('/')
def render():
    def list_folders():
        try:
            folders = cloudinary.api.root_folders()
            return folders['folders']
        except cloudinary.exceptions.Error as e:
            print(f"An error occurred while fetching folders: {str(e)}")
            return []

    def get_videos_from_folder(folder_name):
        try:
            resources = cloudinary.api.resources(type='upload', prefix=folder_name, resource_type='video')
            return resources['resources']
        except cloudinary.exceptions.Error as e:
            print(f"An error occurred while fetching videos: {str(e)}")
            return []
    cloudinary_url =  {}
    folders = list_folders()
    for folder in folders:
        folder_name = folder['name']
        if folder_name:
            videos = get_videos_from_folder(folder_name)
            if videos:
                for video in videos:
                    cloudinary_url[folder_name] = video['url']
            else:
                print(f"No videos found in folder '{folder_name}'.")

    limited_cloudinary_url = dict(list(cloudinary_url.items())[:10])

    return jsonify({"words" : limited_cloudinary_url})

 

if __name__ == '__main__':
    app.run(debug=True)

