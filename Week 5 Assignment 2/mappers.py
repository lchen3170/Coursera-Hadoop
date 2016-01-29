def split_show_views(line):
    split = line.split(",")
    show = split[0]
    views = int(split[1])
    return (show, views)


def split_show_channel(line):
    split = line.split(",")
    show = split[0]
    channel = split[1]
    return (show, channel)