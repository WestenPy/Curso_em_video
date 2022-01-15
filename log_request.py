def log_request(req, res):
    """
    ->
    :param req: 'flask_request'
    :param res: str
    :return: none
    """
    with open('vsearch.log', 'a') as log:
        print(req, res, file=log)
