# Build a function that takes two lists, one of YouTube video titles and one of their view counts, and returns a list of tuples with each title and its rounded view count (to the nearest thousand using round()).<br><br><em><strong>Hint:</strong> Use zip() to pair titles and counts, and round() inside a list comprehension.</em>


def youtube(total,count):
    return list(zip(total,count))

video_titles = ("vlog","gaming","tutorial","sports","fooding")
view_counts = (12001,12301,43501,56701,67601)
final = (round(i,-3) for i in view_counts)

print(youtube(video_titles,final))

