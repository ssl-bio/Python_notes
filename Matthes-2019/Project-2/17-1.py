import os
import requests

from plotly.graph_objs import Bar
from plotly import offline

language = input('Type the language you want to analyze:\n')
# language = 'r'
language = language.lower()
# Make an API call and store the response.
url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
status_code = r.status_code
if status_code == 200:

    # Store API response in a variable.
    response_dict = r.json()

    print(f"Total repositories: {response_dict['total_count']}")

    # Explore information about the repositories.
    repo_dicts = response_dict['items']
    print(f"Repositories returned: {len(repo_dicts)}")
    # Does it always returns 30?

    # PLot a graph
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict['stargazers_count'])
        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(250, 50, 20)',  # Red tone
            'line': {
                'width': 1.5,
                'color': 'rgb(25, 25, 25)'
            }  # Grey line
        },
        'opacity': 0.8,
    }]

    my_layout = {
        'title': f'Most-Starred {language.title()} Projects on GitHub',
        'titlefont': {
            'size': 28
        },
        'xaxis': {
            'title': 'Repository',
            'titlefont': {
                'size': 24
            },
            'tickfont': {
                'size': 14
            },
        },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {
                'size': 24
            },
            'tickfont': {
                'size': 14
            },
        },
    }
    fig = {'data': data, 'layout': my_layout}
    icounter = 1
    out_file = f'{language}_repos_v{icounter}'
    while os.path.exists(out_file):
        icounter += 1
        out_file = f'{language}_repos_v{icounter}'

    if not os.path.exists("images"):
        os.mkdir("images")

    # Plot and save file as png
    # offline.plot(fig, filename=out_file)
    offline.plot(fig,
                 auto_open=True, image='png', image_filename=out_file,
                 output_type='file', image_width=1600, image_height=900,
                 filename=out_file+'.html', validate=False)
