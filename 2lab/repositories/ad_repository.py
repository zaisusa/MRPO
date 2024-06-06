class AdRepository:
    def __init__(self):
        self.ads = []

    def add_ad(self, ad):
        self.ads.append(ad)

    def get_ad(self, ad_id):
        return next((ad for ad in self.ads if ad.id == ad_id), None)
