__all__ = ['Property']


class Property:
    def __init__(self, name, type_, number_bedrooms, number_bathrooms, amenities):
        self.name = name
        self.type = type_
        self.number_bedrooms = number_bedrooms
        self.number_bathrooms = number_bathrooms
        self.amenities = amenities

    def __str__(self):
        return (
            'Property\n'
            '==========\n'
            'Name: {}\n'
            'Type: {}\n'
            'Number of bedrooms: {}\n'
            'Number of bathrooms: {}\n'
            'Amenities: {}\n'
            '\n'
        ).format(
            self.name,
            self.type,
            self.number_bedrooms,
            self.number_bathrooms,
            self.amenities,
        )

    def all_is_unknown(self):
        return (
            (None,) * 5
            == (
                self.name,
                self.type,
                self.number_bedrooms,
                self.number_bathrooms,
                self.amenities
            )
        )