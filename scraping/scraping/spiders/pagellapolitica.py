import scrapy


class PagellapoliticaSpider(scrapy.Spider):
    name = 'pagellapolitica'
    allowed_domains = ['pagellapolitica.it']
    start_urls = ['https://pagellapolitica.it/dichiarazioni/verificato/']

    # {css class name: truthness value}
    css_mapping = {"mark-vero":"true",
                   "mark-ceri": "almost_true",
                   "mark-ni": "ni",
                   "mark-pinocchi": "almost_false",
                   "mark-panzana":"false"}


    def parse(self, response):
        
        statement_articles_links = response.css("a.statement-link::attr(href)").getall()

        for article_href in statement_articles_links:
            yield scrapy.Request(response.urljoin(article_href), callback=self.parse_article)


    def parse_article(self, response):
        
        politician = response.css("p a.u-link-muted::text").get().strip()
        title = response.css("span.h2::text").get().strip()
        statement = response.css("p.lead::text").get().strip()
        
        for css_class, truth_value in self.css_mapping.items():
            if response.css(f"span.h2.{css_class}"):
                truthness = truth_value

        claim_source_url = (response.css("i.fa-external-link-alt") # icon
                                    .xpath("..") # get parent
                                    .attrib["href"]) # get parent href

        dates = response.css(".card-body .row span::text")[:2].getall()
        
        article_date = dates[0]
        claim_date = dates[1]

        self.logger.info(f"DATA: {politician} say  {statement} that is {truthness}")
