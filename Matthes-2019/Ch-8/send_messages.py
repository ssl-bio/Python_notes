def send_messages(msg_list):
    """Sends messages from a list and returns a list of sent ones
    """
    
    sent_msgs = []
    while msg_list:
        msg = msg_list.pop()
        sent_msgs.append(msg)

    if sent_msgs:
        return sent_msgs
