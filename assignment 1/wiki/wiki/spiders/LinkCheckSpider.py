import scrapy

class LinkCheckerSpider(scrapy.Spider):
    name = 'link_checker'
    allowed_domains = ['vi.wikipedia.org']
    start_urls = ['https://vi.wikipedia.org/wiki/Hoa_L%C6%B0']

    maxdepth = 2

    def parse(self, response):
        # Set default meta information for first page
        from_url = ''
        from_text = ''
        depth = 0;
        # Extract the meta information from the response, if any
        if 'from' in response.meta:
            from_url = response.meta['from']
        if 'text' in response.meta:
            from_text = response.meta['text']
        if 'depth' in response.meta:
            depth = response.meta['depth']

        # Update the print logic to show what page contain a link to the
        # current page, and what was the text of the link
        # yield {
        #     "url":response.url,
        #     "title":response.xpath("//title/text()").getall()[0]
        # }
        print(depth, response.url, '<-', from_url, from_text, sep=' ')

        # Browse a tags only if maximum depth has not be reached
        if depth < self.maxdepth:
            a_selectors = response.xpath("//a")
            for selector in a_selectors:
                text = selector.xpath("text()").extract_first()
                link = selector.xpath("@href").extract_first()
                if not link or not text :
                    continue
                yield {
                    "from_url":response.url,
                    "current_url":"https://vi.wikipedia.org"+link,
                }

                request = response.follow(link, callback=self.parse)
                # Meta information: URL of the current page
                request.meta['from'] = response.url
                # Meta information: text of the link
                request.meta['text'] = text
                # Meta information: depth of the link
                request.meta['depth'] = depth + 1

                yield request
