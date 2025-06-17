from collections import deque

def greater(fifo,lifo):
    return 'lifo' if lifo > fifo else 'fifo'

def divide(x,y):
    return max(x,y) % min(x,y) if min(x,y) != 0 else 0

def append_element(sug_links, feat_art,value, rem):
    result = rem * 2
    match value:
        case 'lifo' : feat_art.append(result)
        case 'fifo' : sug_links.append(result)
    return



suggested_links = deque(map(int, input().split())) # FIFO
featured_articles = list(map(int, input().split())) # LIFO
target_value = int(input())
calcs = {
    'fifo': lambda x: -x ,
    'lifo': lambda x: +x
}
final_feed = []

while suggested_links and featured_articles:
    link = suggested_links.popleft()
    feature = featured_articles.pop()
    remainder = divide(link, feature)

    if link == feature or remainder == 0:
        final_feed.append(0)
        continue

    greater_value = greater(link, feature)

    final_feed.append(calcs[greater_value](remainder))
    append_element(suggested_links, featured_articles, greater_value, remainder)


total_engagement = sum(final_feed)

if final_feed:
    print(f"Final Feed: {', '.join(str(n) for n in final_feed)}")

if total_engagement >= target_value:
    print(f'Goal achieved! Engagement Value: {total_engagement}')
else:
    print(f'Goal not achieved! Short by: {target_value - total_engagement}')

