# Image Uploader CLI

## Overview

Image Uploader CLI is a command line tool that allows users to upload images to a GitHub repository and generate permalinks for them. This tool simplifies the process of sharing images online by automating the upload and link generation steps.

Made this after seeing this [idea list](https://www.ishan.coffee/notes/Idea-List)!

## Features

- Upload images to a specified GitHub repository.
- Generate permanent links (permalinks) for the uploaded images.
- Securely handle GitHub personal access tokens.
- Easy-to-use command line interface.

## Requirements

- Python 3.6 or higher
- GitHub account
- GitHub repository for storing the images
- GitHub personal access token with `repo` scope

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/retrogtx/image-uploader-cli.git
   cd image-uploader-cli
   ```

2. **Set Up a Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```sh
   pip install requests click
   ```

## Usage

### Running the CLI Tool

1. **Ensure you have a GitHub Personal Access Token:**
   - Go to GitHub > Settings > Developer settings > Personal access tokens > Generate new token.
   - Select the `repo` scope and generate the token.

2. **Upload an Image:**
   ```sh
   python upload_image.py --file path/to/your/image.jpg
   ```

3. **Enter your GitHub Personal Access Token when prompted:**
   ```sh
   GitHub Personal Access Token:
   Confirm GitHub Personal Access Token:
   ```

4. **Get the Permalink:**
   - The script will output the permalink if the upload is successful:
     ```sh
     Image uploaded successfully. Permalink: https://raw.githubusercontent.com/your_github_username/your_repo_name/main/image.jpg
     ```

### Example

```sh
$ python upload_image.py --file path/to/your/image.jpg
GitHub Personal Access Token:
Confirm GitHub Personal Access Token:
Image uploaded successfully. Permalink: https://raw.githubusercontent.com/your_github_username/your_repo_name/main/image.jpg
```

## Configuration

- **GitHub Username and Repository:**
  - Set your GitHub username and repository name in the script:
    ```python
    GITHUB_USERNAME = 'your_github_username'
    GITHUB_REPO = 'your_repo_name'
    ```

