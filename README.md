# ark-academic-template

Template repository for an academic web site using the [Ark](https://www.dmulholl.com/docs/ark/main/) static site generator.

## How to use

1. Create a new web site repository in your GitHub account from this template by clicking the "Use this template" green button in the upper right corner.

2. Clone your web site repository to your local computer and go to your local clone's root directory in the terminal.

3. If you don't have a recent Python installed, install it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

4. In your web site repository clone's root directory, install all the Python dependencies with the command below.  You may want to use a virtual environment.  If you don't know what that is, don't worry about it.

    ```sh
    pip install -r requirements.txt
    ```


5. In [`site.py`](site.py), update the values in all capitals that start with `YOUR_`.

    Example:
    ```Python
    # GitHub template users, update these values with your own.
    # If you don't have a particular item, set it to None, e.g.:
    #   twitter_handle = None
    title = "YOUR_SITE_TITLE"
    # headshot="@root/images/YOUR_HEADSHOT_PHOTO"
    headshot="@root/images/elsa-small.jpg"
    professional_title ="YOUR_PROFESSIONAL_TITLE"
    professional_email ="YOUR_PROFESSIONAL_EMAIL"
    personal_email ="YOUR_PERSONAL_EMAIL"
    linkedin = "YOUR_LINKEDIN_PAGE"
    twitter_handle ="YOUR_TWITTER_HANDLE"
    github_org = "https://github.com/YOUR_GITHUB_ORG"
    ```



6. Customize all the content in the [`src/`](src/) directory.

7. Build your site with:

    ```sh
    ark build
    ```

    This will generate a static site and store it in the `docs/` directory.

8. Commit your changes and push to GitHub.

    ```sh
    git add .
    git commit -m "Add awesome content"
    git push
    ```

    Of course, if you use developer workflows you can create branches and pull requests.

Your new content should be visible at `https://YOUR_GITHUB_USERNAME.github.io/YOUR_WEB_SITE_REPO_NAME`.

> While you are developing your site on your machine, you can run `ark watch` and see the changes in your local browser before committing changes and pushing to GitHub.




