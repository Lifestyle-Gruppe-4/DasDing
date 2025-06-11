from data_access import base_data_access, BaseDataAccess
from model.review import Review

class ReviewDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_review(self, review: Review)-> int:
        sql = """
        INSERT Into Review (booking_id, rating, comment)
        VALUES (?, ?, ?)
        """
        params = (review.booking_id, review.rating, review.comment)
        lastrowid, _ = self.execute(sql, params)
        return lastrowid

    def read_reviews_by_hotel(self, hotel_id: int) -> list[Review]:
        sql = """
    SELECT r.review_id,
           r.booking_id,
           r.rating,
           r.comment,
           r.created_at
      FROM Review r
      JOIN Booking b ON r.booking_id = b.booking_id
      JOIN Room    ro ON b.room_id    = ro.room_id
     WHERE ro.hotel_id = ?
        """
        rows = self.fetchall(sql, (hotel_id,))
        return [Review(*row) for row in rows]
