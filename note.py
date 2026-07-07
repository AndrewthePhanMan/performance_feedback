class Note:
    def __init__(self, onset, duration, pitch, frequency):
        """
            Initializes an instance of the Note class.

            Parameters:
            - onset (float): The location of the onset in seconds.
            - duration (float): The length of the onset in seconds.
            - pitch (str): The musical note's name.
            - frequency (float): The onset's fundamental frequency.
        """
        self.onset = onset
        self.duration = duration
        self.pitch = pitch
        self.frequency = frequency