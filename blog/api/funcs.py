from api.serializers import APICommentSerializer


def nesting_comments(comments, nesting_level):
    if not nesting_level:
        return None

    data = []

    for comment in comments:
        serialized_data = APICommentSerializer(comment).data
        serialized_data.update({
            "reply": nesting_comments(comment.child.all(), nesting_level - 1)
        })
        data.append(serialized_data)

    return data
