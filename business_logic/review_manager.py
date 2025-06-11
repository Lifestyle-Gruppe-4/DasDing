from data_access.review_data_access import ReviewDataAccess
from model.review import Review


class ReviewManager:
    def __init__(self, review_dal: ReviewDataAccess):
        self.review_dal = review_dal

    def add_review(self, booking_id:int, rating:int, comment:str)-> int:
        review = Review(None, booking_id, rating, comment,None)
        return self.review_dal.create_review(review)

    def get_hotel_reviews(self,hotel_id:int) -> list[Review]:
        return self.review_dal.read_reviews_by_hotel(hotel_id)

