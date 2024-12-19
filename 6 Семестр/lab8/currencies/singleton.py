def singleton(class_):
    """

    :param class_: 

    """
    instances = {}

    def getinstance(*args, **kwargs):
        """

        :param *args: 
        :param **kwargs: 

        """
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance
