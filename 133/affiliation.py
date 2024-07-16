def generate_affiliation_link(url):
    """
    The segment following /dp/ seems to be the affilate number.
    """
    affiliate_number = str.split(url.split("/dp/")[1], "/")[0]

    return f"http://www.amazon.com/dp/{affiliate_number}/?tag=pyb0f-20"
