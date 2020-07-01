import webbrowser


def Start(cfg):
    url = cfg['url']
    webbrowser.open_new_tab(url)
