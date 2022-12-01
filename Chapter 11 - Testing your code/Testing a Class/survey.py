class AnonymousSurvey():
    """Collect anonymous answersr to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question # survey question you provide
        self.responses = [] # empty list of responses

    def show_question(self):
        """Show the survey question."""
        print(self.question) # method that prints the question

    def store_response(self, new_response):
        """"Store a single response to the survey."""
        self.responses.append(new_response) # adds response to the list

    def show_results(self):
        """Show all the responses they've been given. """
        print("Survey results:") # prints all stored responses
        for response in self.responses:
            print(f" - {response}")