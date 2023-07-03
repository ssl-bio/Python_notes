import os
import requests
from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
# print(f"Status code: {r.status_code}")
if r.status_code == 200:
    # Process information about each submission.
    submission_ids = r.json()
    submission_dicts = []
    for submission_id in submission_ids[:30]:
        # Make a separate API call for each submission.

        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        if r.status_code != 200:
            print(f"Failed for id: {submission_id}\tstatus: {r.status_code}")
        else:
            print('.', end='')
        print(' ')

        response_dict = r.json()

        # Build a dictionary for each article.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)

    # Sort by number of comments
    submission_dicts = sorted(submission_dicts,
                              key=itemgetter('comments'),
                              reverse=True)

    links, icounts, ilabels = [], [], []
    for i in range(0, len(submission_dicts)-1):
        ititle = submission_dicts[i]['title']
        if len(ititle) > 27:
            ititle_sub = ititle[:27] + '...'
        else:
            ititle_sub = ititle
        hn_link = submission_dicts[i]['hn_link']
        comments = submission_dicts[i]['comments']
        links.append(f"<a href='{hn_link}'>{ititle_sub}</a>")
        icounts.append(comments)
        ilabels.append(ititle)

    data = [{
        'type': 'bar',
        'x': links,
        'y': icounts,
        'hovertext': ilabels,
        'marker': {
            'color': 'rgb(250, 50, 20)',  # Red tone
            'line': {
                'width': 1.5,
                'color': 'rgb(25, 25, 25)'  # Grey line
            }
        },
        'opacity': 0.8,
    }]

    my_layout = {
        'title': 'Most-Comments on Hacker News',
        'titlefont': {
            'size': 28
        },
        'xaxis': {
            'title': 'News',
            'titlefont': {
                'size': 24
            },
            'tickfont': {
                'size': 14
            },
        },
        'yaxis': {
            'title': 'Comments',
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
    out_file = f'Hacker_news_v{icounter}'
    if not os.path.exists("images"):
        os.mkdir("images")

    while os.path.exists(out_file):
        icounter += 1
        out_file = f'Hacker_news_v{icounter}'

    # Plot and save file as png
    offline.plot(fig,
                 auto_open=True, image='png', image_filename=out_file,
                 output_type='file', image_width=1600, image_height=900,
                 filename=out_file+'.html', validate=False)
    # offline.plot(fig, filename=out_file)
