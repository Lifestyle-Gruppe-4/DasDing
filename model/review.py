class Review:
    def __init__(self, review_id, booking_id, rating, comment, created_at):
        self.review_id = review_id
        self.booking_id = booking_id
        self._rating = None # internes Feld initialisieren
        self.rating = rating # ruft hier den Setter ein einziges Mal auf
        self.comment = comment
        self.created_at = created_at

    @property
    def rating(self) -> float: # Gibt den geprüften Rating Wert zurück
        return float(self._rating)
    @rating.setter
    def rating(self, value:int): # validiert und setzt das Feld _rating.
        if not (1<= value <= 5):
            raise ValueError('rating must be between 1 and 5')
        self._rating = value
    # Verhindert unendliche Rekursion