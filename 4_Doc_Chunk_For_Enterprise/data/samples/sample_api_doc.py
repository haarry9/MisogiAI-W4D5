# -*- coding: utf-8 -*-

class UserAPI:
    """
    API for managing user accounts.
    """
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_user(self, user_id: int):
        """
        Retrieves a user by their ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            dict: The user's data or None if not found.
        """
        if not isinstance(user_id, int):
            raise ValueError("user_id must be an integer.")
        
        # In a real scenario, this would make an API call.
        print(f"Fetching user {user_id}...")
        return {"id": user_id, "name": "Jane Doe"}

def calculate_metrics(data: list) -> dict:
    """
    Calculates metrics from a list of data points.
    
    This function is part of the data processing library and is used
    across different services.
    """
    if not data:
        return {}
    
    # Complex calculation logic would be here.
    return {"mean": sum(data) / len(data), "size": len(data)} 