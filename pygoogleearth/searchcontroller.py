class SearchController(object):
    """
    This contains search options and controls.
    
    Use this interface to control searches and their results.
    
    To get a search controller get the search_controller property
    from a GoogleEarth instance.
    """
    def __init__(self, comobject):
        self.ge_ac = comobject
    
    def search(self, search_string):
        """
        Performs a regular search.

        Performs a search given a search string. This search string may 
        represent a location, driving directions, businesses, or anything 
        else possible through Google Earth's regular search box.

        There is a limit on the number of searches within a certain time period. When this limit is exceeded, the function returns E_USAGE_LIMIT_EXCEEDED, and the search is not performed. This restriction is subject to change.

        Note:
        This function may return before search is actually complete, which 
        means that GetResults might not immediately reflect very recent searches 
        made. Use IsSearchInProgress to check if there is a search in progress.

        Parameters:
        searchString     string containing search parameters. Could contain 
                         special keywords such as "near", "from:", "to:", etc.
        """
        self.ge_ac.Search(search_string)
    
    def is_search_in_progress(self):
        """
        Checks if there is any search currently in progress.

        Useful for knowing when search is complete after calling Search and 
        before calling GetResults.
        """
        return self.ge_ac.IsSearchInProgress()
    
    def get_results(self):
        """
        Retrieves search results.

        Retrieves the collection of features in the search results.

        Note:
        Searches may take a few moments to complete, which means that 
        GetResults might not immediately reflect very recent searches 
        made. Use IsSearchInProgress to check if there is a search 
        in progress.
        """
        return self.ge_ac.GetResults()
    
    def clear_results(self):
        """
        Clears all search results.

        Clears all the features from search results.
        """
        self.ge_ac.ClearResults()
    