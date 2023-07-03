import os
import plotly.express as px
# from plotly import offline
import pandas as pd
import search_github_repos as sgh

language = 'python'
python_repos = sgh.query_github_repos(language)
repo_dicts = python_repos['items']

repo_links, stars, descriptions, names = [], [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])
    # owner = repo_dict['owner']['login']
    description = repo_dict['description']
    # label = f"{owner}<br />{description}"
    descriptions.append(description)
    names.append(repo_name)

# Create a pandas dataframe
data = {'Repository': names, 'N stars': stars, 'Description': descriptions}
df = pd.DataFrame(data)
df_inv = df.sort_values(by='N stars')


# Create a plotly object
fig = px.bar(df_inv, y='Repository', x='N stars',
             orientation='h', text='N stars',
             hover_name='Description',
             color='N stars', color_continuous_scale='Burg',
             title=f"Most-Starred {language.title()} Projects on GitHub")

# Show figure
# fig.show()
icounter = 1
out_file = f'{language.title()}_repos_px_v{icounter}'
if not os.path.exists("images"):
    os.mkdir("images")

while os.path.exists(out_file):
    icounter += 1
    out_file = f'{language.title()}_repos_px_v{icounter}'

# Plot and save file as png
fig.write_image("./images/"+out_file+".png", width=1600, height=900)
