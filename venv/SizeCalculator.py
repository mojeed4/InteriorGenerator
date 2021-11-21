class SizeCalculator:
    def __init__(self, trim_size, page_count, interior_type):
        self.trim_size = trim_size
        self.page_count = page_count
        self.interior_type = interior_type

    BLEED = 0.125

    def get_spine_size(self):
        #Cream paper = 0, Colored paper = 1, White paper = others
        spine_per_page = 0.002252
        if self.interior_type == 0:
            spine_per_page = 0.0025
        elif self.interior_type == 1:
            spine_per_page = 0.002347

        return spine_per_page * self.page_count

    def get_trim_width(self):
        return self.trim_size[0]

    def get_trim_height(self):
        return self.trim_size[1]

    def get_cover_width(self):
        return 2 * self.trim_size[0] + 2 * self.BLEED + self.get_spine_size()

    def get_cover_height(self):
        return self.trim_size[1] + 2 * self.BLEED

    def get_cover_size(self):
        return (self.get_cover_width(), self.get_cover_height())