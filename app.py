import os
import base64
import requests
import click

GITHUB_USERNAME = 'your username'
GITHUB_REPO = 'your repository name'

@click.command()
@click.option('--file', type=click.Path(exists=True), required=True, help='Path to the image file')
@click.option('--token', prompt=True, hide_input=True, confirmation_prompt=True, help='GitHub Personal Access Token')
def upload_image(file, token):
    """Uploads an image to GitHub and returns the permalink."""
    try:
        with open(file, 'rb') as image_file:
            image_content = base64.b64encode(image_file.read()).decode('utf-8')

        image_name = os.path.basename(file)
        url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{GITHUB_REPO}/contents/{image_name}'
        headers = {
            'Authorization': f'token {token}',
            'Content-Type': 'application/json'
        }
        data = {
            'message': f'Upload image {image_name}',
            'content': image_content
        }
        
        response = requests.put(url, headers=headers, json=data)
        
        if response.status_code == 201:
            file_sha = response.json()['content']['sha']
            permalink = f'https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/main/{image_name}'
            click.echo(f'Image uploaded successfully. Permalink: {permalink}')
        else:
            click.echo(f'Error: {response.json()["message"]}')
    except Exception as e:
        click.echo(f'Error: {e}')

if __name__ == '__main__':
    upload_image()
